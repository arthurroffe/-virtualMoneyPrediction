import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import ImageTk, Image
from ml import ml
import os
import datetime


def load(name):
    get_today = datetime.date.today()
    today = str(get_today)
    #連結資料庫
    conn = sql.connect('cash_'+today+'.db')
    print('連結資料庫..')
    c = conn.cursor()
    #讀取資料
    sql_select = 'select * from '+name
    c.execute(sql_select)
    select_all = c.fetchall()
    
    
    date = []
    dateok=[]
    openm = []
    high = []
    low = []
    close = []
    volume = []
    volume_ok = []
    marketCap = []
    test = []
    
    for i in select_all:
        date.append(i[0])
        openm.append(i[1])
        high.append(i[2])
        low.append(i[3])
        close.append(i[4])
        volume.append(i[5])
        marketCap.append(i[6])
    conn.close()
    
    BTC = {}
    data= pd.to_datetime(date)
    
    BTC['date'] = data
    BTC['open'] = openm
    BTC['high'] = high
    BTC['low'] = low
    BTC['close'] = close
    BTC['volume'] = volume
    BTC['marketCap'] = marketCap
        
    bct = pd.DataFrame(BTC,columns=('date','open','high','low','close','volume','marketCap'))
    
    #將資料製作成csv檔案
    out_file = '.\\file\\'+name+'.csv'
    bct.to_csv(out_file,encoding='utf-8')
    
    
    
    for i in volume:
        num = i/100000000
        num = f'{num:.1f}'
        num = float(num)
        volume_ok.append(num)
        
    #找最高的資料
    max_high = max(high)
    max_high_index = high.index(max_high)
    max_date = data[max_high_index]
    max_high_vo = volume_ok[max_high_index]
    #找最低的資料
    min_low = min(low)
    min_low_index = low.index(min_low)
    min_date = data[min_low_index]
    min_low_vo = volume_ok[min_low_index]
    #找最高成交量
    max_vo = max(volume_ok)
    max_vo_index = volume_ok.index(max_vo)
    max_vo_high = high[max_vo_index]
    
    
    
    
    #將資料製作成圖表
    plt.rcParams['font.family']='Microsoft JhengHei'
    plt.figure(dpi=300,figsize=(15,10),facecolor='slategrey')
    plt.rcParams['axes.facecolor'] = 'slategrey'
    plt.title(name)
    plt.xlabel('年份時間')
    plt.ylabel('金額(台幣)')
    plt.scatter(data,openm,alpha=0.8,s=volume_ok,c='blue',label='開盤')
    plt.axvline(x=pd.to_datetime(max_date),ymin=0,ymax=1000,color='red',alpha=0.8)
    plt.axhline(max_high, color= 'r')
    plt.text(x=pd.to_datetime(max_date),y=max_high,s=f'NT${max_high}')
    plt.scatter(data,high,alpha=0.5,s=volume_ok,c='red',label='最高')
    plt.scatter(data,low,alpha=0.5,s=volume_ok,c='yellow',label='最低')
    plt.axvline(x=pd.to_datetime(min_date),ymin=0,ymax=1000,color='greenyellow',alpha=0.8)
    plt.axhline(min_low, color= 'greenyellow')
    plt.text(x=pd.to_datetime(min_date),y=min_low,s=f'NT${min_low}')
    plt.scatter(data,close,alpha=0.5,s=volume_ok,c='lime',label='收盤')
    plt.legend()
    plt.savefig('.\\file\\'+name+'Trend.png')
    
    #呼叫視窗檢
    pred_name = name
    load_page= tk.Toplevel()
    load_page.geometry('1200x800')                
    load_page.resizable(True,True)             
    load_page.title(name+'圖表')   
    load_page.configure(bg='#003D79')
    img = ImageTk.PhotoImage(Image.open('.\\file\\'+name+'Trend.png').resize((1200,800)))
    label = tk.Label(load_page,image = img).pack()
    mlb = tk.Button(load_page,text='預測20天',command=ml(pred_name),bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10)).place(x=1000,y=50)
    
    load_page.mainloop()
