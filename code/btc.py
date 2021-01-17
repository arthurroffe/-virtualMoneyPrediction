from selenium import webdriver
import time
import re
import requests
from bs4 import BeautifulSoup
import sqlite3 as sq
from PIL import Image
import os
import datetime


get_today = datetime.date.today()
today = str(get_today)
try:
    os.mkdir(r'.\icon')
except:
    print('資料夾已經建立')
#抓取網址資料
url_lis = []
for i in range(1,42):
    link = 'https://coinmarketcap.com/zh-tw/'+str(i)
    web = requests.get(link)
    soup = BeautifulSoup(web.text,'lxml')
    url = soup.find_all('td',{'style':'text-align:left'})
    url2 = soup.find_all('tbody')[0].find_all('tr')
    for j in range(len(url2)):
        try:
            #print(url2[i].find('a')['href'])
            url_lis.append(url2[j].find('a')['href'])
        except:
            print(f'{j}NO')

fail = []
for url in url_lis:
    try:
        #網址
        driver = webdriver.Chrome('chromedriver')
        driver.get('https://coinmarketcap.com'+url+'historical-data/')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="cmc-cookie-policy-banner"]/div[2]').click()
        time.sleep(2)
        #點選data
        js="var action=document.documentElement.scrollTop=200"
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[1]/span/button').click()
        time.sleep(2)
        try:
            for i in range(1,100):
                driver.find_element_by_xpath('//*[@id="tippy-13"]/div/div[1]/div/div/div[1]/div[1]/div/button[1]').click()
            driver.find_element_by_xpath('//*[@id="tippy-13"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[5]').click()
            driver.find_element_by_xpath('//*[@id="tippy-13"]/div/div[1]/div/div/div[2]/button[2]').click()
            time.sleep(5)
        except:
            try:
                print(f'{url} fix to 14')
                for i in range(1,100):
                    driver.find_element_by_xpath('//*[@id="tippy-14"]/div/div[1]/div/div/div[1]/div[1]/div/button[1]').click()
                driver.find_element_by_xpath('//*[@id="tippy-14"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[5]').click()
                driver.find_element_by_xpath('//*[@id="tippy-14"]/div/div[1]/div/div/div[2]/button[2]').click()
                time.sleep(5)
            except:
                try:
                    print(f'{url} fix to 18')
                    for i in range(1,100):
                        driver.find_element_by_xpath('//*[@id="tippy-18"]/div/div[1]/div/div/div[1]/div[1]/div/button[1]').click()
                    driver.find_element_by_xpath('//*[@id="tippy-18"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[5]').click()
                    driver.find_element_by_xpath('//*[@id="tippy-18"]/div/div[1]/div/div/div[2]/button[2]').click()
                    time.sleep(5)
                except:
                    try:
                        print(f'{url} fix to 15')
                        for i in range(1,100):
                            driver.find_element_by_xpath('//*[@id="tippy-15"]/div/div[1]/div/div/div[1]/div[1]/div/button[1]').click()
                        driver.find_element_by_xpath('//*[@id="tippy-15"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[5]').click()
                        driver.find_element_by_xpath('//*[@id="tippy-15"]/div/div[1]/div/div/div[2]/button[2]').click()
                        time.sleep(5)
                    except:
                        try:
                            print(f'{url} fix to 16')
                            for i in range(1,100):
                                driver.find_element_by_xpath('//*[@id="tippy-16"]/div/div[1]/div/div/div[1]/div[1]/div/button[1]').click()
                            driver.find_element_by_xpath('//*[@id="tippy-16"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[5]').click()
                            driver.find_element_by_xpath('//*[@id="tippy-16"]/div/div[1]/div/div/div[2]/button[2]').click()
                            time.sleep(5)
                        except:
                            try:
                                print(f'{url} fix to 17')
                                for i in range(1,100):
                                    driver.find_element_by_xpath('//*[@id="tippy-17"]/div/div[1]/div/div/div[1]/div[1]/div/button[1]').click()
                                driver.find_element_by_xpath('//*[@id="tippy-17"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[5]').click()
                                driver.find_element_by_xpath('//*[@id="tippy-17"]/div/div[1]/div/div/div[2]/button[2]').click()
                                time.sleep(5)
                            except:
                                try:
                                    print(f'{url} fix to 12')
                                    for i in range(1,100):
                                        driver.find_element_by_xpath('//*[@id="tippy-12"]/div/div[1]/div/div/div[1]/div[1]/div/button[1]').click()
                                    driver.find_element_by_xpath('//*[@id="tippy-12"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[5]').click()
                                    driver.find_element_by_xpath('//*[@id="tippy-12"]/div/div[1]/div/div/div[2]/button[2]').click()
                                    time.sleep(5)
                                except:
                                    print('faile')
                                    fail.append(url)
        
        #抓取資料
        soup = BeautifulSoup(driver.page_source,'lxml')
        data = soup.find_all('tr')
        name = soup.find('h2',{'class':'sc-1q9q90x-0 iYFMbU h1___3QSYG'}).text
        #抓取名稱和儲存icon
        name = re.sub('[.]','',name)
        name = re.sub(' ','_',name)
        name = re.sub('^[0]','O',name)
        name = re.sub('[|]','',name)
        print(name)
        
        img = soup.find('img')
        img_url = img['src']
        im = Image.open(requests.get(img_url, stream = True).raw)
        im.save('.\\icon\\'+name+'.png')
        print(f'儲存:{name}圖示')
        driver.quit()
        print('關閉自動瀏覽器')
        
       
        #整理資料
        dateok = []
        date = []
        openm = []
        openok = []
        high = []
        highok = []
        low = []
        lowok = []
        close =[]
        closeok =[]
        volume = []
        volumeok = []
        marketCap = []
        marketCapok = []
        for i in range(1,len(data)):
            data1 = data[i].find_all('td')
            date.append(data1[0].text)
            openm.append(data1[1].text)
            high.append(data1[2].text)
            low.append(data1[3].text)
            close.append(data1[4].text)
            volume.append(data1[5].text)
            marketCap.append(data1[6].text)  
            print(f'將資料變成串列中:{i/len(data)*100:.2f}%',end='\r')
        print('轉成串列完成')
        print('轉換日期..')
        for i in date:
            if 'Jan' in i:
                remou = re.sub('Jan','01',i)        
                dateok.append(remou)
            if 'Feb' in i:
                remou = re.sub('Feb','02',i)        
                dateok.append(remou)
            if 'Mar' in i:
                remou = re.sub('Mar','03',i)       
                dateok.append(remou)
            if 'Apr' in i:
                remou = re.sub('Apr','04',i)       
                dateok.append(remou)
            if 'May' in i:
                remou = re.sub('May','05',i)        
                dateok.append(remou)
            if 'Jun' in i:
                remou = re.sub('Jun','06',i)        
                dateok.append(remou)
            if 'Jul' in i:
                remou = re.sub('Jul','07',i)        
                dateok.append(remou)
            if 'Aug' in i:
                remou = re.sub('Aug','08',i)        
                dateok.append(remou)
            if 'Sep' in i:
                remou = re.sub('Sep','09',i)
                dateok.append(remou)
            if 'Oct' in i:
                remou = re.sub('Oct','10',i)
                dateok.append(remou)
            if 'Nov' in i:
                remou = re.sub('Nov','11',i)
                dateok.append(remou)
            if 'Dec' in i:
                remou = re.sub('Dec','12',i)
                dateok.append(remou)
        print('將不必要的逗號消除中')
        for i in openm:
            resu = re.sub(',','',i)
            resu = re.sub('\w+[$]','',resu)
            openok.append(resu)
        for i in high:
            resu = re.sub(',','',i)
            resu = re.sub('\w+[$]','',resu)
            highok.append(resu)
        print('將不必要的逗號消除中.')
        for i in low:
            resu = re.sub(',','',i)
            resu = re.sub('\w+[$]','',resu)
            lowok.append(resu)
        for i in close:
            resu = re.sub(',','',i)
            resu = re.sub('\w+[$]','',resu)
            closeok.append(resu)
        print('將不必要的逗號消除中..')
        for i in volume:
            resu = re.sub(',','',i)
            resu = re.sub('\w+[$]','',resu)
            volumeok.append(resu)
        for i in marketCap:
            resu = re.sub(',','',i)
            resu = re.sub('\w+[$]','',resu)
            marketCapok.append(resu)
        print('消除完成!')
        
        conn = sq.connect('cash_'+today+'.db')
        print('連結資料庫..')
        c = conn.cursor()
        try:
            sql_table = f'create table if not exists {name} (date CHAR(50)  not null,open int not null,high int not null,low int not null,close int not null,volume int not null,marktCap int not null);'
            c.execute(sql_table)
            conn.commit()
            print('創建資料表..')
        except:
            print(f'名稱錯誤:{name}')
            fail.append(url)
        for i in range(0,len(data)-1):
            sql_ins = 'insert into '+name+'(date,open,high,low,close,volume,marktcap)values('+'\''+dateok[i]+'\''+','+openok[i]+','+highok[i]+','+lowok[i]+','+closeok[i]+','+volumeok[i]+','+marketCapok[i]+');'
            c.execute(sql_ins)
            conn.commit()
            print(f'進度:{i/len(data)*100:.1f}%',end='\r')
        print('結束輸入..')
        
        conn.close()
        print('關閉資料庫')
        
        driver.quit()
        print('關閉自動瀏覽器')
    except:
        print(f'{url}需要重抓')
        fail.append(url)
print(fail)
