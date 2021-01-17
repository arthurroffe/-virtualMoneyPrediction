import sqlite3 as sql
from load import load
import tkinter as tk
import sklearn.neighbors._typedefs
import sklearn.neighbors._quad_tree
import sklearn.utils._weight_vector
import scipy.spatial.transform._rotation_groups
import os
import datetime

get_today = datetime.date.today()
today = str(get_today)
#連結資料庫
conn = sql.connect('cash_'+today+'.db')
c = conn.cursor()
sql_tableShow = 'SELECT name FROM sqlite_master WHERE type=\'table\' order by name'
c.execute(sql_tableShow)
table = []
for i in range(100):
    tables = c.fetchone()
    for j in tables:
        table.append(j)
        
os.mkdir(r'.\file')
def select_0():
    name = table[0]
    load(name)
def select_1():
    name = table[1]
    load(name)
def select_2():
    name = table[2]
    load(name)
def select_3():
    name = table[3]
    load(name)
def select_4():
    name = table[4]
    load(name)
def select_5():
    name = table[5]
    load(name)
def select_6():
    name = table[6]
    load(name)
def select_7():
    name = table[7]
    load(name)
def select_8():
    name = table[8]
    load(name)
def select_9():
    name = table[9]
    load(name)
def select_10():
    name = table[10]
    load(name)
def select_11():
    name = table[11]
    load(name)
def select_12():
    name = table[12]
    load(name)
def select_13():
    name = table[13]
    load(name)
def select_14():
    name = table[14]
    load(name)
def select_15():
    name = table[15]
    load(name)
def select_16():
    name = table[16]
    load(name)
def select_17():
    name = table[17]
    load(name)
def select_18():
    name = table[18]
    load(name)
def select_19():
    name = table[19]
    load(name)
def select_20():
    name = table[20]
    load(name)
def select_21():
    name = table[21]
    load(name)
def select_22():
    name = table[22]
    load(name)
def select_23():
    name = table[23]
    load(name)
def select_24():
    name = table[24]
    load(name)
def select_25():
    name = table[25]
    load(name)
def select_26():
    name = table[26]
    load(name)
def select_27():
    name = table[27]
    load(name)
def select_28():
    name = table[28]
    load(name)
def select_29():
    name = table[29]
    load(name)
def select_30():
    name = table[30]
    load(name)
def select_31():
    name = table[31]
    load(name)
def select_32():
    name = table[32]
    load(name)
def select_33():
    name = table[33]
    load(name)
def select_34():
    name = table[34]
    load(name)
def select_35():
    name = table[35]
    load(name)
def select_36():
    name = table[36]
    load(name)
def select_37():
    name = table[37]
    load(name)
def select_38():
    name = table[38]
    load(name)
def select_39():
    name = table[39]
    load(name)
def select_40():
    name = table[40]
    load(name)
def select_41():
    name = table[41]
    load(name)
def select_42():
    name = table[42]
    load(name)
def select_43():
    name = table[43]
    load(name)
def select_44():
    name = table[44]
    load(name)
def select_45():
    name = table[45]
    load(name)
def select_46():
    name = table[46]
    load(name)
def select_47():
    name = table[47]
    load(name)
def select_48():
    name = table[48]
    load(name)
def select_49():
    name = table[49]
    load(name)
def select_50():
    name = table[50]
    load(name)
def select_51():
    name = table[51]
    load(name)
def select_52():
    name = table[52]
    load(name)
def select_53():
    name = table[53]
    load(name)
def select_54():
    name = table[54]
    load(name)
def select_55():
    name = table[55]
    load(name)
def select_56():
    name = table[56]
    load(name)
def select_57():
    name = table[57]
    load(name)
def select_58():
    name = table[58]
    load(name)
def select_59():
    name = table[59]
    load(name)
def select_60():
    name = table[60]
    load(name)
def select_61():
    name = table[61]
    load(name)
def select_62():
    name = table[62]
    load(name)
def select_63():
    name = table[63]
    load(name)
def select_64():
    name = table[64]
    load(name)
def select_65():
    name = table[65]
    load(name)
def select_66():
    name = table[66]
    load(name)
def select_67():
    name = table[67]
    load(name)
def select_68():
    name = table[68]
    load(name)
def select_69():
    name = table[69]
    load(name)
def select_70():
    name = table[70]
    load(name)
def select_71():
    name = table[71]
    load(name)
def select_72():
    name = table[72]
    load(name)
def select_73():
    name = table[73]
    load(name)
def select_74():
    name = table[74]
    load(name)
def select_75():
    name = table[75]
    load(name)
def select_76():
    name = table[76]
    load(name)
def select_77():
    name = table[77]
    load(name)
def select_78():
    name = table[78]
    load(name)
def select_79():
    name = table[79]
    load(name)
def select_80():
    name = table[80]
    load(name)
def select_81():
    name = table[81]
    load(name)
def select_82():
    name = table[82]
    load(name)
