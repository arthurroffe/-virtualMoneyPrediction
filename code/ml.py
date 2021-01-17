import sqlite3 as sql
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn import tree
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import accuracy_score as acc
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import ImageTk, Image
import datetime
def ml(name):
    get_today = datetime.date.today()
    today = str(get_today)
    #連結資料庫
    conn = sql.connect('cash_'+today+'.db')
    print('連結資料庫..')
    c = conn.cursor()
    #讀取資料庫
    sql_select = 'select * from '+name
    c.execute(sql_select)
    select_all = c.fetchall()
    
    #整理資料
    date = []
    openm = []
    high = []
    low = []
    close = []
    volume = []
    volume_ok = []
    marketCap = []
    eu_un_lis = []
    
    for i in select_all:
        date.append(i[0])
        openm.append(int(i[1]))
        high.append(int(i[2]))
        low.append(int(i[3]))
        close.append(int(i[4]))
        volume.append(int(i[5]))
        marketCap.append(int(i[6]))
    conn.close()
    
    BTC = {}
    #data= pd.to_datetime(date)
    BTC['date'] = date
    BTC['open'] = openm
    BTC['high'] = high
    BTC['low'] = low
    BTC['close'] = close
    BTC['volume'] = volume
    BTC['marketCap'] = marketCap
    
    
    
    btc = pd.DataFrame(BTC,columns=('date','open','high','low','close','volume',
                                    'marketCap','damage'))
    #計算今日收盤價有沒有比前日收盤高或低，如果比較低代表跌(0)反之1=up 0=down
    for i in range(0,len(btc['close'])-1):
        if btc['close'][i] > btc['close'][i+1]:
            btc.loc[i,['damage']] = 1
        elif btc['close'][i] <= btc['close'][i+1]:
            btc.loc[i,['damage']] = 0
    btc['damage'] = btc['damage'].fillna(0)
    
    btc['date'] = pd.to_datetime(btc['date'])
    
    #製作模型
    x = pd.DataFrame(btc[['open','high','low','volume','close']])
    y = btc['damage'].astype('int')
    
    x_open = pd.DataFrame(btc[['high','low','volume','close']])
    y_open = btc['open'].astype('int')
    
    x_high = pd.DataFrame(btc[['open','low','volume','close']])
    y_high = btc['high'].astype('int')
    
    x_low = pd.DataFrame(btc[['open','high','volume','close']])
    y_low = btc['low'].astype('int')
    
    x_close = pd.DataFrame(btc[['open','low','volume','high']])
    y_close = btc['close'].astype('int')
    
    x_volume = pd.DataFrame(btc[['open','low','high','close']])
    y_volume = btc['volume'].astype('int')
    
    #複回歸
    lm = LinearRegression()
    lm.fit(x_open,y_open)
    pre_open = lm.predict(x_open)
    print('開盤價準確度=',lm.score(x_open,y_open))
    
    lm2 = LinearRegression()
    lm2.fit(x_high,y_high)
    pre_high = lm.predict(x_high)
    print('最高價準確度=',lm.score(x_high,y_high))
    
    lm3 = LinearRegression()
    lm3.fit(x_low,y_low)
    pre_low = lm.predict(x_low)
    print('最低價準確度=',lm.score(x_low,y_low))
    
    lm4 = LinearRegression()
    lm4.fit(x_close,y_close)
    pre_close = lm.predict(x_close)
    print('收盤價準確度=',lm.score(x_close,y_close))
    
    lm5 = LinearRegression()
    lm5.fit(x_volume,y_volume)
    pre_volume = lm.predict(x_volume)
    print('成交量準確度=',lm.score(x_volume,y_volume))
    
    #決策樹
    max_acc = 0
    max_d = 0
    for i in range(1,101):
        dtree = tree.DecisionTreeClassifier(max_depth=i)
        dtree.fit(x,y)
        pred = dtree.predict(x)
        ACC = acc(y,pred)
        if ACC > max_acc :
            max_acc = ACC
            max_d = i
        print(f'計算最高準確度深度{i/100*100:.1f}')
            
    print('決策樹原始模型最高準確度:',max_acc)
    print('決策樹原始模型最高準確度深度:',max_d)
    
    
    
    #使用模型產生的結果去預測damage
    pred_dataframe = pd.DataFrame([pre_open,pre_high,pre_low,pre_close,pre_volume,pre_open]).T
    pred_dataframe.columns = ['open','high','low','close','volume','damage']
    
    for i in range(0,len(pred_dataframe['close'])-1):
        if pred_dataframe['close'][i] > pred_dataframe['close'][i+1]:
            pred_dataframe.loc[i,['damage']] = 1
        elif pred_dataframe['close'][i] <= pred_dataframe['close'][i+1]:
            pred_dataframe.loc[i,['damage']] = 0
    pred_dataframe['damage'].fillna(0)
    #預測使用預測資料的damage
    new_pred_x = pd.DataFrame(pred_dataframe[['open','high','low','close','volume']])
    new_pred_y = pred_dataframe['damage'].astype('int')
    #算最大準確度
    max_pred_acc = 0
    max_pred_d = 0
    for i in range(1,101):
        dtree2 = tree.DecisionTreeClassifier(max_depth=i)
        dtree2.fit(new_pred_x,new_pred_y)
        pred_new_1 = dtree2.predict(new_pred_x)
        pred_acc = acc(new_pred_y,pred_new_1)
        if pred_acc > max_pred_acc:
            max_pred_acc = pred_acc
            max_pred_d = i
        print(f'計算最高準確度深度{i/100*100:.1f}')
    print('決策樹原始模型最高準確度:',max_pred_acc)
    print('決策樹原始模型最高準確度深度:',max_pred_d)

    #將結果繪製圖表
    plt.rcParams['font.family']='Microsoft JhengHei'
    plt.rcParams['axes.facecolor'] = 'slategrey'
    plt.figure(dpi=300,figsize=(15,10),facecolor='slategrey')
    plt.title(name+'20天預測圖表')
    plt.xlabel('時間')
    plt.ylabel('金額')
    plt.scatter(btc['date'][0:20],pred_dataframe['open'][0:20],c='#2894FF',label='預測開盤')
    plt.scatter(btc['date'][0:20],pred_dataframe['high'][0:20],c='#00EC00',label='預測最高')
    plt.scatter(btc['date'][0:20],pred_dataframe['low'][0:20],c='#FF2D2D',label='預測最低')
    plt.scatter(btc['date'][0:20],pred_dataframe['close'][0:20],c='#A3D1D1',label='預測收盤')
    plt.plot(btc['date'][0:20],btc['open'][0:20],'-x',c='#003060',label='實際開盤')
    plt.plot(btc['date'][0:20],btc['high'][0:20],'-x',c='#006000',label='實際最高')
    plt.plot(btc['date'][0:20],btc['low'][0:20],'-x',c='#CE0000',label='實際最低')
    plt.plot(btc['date'][0:20],btc['close'][0:20],'-x',c='#4F9D9D',label='實際收盤')
    colmap=np.array(['red','lime']) #紅漲綠跌
    for i in range(20):
        plt.axvline(x=pd.to_datetime(btc.loc[i,'date']),color=colmap[int(pred_dataframe.loc[i,'damage'])]
                    ,alpha=0.3,label='紅漲綠跌')
    plt.legend()
    plt.savefig('.\\file\\'+name+'Prediction.png')
    
    
    #視窗化
    load_page= tk.Toplevel()
    load_page.geometry('1200x800')                
    load_page.resizable(True,True)             
    load_page.title(name+'20天預測圖表')   
    load_page.configure(bg='#003D79')
    img = ImageTk.PhotoImage(Image.open('.\\file\\'+name+'Prediction.png').resize((1200,800)))
    label = tk.Label(load_page,image = img).pack()
    load_page.mainloop()