def select_83():
    name = table[83]
    load(name)
def select_84():
    name = table[84]
    load(name)
def select_85():
    name = table[85]
    load(name)
def select_86():
    name = table[86]
    load(name)
def select_87():
    name = table[87]
    load(name)
def select_88():
    name = table[88]
    load(name)
def select_89():
    name = table[89]
    load(name)
def select_90():
    name = table[90]
    load(name)
def select_91():
    name = table[91]
    load(name)
def select_92():
    name = table[92]
    load(name)
def select_93():
    name = table[93]
    load(name)
def select_94():
    name = table[94]
    load(name)
def select_95():
    name = table[95]
    load(name)
def select_96():
    name = table[96]
    load(name)
def select_97():
    name = table[97]
    load(name)
def select_98():
    name = table[98]
    load(name)
def select_99():
    name = table[99]
    load(name)
def page_1():
    page1 = tk.Toplevel()
    page1.geometry('800x800')                
    page1.resizable(True,True)             
    page1.title('虛擬貨幣page1')   
    page1.configure(bg='#003D79')
    
    label = tk.Label(page1,text='請選擇想看的虛擬貨幣',fg='white',bg='#003D79',
                     font=('Microsoft JhengHei',20))
    label.pack()
    imgBtn20 = tk.PhotoImage(file=f'{table[20]}.png') 
    small_logo20 = imgBtn20.subsample(2,2)
    b20 = tk.Button(page1,text=f'{table[20]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10),image=small_logo20,compound='left'
                   ,command=select_20,anchor="w")
    b20.image=small_logo20
    b20.place(x=200,y=100)
    
    b21 = tk.Button(page1,text=f'{table[21]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_21,anchor="w")
    imgBtn21 = tk.PhotoImage(file=f'{table[21]}.png').subsample(2,2)
    b21.config(image=imgBtn21,compound='left')
    b21.image=imgBtn21
    b21.place(x=200,y=150)
    b22 = tk.Button(page1,text=f'{table[22]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_22,anchor="w")
    imgBtn22 = tk.PhotoImage(file=f'{table[22]}.png').subsample(2,2)
    b22.config(image=imgBtn22,compound='left')
    b22.image=imgBtn22
    b22.place(x=200,y=200)
    b23 = tk.Button(page1,text=f'{table[23]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_23,anchor="w")
    imgBtn23 = tk.PhotoImage(file=f'{table[23]}.png').subsample(2,2)
    b23.config(image=imgBtn23,compound='left')
    b23.image=imgBtn23
    b23.place(x=200,y=250)
    b24 = tk.Button(page1,text=f'{table[24]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_24,anchor="w")
    imgBtn24 = tk.PhotoImage(file=f'{table[24]}.png').subsample(2,2)
    b24.config(image=imgBtn24,compound='left')
    b24.image=imgBtn24
    b24.place(x=200,y=300)
    b25 = tk.Button(page1,text=f'{table[25]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_25,anchor="w")
    imgBtn25 = tk.PhotoImage(file=f'{table[25]}.png').subsample(2,2)
    b25.config(image=imgBtn25,compound='left')
    b25.image=imgBtn25
    b25.place(x=450,y=100)
    b26 = tk.Button(page1,text=f'{table[26]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_26,anchor="w")
    imgBtn26 = tk.PhotoImage(file=f'{table[26]}.png').subsample(2,2)
    b26.config(image=imgBtn26,compound='left')
    b26.image=imgBtn26
    b26.place(x=450,y=150)
    b27 = tk.Button(page1,text=f'{table[27]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_27,anchor="w")
    imgBtn27 = tk.PhotoImage(file=f'{table[27]}.png').subsample(2,2)
    b27.config(image=imgBtn27,compound='left')
    b27.image=imgBtn27
    b27.place(x=450,y=200)
    b28 = tk.Button(page1,text=f'{table[28]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_28,anchor="w")
    imgBtn28 = tk.PhotoImage(file=f'{table[28]}.png').subsample(2,2)
    b28.config(image=imgBtn28,compound='left')
    b28.image=imgBtn28
    b28.place(x=450,y=250)
    b29 = tk.Button(page1,text=f'{table[29]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_29,anchor="w")
    imgBtn29 = tk.PhotoImage(file=f'{table[29]}.png').subsample(2,2)
    b29.config(image=imgBtn29,compound='left')
    b29.image=imgBtn29
    b29.place(x=450,y=300)
    b30 = tk.Button(page1,text=f'{table[30]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_30,anchor="w")
    imgBtn30 = tk.PhotoImage(file=f'{table[30]}.png').subsample(2,2)
    b30.config(image=imgBtn30,compound='left')
    b30.image=imgBtn30
    b30.place(x=200,y=350)
    b31 = tk.Button(page1,text=f'{table[31]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_31,anchor="w")
    imgBtn31 = tk.PhotoImage(file=f'{table[31]}.png').subsample(2,2)
    b31.config(image=imgBtn31,compound='left')
    b31.image=imgBtn31
    b31.place(x=200,y=400)
    b32 = tk.Button(page1,text=f'{table[32]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_32,anchor="w")
    imgBtn32 = tk.PhotoImage(file=f'{table[32]}.png').subsample(2,2)
    b32.config(image=imgBtn32,compound='left')
    b32.image=imgBtn32
    b32.place(x=200,y=450)
    b33 = tk.Button(page1,text=f'{table[33]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_33,anchor="w")
    imgBtn33 = tk.PhotoImage(file=f'{table[33]}.png').subsample(2,2)
    b33.config(image=imgBtn33,compound='left')
    b33.image=imgBtn33
    b33.place(x=200,y=500)
    b34 = tk.Button(page1,text=f'{table[34]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_34,anchor="w")
    imgBtn34 = tk.PhotoImage(file=f'{table[34]}.png').subsample(2,2)
    b34.config(image=imgBtn34,compound='left')
    b34.image=imgBtn34
    b34.place(x=200,y=550)
    b35 = tk.Button(page1,text=f'{table[35]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_35,anchor="w")
    imgBtn35 = tk.PhotoImage(file=f'{table[35]}.png').subsample(2,2)
    b35.config(image=imgBtn35,compound='left')
    b35.image=imgBtn35
    b35.place(x=450,y=350)
    b36 = tk.Button(page1,text=f'{table[36]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_36,anchor="w")
    imgBtn36 = tk.PhotoImage(file=f'{table[36]}.png').subsample(2,2)
    b36.config(image=imgBtn36,compound='left')
    b36.image=imgBtn36
    b36.place(x=450,y=400)
    b37 = tk.Button(page1,text=f'{table[37]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_37,anchor="w")
    imgBtn37 = tk.PhotoImage(file=f'{table[37]}.png').subsample(2,2)
    b37.config(image=imgBtn37,compound='left')
    b37.image=imgBtn37
    b37.place(x=450,y=450)
    b38 = tk.Button(page1,text=f'{table[38]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_38,anchor="w")
    imgBtn38 = tk.PhotoImage(file=f'{table[38]}.png').subsample(2,2)
    b38.config(image=imgBtn38,compound='left')
    b38.image=imgBtn38
    b38.place(x=450,y=500)
    b39 = tk.Button(page1,text=f'{table[39]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_39,anchor="w")
    imgBtn39 = tk.PhotoImage(file=f'{table[39]}.png').subsample(2,2)
    b39.config(image=imgBtn39,compound='left')
    b39.image=imgBtn39
    b39.place(x=450,y=550)
    next_page = tk.Button(page1,text='下一頁',bg='#46A3FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=page_2).place(x=500,y=700)

def page_2():
    page_2 = tk.Toplevel()
    page_2.geometry('800x800')                
    page_2.resizable(True,True)             
    page_2.title('虛擬貨幣page_2')   
    page_2.configure(bg='#003D79')
    
    label = tk.Label(page_2,text='請選擇想看的虛擬貨幣',fg='white',bg='#003D79',
                     font=('Microsoft JhengHei',20))
    label.pack()
    
    b40 = tk.Button(page_2,text=f'{table[40]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_40,anchor="w")
    imgBtn40 = tk.PhotoImage(file=f'{table[40]}.png').subsample(2,2)
    b40.config(image=imgBtn40,compound='left')
    b40.image=imgBtn40
    b40.place(x=200,y=100)
    b41 = tk.Button(page_2,text=f'{table[41]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_41,anchor="w")
    imgBtn41 = tk.PhotoImage(file=f'{table[41]}.png').subsample(2,2)
    b41.config(image=imgBtn41,compound='left')
    b41.image=imgBtn41
    b41.place(x=200,y=150)
    b42 = tk.Button(page_2,text=f'{table[42]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_42,anchor="w")
    imgBtn42 = tk.PhotoImage(file=f'{table[42]}.png').subsample(2,2)
    b42.config(image=imgBtn42,compound='left')
    b42.image=imgBtn42
    b42.place(x=200,y=200)
    b43 = tk.Button(page_2,text=f'{table[43]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_43,anchor="w")
    imgBtn43 = tk.PhotoImage(file=f'{table[43]}.png').subsample(2,2)
    b43.config(image=imgBtn43,compound='left')
    b43.image=imgBtn43
    b43.place(x=200,y=250)
    b44 = tk.Button(page_2,text=f'{table[44]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_44,anchor="w")
    imgBtn44 = tk.PhotoImage(file=f'{table[44]}.png').subsample(2,2)
    b44.config(image=imgBtn44,compound='left')
    b44.image=imgBtn44
    b44.place(x=200,y=300)
    b45 = tk.Button(page_2,text=f'{table[45]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_45,anchor="w")
    imgBtn45 = tk.PhotoImage(file=f'{table[45]}.png').subsample(2,2)
    b45.config(image=imgBtn45,compound='left')
    b45.image=imgBtn45
    b45.place(x=200,y=350)
    b46 = tk.Button(page_2,text=f'{table[46]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_46,anchor="w")
    imgBtn46 = tk.PhotoImage(file=f'{table[46]}.png').subsample(2,2)
    b46.config(image=imgBtn46,compound='left')
    b46.image=imgBtn46
    b46.place(x=200,y=400)
    b47 = tk.Button(page_2,text=f'{table[47]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_47,anchor="w")
    imgBtn47 = tk.PhotoImage(file=f'{table[47]}.png').subsample(2,2)
    b47.config(image=imgBtn47,compound='left')
    b47.image=imgBtn47
    b47.place(x=200,y=450)
    b48 = tk.Button(page_2,text=f'{table[48]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_48,anchor="w")
    imgBtn48 = tk.PhotoImage(file=f'{table[48]}.png').subsample(2,2)
    b48.config(image=imgBtn48,compound='left')
    b48.image=imgBtn48
    b48.place(x=200,y=500)
    b49 = tk.Button(page_2,text=f'{table[49]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_49,anchor="w")
    imgBtn49 = tk.PhotoImage(file=f'{table[49]}.png').subsample(2,2)
    b49.config(image=imgBtn49,compound='left')
    b49.image=imgBtn49
    b49.place(x=200,y=550)
    b50 = tk.Button(page_2,text=f'{table[50]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_50,anchor="w")
    imgBtn50 = tk.PhotoImage(file=f'{table[50]}.png').subsample(2,2)
    b50.config(image=imgBtn50,compound='left')
    b50.image=imgBtn50
    b50.place(x=450,y=100)
    b51 = tk.Button(page_2,text=f'{table[51]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_51,anchor="w")
    imgBtn51 = tk.PhotoImage(file=f'{table[51]}.png').subsample(2,2)
    b51.config(image=imgBtn51,compound='left')
    b51.image=imgBtn51
    b51.place(x=450,y=150)
    b52 = tk.Button(page_2,text=f'{table[52]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_52,anchor="w")
    imgBtn52 = tk.PhotoImage(file=f'{table[52]}.png').subsample(2,2)
    b52.config(image=imgBtn52,compound='left')
    b52.image=imgBtn52
    b52.place(x=450,y=200)
    b53 = tk.Button(page_2,text=f'{table[53]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_53,anchor="w")
    imgBtn53 = tk.PhotoImage(file=f'{table[53]}.png').subsample(2,2)
    b53.config(image=imgBtn53,compound='left')
    b53.image=imgBtn53
    b53.place(x=450,y=250)
    b54 = tk.Button(page_2,text=f'{table[54]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_54,anchor="w")
    imgBtn54 = tk.PhotoImage(file=f'{table[54]}.png').subsample(2,2)
    b54.config(image=imgBtn54,compound='left')
    b54.image=imgBtn54
    b54.place(x=450,y=300)
    b55 = tk.Button(page_2,text=f'{table[55]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_55,anchor="w")
    imgBtn55 = tk.PhotoImage(file=f'{table[55]}.png').subsample(2,2)
    b55.config(image=imgBtn55,compound='left')
    b55.image=imgBtn55
    b55.place(x=450,y=350)
    b56 = tk.Button(page_2,text=f'{table[56]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_56,anchor="w")
    imgBtn56 = tk.PhotoImage(file=f'{table[56]}.png').subsample(2,2)
    b56.config(image=imgBtn56,compound='left')
    b56.image=imgBtn56
    b56.place(x=450,y=400)
    b57 = tk.Button(page_2,text=f'{table[57]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_57,anchor="w")
    imgBtn57 = tk.PhotoImage(file=f'{table[57]}.png').subsample(2,2)
    b57.config(image=imgBtn57,compound='left')
    b57.image=imgBtn57
    b57.place(x=450,y=450)
    b58 = tk.Button(page_2,text=f'{table[58]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_58,anchor="w")
    imgBtn58 = tk.PhotoImage(file=f'{table[58]}.png').subsample(2,2)
    b58.config(image=imgBtn58,compound='left')
    b58.image=imgBtn58
    b58.place(x=450,y=500)
    b59 = tk.Button(page_2,text=f'{table[59]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_59,anchor="w")
    imgBtn59 = tk.PhotoImage(file=f'{table[59]}.png').subsample(2,2)
    b59.config(image=imgBtn59,compound='left')
    b59.image=imgBtn59
    b59.place(x=450,y=550)
    next_page = tk.Button(page_2,text='下一頁',bg='#46A3FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=page_3).place(x=500,y=700) 
def page_3():
    page_3 = tk.Toplevel()
    page_3.geometry('800x800')                
    page_3.resizable(True,True)             
    page_3.title('虛擬貨幣page_3')   
    page_3.configure(bg='#003D79')
    
    label = tk.Label(page_3,text='請選擇想看的虛擬貨幣',fg='white',bg='#003D79',
                     font=('Microsoft JhengHei',20))
    label.pack()
    
    b0 = tk.Button(page_3,text=f'{table[60]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_60,anchor="w")
    imgBtn0 = tk.PhotoImage(file=f'{table[60]}.png').subsample(2,2)
    b0.config(image=imgBtn0,compound='left')
    b0.image=imgBtn0
    b0.place(x=200,y=100)
    b1 = tk.Button(page_3,text=f'{table[61]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_61,anchor="w")
    imgBtn1 = tk.PhotoImage(file=f'{table[61]}.png').subsample(2,2)
    b1.config(image=imgBtn1,compound='left')
    b1.image=imgBtn1
    b1.place(x=200,y=150)
    b2 = tk.Button(page_3,text=f'{table[62]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_62,anchor="w")
    imgBtn2 = tk.PhotoImage(file=f'{table[62]}.png').subsample(2,2)
    b2.config(image=imgBtn2,compound='left')
    b2.image=imgBtn2
    b2.place(x=200,y=200)
    b3 = tk.Button(page_3,text=f'{table[63]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_63,anchor="w")
    imgBtn3 = tk.PhotoImage(file=f'{table[63]}.png').subsample(2,2)
    b3.config(image=imgBtn3,compound='left')
    b3.image=imgBtn3
    b3.place(x=200,y=250)
    b4 = tk.Button(page_3,text=f'{table[64]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_64,anchor="w")
    imgBtn4 = tk.PhotoImage(file=f'{table[64]}.png').subsample(2,2)
    b4.config(image=imgBtn4,compound='left')
    b4.image=imgBtn4
    b4.place(x=200,y=300)
    b5 = tk.Button(page_3,text=f'{table[65]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_65,anchor="w")
    imgBtn5 = tk.PhotoImage(file=f'{table[65]}.png').subsample(2,2)
    b5.config(image=imgBtn5,compound='left')
    b5.image=imgBtn5
    b5.place(x=200,y=350)
    b6 = tk.Button(page_3,text=f'{table[66]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_66,anchor="w")
    imgBtn6 = tk.PhotoImage(file=f'{table[66]}.png').subsample(2,2)
    b6.config(image=imgBtn6,compound='left')
    b6.image=imgBtn6
    b6.place(x=200,y=400)
    b7 = tk.Button(page_3,text=f'{table[67]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_67,anchor="w")
    imgBtn7 = tk.PhotoImage(file=f'{table[67]}.png').subsample(2,2)
    b7.config(image=imgBtn7,compound='left')
    b7.image=imgBtn7
    b7.place(x=200,y=450)
    b8 = tk.Button(page_3,text=f'{table[68]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_68,anchor="w")
    imgBtn8 = tk.PhotoImage(file=f'{table[68]}.png').subsample(2,2)
    b8.config(image=imgBtn8,compound='left')
    b8.image=imgBtn8
    b8.place(x=200,y=500)
    b9 = tk.Button(page_3,text=f'{table[69]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_69,anchor="w")
    imgBtn9 = tk.PhotoImage(file=f'{table[69]}.png').subsample(2,2)
    b9.config(image=imgBtn9,compound='left')
    b9.image=imgBtn9
    b9.place(x=200,y=550)
    b10 = tk.Button(page_3,text=f'{table[70]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_70,anchor="w")
    imgBtn10 = tk.PhotoImage(file=f'{table[70]}.png').subsample(2,2)
    b10.config(image=imgBtn10,compound='left')
    b10.image=imgBtn10
    b10.place(x=450,y=100)
    b11 = tk.Button(page_3,text=f'{table[71]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_71,anchor="w")
    imgBtn11 = tk.PhotoImage(file=f'{table[71]}.png').subsample(2,2)
    b11.config(image=imgBtn11,compound='left')
    b11.image=imgBtn11
    b11.place(x=450,y=150)
    b12 = tk.Button(page_3,text=f'{table[72]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_72,anchor="w")
    imgBtn12 = tk.PhotoImage(file=f'{table[72]}.png').subsample(2,2)
    b12.config(image=imgBtn12,compound='left')
    b12.image=imgBtn12
    b12.place(x=450,y=200)
    b13 = tk.Button(page_3,text=f'{table[73]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_73,anchor="w")
    imgBtn13 = tk.PhotoImage(file=f'{table[73]}.png').subsample(2,2)
    b13.config(image=imgBtn13,compound='left')
    b13.image=imgBtn13
    b13.place(x=450,y=250)
    b14 = tk.Button(page_3,text=f'{table[74]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_74,anchor="w")
    imgBtn14 = tk.PhotoImage(file=f'{table[74]}.png').subsample(2,2)
    b14.config(image=imgBtn14,compound='left')
    b14.image=imgBtn14
    b14.place(x=450,y=300)
    b15 = tk.Button(page_3,text=f'{table[75]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_75,anchor="w")
    imgBtn15 = tk.PhotoImage(file=f'{table[75]}.png').subsample(2,2)
    b15.config(image=imgBtn15,compound='left')
    b15.image=imgBtn15
    b15.place(x=450,y=350)
    b16 = tk.Button(page_3,text=f'{table[76]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_76,anchor="w")
    imgBtn16 = tk.PhotoImage(file=f'{table[76]}.png').subsample(2,2)
    b16.config(image=imgBtn16,compound='left')
    b16.image=imgBtn16
    b16.place(x=450,y=400)
    b17 = tk.Button(page_3,text=f'{table[77]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_77,anchor="w")
    imgBtn17 = tk.PhotoImage(file=f'{table[77]}.png').subsample(2,2)
    b17.config(image=imgBtn17,compound='left')
    b17.image=imgBtn17
    b17.place(x=450,y=450)
    b18 = tk.Button(page_3,text=f'{table[78]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_78,anchor="w")
    imgBtn18 = tk.PhotoImage(file=f'{table[78]}.png').subsample(2,2)
    b18.config(image=imgBtn18,compound='left')
    b18.image=imgBtn18
    b18.place(x=450,y=500)
    b19 = tk.Button(page_3,text=f'{table[79]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_79,anchor="w")
    imgBtn19 = tk.PhotoImage(file=f'{table[79]}.png').subsample(2,2)
    b19.config(image=imgBtn19,compound='left')
    b19.image=imgBtn19
    b19.place(x=450,y=550)
    next_page = tk.Button(page_3,text='下一頁',bg='#46A3FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=page_4).place(x=500,y=700) 
def page_4():
    page_4 = tk.Toplevel()
    page_4.geometry('800x800')                
    page_4.resizable(True,True)             
    page_4.title('虛擬貨幣page_4')   
    page_4.configure(bg='#003D79')
    
    label = tk.Label(page_4,text='請選擇想看的虛擬貨幣',fg='white',bg='#003D79',
                     font=('Microsoft JhengHei',20))
    label.pack()
    
    b0 = tk.Button(page_4,text=f'{table[80]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_80,anchor="w")
    imgBtn0 = tk.PhotoImage(file=f'{table[80]}.png').subsample(2,2)
    b0.config(image=imgBtn0,compound='left')
    b0.image=imgBtn0
    b0.place(x=200,y=100)
    b1 = tk.Button(page_4,text=f'{table[81]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_81,anchor="w")
    imgBtn1 = tk.PhotoImage(file=f'{table[81]}.png').subsample(2,2)
    b1.config(image=imgBtn1,compound='left')
    b1.image=imgBtn1
    b1.place(x=200,y=150)
    b2 = tk.Button(page_4,text=f'{table[82]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_82,anchor="w")
    imgBtn2 = tk.PhotoImage(file=f'{table[82]}.png').subsample(2,2)
    b2.config(image=imgBtn2,compound='left')
    b2.image=imgBtn2
    b2.place(x=200,y=200)
    b3 = tk.Button(page_4,text=f'{table[83]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_83,anchor="w")
    imgBtn3 = tk.PhotoImage(file=f'{table[83]}.png').subsample(2,2)
    b3.config(image=imgBtn3,compound='left')
    b3.image=imgBtn3
    b3.place(x=200,y=250)
    b4 = tk.Button(page_4,text=f'{table[84]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_84,anchor="w")
    imgBtn4 = tk.PhotoImage(file=f'{table[84]}.png').subsample(2,2)
    b4.config(image=imgBtn4,compound='left')
    b4.image=imgBtn4
    b4.place(x=200,y=300)
    b5 = tk.Button(page_4,text=f'{table[85]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_85,anchor="w")
    imgBtn5 = tk.PhotoImage(file=f'{table[85]}.png').subsample(2,2)
    b5.config(image=imgBtn5,compound='left')
    b5.image=imgBtn5
    b5.place(x=200,y=350)
    b6 = tk.Button(page_4,text=f'{table[86]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_86,anchor="w")
    imgBtn6 = tk.PhotoImage(file=f'{table[86]}.png').subsample(2,2)
    b6.config(image=imgBtn6,compound='left')
    b6.image=imgBtn6
    b6.place(x=200,y=400)
    b7 = tk.Button(page_4,text=f'{table[87]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_87,anchor="w")
    imgBtn7 = tk.PhotoImage(file=f'{table[87]}.png').subsample(2,2)
    b7.config(image=imgBtn7,compound='left')
    b7.image=imgBtn7
    b7.place(x=200,y=450)
    b8 = tk.Button(page_4,text=f'{table[88]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_88,anchor="w")
    imgBtn8 = tk.PhotoImage(file=f'{table[88]}.png').subsample(2,2)
    b8.config(image=imgBtn8,compound='left')
    b8.image=imgBtn8
    b8.place(x=200,y=500)
    b9 = tk.Button(page_4,text=f'{table[89]}',width=160,bg='#C6E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_89,anchor="w")
    imgBtn9 = tk.PhotoImage(file=f'{table[89]}.png').subsample(2,2)
    b9.config(image=imgBtn9,compound='left')
    b9.image=imgBtn9
    b9.place(x=200,y=550)
    b10 = tk.Button(page_4,text=f'{table[90]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_90,anchor="w")
    imgBtn10 = tk.PhotoImage(file=f'{table[90]}.png').subsample(2,2)
    b10.config(image=imgBtn10,compound='left')
    b10.image=imgBtn10
    b10.place(x=450,y=100)
    b11 = tk.Button(page_4,text=f'{table[91]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_91,anchor="w")
    imgBtn11 = tk.PhotoImage(file=f'{table[91]}.png').subsample(2,2)
    b11.config(image=imgBtn11,compound='left')
    b11.image=imgBtn11
    b11.place(x=450,y=150)
    b12 = tk.Button(page_4,text=f'{table[92]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_92,anchor="w")
    imgBtn12 = tk.PhotoImage(file=f'{table[92]}.png').subsample(2,2)
    b12.config(image=imgBtn12,compound='left')
    b12.image=imgBtn12
    b12.place(x=450,y=200)
    b13 = tk.Button(page_4,text=f'{table[93]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_93,anchor="w")
    imgBtn13 = tk.PhotoImage(file=f'{table[93]}.png').subsample(2,2)
    b13.config(image=imgBtn13,compound='left')
    b13.image=imgBtn13
    b13.place(x=450,y=250)
    b14 = tk.Button(page_4,text=f'{table[94]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_94,anchor="w")
    imgBtn14 = tk.PhotoImage(file=f'{table[94]}.png').subsample(2,2)
    b14.config(image=imgBtn14,compound='left')
    b14.image=imgBtn14
    b14.place(x=450,y=300)
    b15 = tk.Button(page_4,text=f'{table[95]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_95,anchor="w")
    imgBtn15 = tk.PhotoImage(file=f'{table[95]}.png').subsample(2,2)
    b15.config(image=imgBtn15,compound='left')
    b15.image=imgBtn15
    b15.place(x=450,y=350)
    b16 = tk.Button(page_4,text=f'{table[96]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_96,anchor="w")
    imgBtn16 = tk.PhotoImage(file=f'{table[96]}.png').subsample(2,2)
    b16.config(image=imgBtn16,compound='left')
    b16.image=imgBtn16
    b16.place(x=450,y=400)
    b17 = tk.Button(page_4,text=f'{table[97]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_97,anchor="w")
    imgBtn17 = tk.PhotoImage(file=f'{table[97]}.png').subsample(2,2)
    b17.config(image=imgBtn17,compound='left')
    b17.image=imgBtn17
    b17.place(x=450,y=450)
    b18 = tk.Button(page_4,text=f'{table[98]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_98,anchor="w")
    imgBtn18 = tk.PhotoImage(file=f'{table[98]}.png').subsample(2,2)
    b18.config(image=imgBtn18,compound='left')
    b18.image=imgBtn18
    b18.place(x=450,y=500)
    b19 = tk.Button(page_4,text=f'{table[99]}',width=160,bg='#C4E1FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=select_99,anchor="w")
    imgBtn19 = tk.PhotoImage(file=f'{table[99]}.png').subsample(2,2)
    b19.config(image=imgBtn19,compound='left')
    b19.image=imgBtn19
    b19.place(x=450,y=550)
    next_page = tk.Button(page_4,text='上一頁',bg='#46A3FF',relief='flat',
                   font=('Microsoft JhengHei',10)
                   ,command=page_3).place(x=500,y=700)
    

print('請選擇想看的虛擬貨幣')
win= tk.Tk()         
win.geometry('800x800')                
win.resizable(True,True)             
win.title('虛擬貨幣')   
win.configure(bg='#003D79')

label = tk.Label(win,text='請選擇想看的虛擬貨幣',fg='white',bg='#003D79',
                 font=('Microsoft JhengHei',20))
label.pack()
imgBtn0 = tk.PhotoImage(file=f'{table[0]}.png') 
small_logo0 = imgBtn0.subsample(2,2)
b0 = tk.Button(win,text=f'{table[0]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo0,compound='left'
               ,command=select_0,anchor="w").place(x=200,y=100)
imgBtn1 = tk.PhotoImage(file=f'{table[1]}.png')
small_logo1 = imgBtn1.subsample(2, 2)
b1 = tk.Button(win,text=f'{table[1]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo1,compound='left'
               ,command=select_1,anchor="w").place(x=200,y=150)

imgBtn2 = tk.PhotoImage(file=f'{table[2]}.png')
small_logo2 = imgBtn2.subsample(2, 2)
b2 = tk.Button(win,text=f'{table[2]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo2,compound='left'
               ,command=select_2,anchor="w").place(x=200,y=200)

imgBtn3 = tk.PhotoImage(file=f'{table[3]}.png')
small_logo3 = imgBtn3.subsample(2, 2)
b3 = tk.Button(win,text=f'{table[3]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo3,compound='left'
               ,command=select_3,anchor="w").place(x=200,y=250)

imgBtn4 = tk.PhotoImage(file=f'{table[4]}.png')
small_logo4 = imgBtn4.subsample(2, 2)
b4 = tk.Button(win,text=f'{table[4]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo4,compound='left'
               ,command=select_4,anchor="w").place(x=200,y=300)

imgBtn5 = tk.PhotoImage(file=f'{table[5]}.png')
small_logo5 = imgBtn5.subsample(2, 2)
b5 = tk.Button(win,text=f'{table[5]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo5,compound='left'
               ,command=select_5,anchor="w").place(x=450,y=100)

imgBtn6 = tk.PhotoImage(file=f'{table[6]}.png')
small_logo6 = imgBtn6.subsample(2, 2)
b6 = tk.Button(win,text=f'{table[6]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo6,compound='left'
               ,command=select_6,anchor="w").place(x=450,y=150)
imgBtn7 = tk.PhotoImage(file=f'{table[7]}.png')
small_logo7 = imgBtn7.subsample(2, 2)
b7 = tk.Button(win,text=f'{table[7]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo7,compound='left'
               ,command=select_7,anchor="w").place(x=450,y=200)
imgBtn8 = tk.PhotoImage(file=f'{table[8]}.png')
small_logo8 = imgBtn8.subsample(2, 2)
b8 = tk.Button(win,text=f'{table[8]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',7),image=small_logo8,compound='left'
               ,command=select_8,anchor="w").place(x=450,y=250)
imgBtn9 = tk.PhotoImage(file=f'{table[9]}.png')
small_logo9 = imgBtn9.subsample(2, 2)
b9 = tk.Button(win,text=f'{table[9]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo9,compound='left'
               ,command=select_9,anchor="w").place(x=450,y=300)
imgBtn10 = tk.PhotoImage(file=f'{table[10]}.png')
small_logo10 = imgBtn10.subsample(2, 2)
b10 = tk.Button(win,text=f'{table[10]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo10,compound='left'
               ,command=select_10,anchor="w").place(x=200,y=350)
imgBtn11 = tk.PhotoImage(file=f'{table[11]}.png')
small_logo11 = imgBtn11.subsample(2, 2)
b11 = tk.Button(win,text=f'{table[11]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo11,compound='left'
               ,command=select_11,anchor="w").place(x=200,y=400)
imgBtn12 = tk.PhotoImage(file=f'{table[12]}.png')
small_logo12 = imgBtn12.subsample(2, 2)
b12 = tk.Button(win,text=f'{table[12]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo12,compound='left'
               ,command=select_12,anchor="w").place(x=200,y=450)
imgBtn13 = tk.PhotoImage(file=f'{table[13]}.png')
small_logo13 = imgBtn13.subsample(2, 2)
b13 = tk.Button(win,text=f'{table[13]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo13,compound='left'
               ,command=select_13,anchor="w").place(x=200,y=500)
imgBtn14 = tk.PhotoImage(file=f'{table[14]}.png')
small_logo14 = imgBtn14.subsample(2, 2)
b14 = tk.Button(win,text=f'{table[14]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo14,compound='left'
               ,command=select_14,anchor="w").place(x=200,y=550)
imgBtn15 = tk.PhotoImage(file=f'{table[15]}.png')
small_logo15 = imgBtn15.subsample(2, 2)
b15 = tk.Button(win,text=f'{table[15]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo15,compound='left'
               ,command=select_15,anchor="w").place(x=450,y=350)
imgBtn16 = tk.PhotoImage(file=f'{table[16]}.png')
small_logo16 = imgBtn16.subsample(2, 2)
b16 = tk.Button(win,text=f'{table[16]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo16,compound='left'
               ,command=select_16,anchor="w").place(x=450,y=400)
imgBtn17 = tk.PhotoImage(file=f'{table[17]}.png')
small_logo17 = imgBtn17.subsample(2, 2)
b17 = tk.Button(win,text=f'{table[17]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo17,compound='left'
               ,command=select_17,anchor="w").place(x=450,y=450)
imgBtn18 = tk.PhotoImage(file=f'{table[18]}.png')
small_logo18 = imgBtn18.subsample(2, 2)
b18 = tk.Button(win,text=f'{table[18]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo18,compound='left'
               ,command=select_18,anchor="w").place(x=450,y=500)
imgBtn19 = tk.PhotoImage(file=f'{table[19]}.png')
small_logo19 = imgBtn19.subsample(2, 2)
b19 = tk.Button(win,text=f'{table[19]}',width=160,bg='#C4E1FF',relief='flat',
               font=('Microsoft JhengHei',10),image=small_logo19,compound='left'
               ,command=select_19,anchor="w").place(x=450,y=550)

next_page = tk.Button(win,text='下一頁',bg='#46A3FF',relief='flat',
               font=('Microsoft JhengHei',10)
               ,command=page_1).place(x=500,y=700)

win.mainloop()



