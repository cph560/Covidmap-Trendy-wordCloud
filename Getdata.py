
import requests
import time
import pymysql
import traceback
from datetime import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from Config import *

# Get data released by Tencent
def get_tencentdata():
    header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    url='https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,diseaseh5Shelf,provinceCompare,diseaseh5Shelf'

    res = requests.get(url, headers=header).json()

    data = res['data']
    disease=data["diseaseh5Shelf"]

    history = {}
    for i in data["chinaDayList"]:
        
        date=i['y']+'.'+i['date']
        tup=time.strptime(date,'%Y.%m.%d')
        date=time.strftime('%Y-%m-%d', tup)
        history[date]={'confirm': i['confirm'],'suspect': i['suspect'],
                       'heal': i['heal'], 'dead': i['dead']}
        
    for i in data["chinaDayAddList"]:
        
        date=i['y']+'.'+i['date']
        tup=time.strptime(date,'%Y.%m.%d')
        date=time.strftime('%Y-%m-%d', tup)
        if date not in history.keys():continue
        history[date].update({'confirm': i['confirm'],'suspect': i['suspect'],
                       'heal': i['heal'], 'dead': i['dead']})

    today_data=[]
    update_time=disease["lastUpdateTime"]
    province=disease["areaTree"][0]['children']
    
    for pro in province:
        
        pro_name=pro["name"]
        
        for city in pro['children']:
            city_name=city['name']
            
            confirm = city['total']['confirm']
            confirm_add = city['today']['confirm']
            heal = city['total']['heal']
            dead = city['total']['dead']
            today_data.append([update_time, pro_name, city_name, confirm,
                            confirm_add, heal, dead])

    return {'history':history, 'today_data':today_data}


    
def update_today(today_data:list):
    
    
    try:
        cursor=db.cursor()
        sql_query='insert into details (update_time, province, city, confirm,confirm_add, heal, dead) values (%s,%s,%s,%s,%s,%s,%s)'
        sql='select %s=(select update_time from details order by id desc limit 1)'
        cursor.execute(sql,today_data[0][0])
        res=cursor.fetchone()[0]
        if not res:
            print(f'{time.asctime()} Strat COVID DETAILS update')
            dele='delete from details'
            cursor.execute(dele)
            for i in today_data:
                cursor.execute(sql_query,i)
            db.commit()
            print(f'{time.asctime()} COVID DETAILS update finished')
        else:
            print(f'{time.asctime()} COVID DETAILS is already latest')
    
    except:
        traceback.print_exc()
    finally:
        if cursor:
            cursor.close()
            
def insert_history(history_data:dict):
    try:
        print(f'{time.asctime()} Start insert COVID DATA')
        cursor=db.cursor()
        sql='insert into history value (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        
        for i,j in history_data.items():
            
            cursor.execute(sql,[i,j.get('confirm'),j.get('confirm_add'),j.get('suspect'),j.get('suspect_add'),
            j.get('heal'),j.get('heal_add'),j.get('dead'),j.get('dead_add')])
        
        db.commit()
        print(f'{time.asctime()} Insert COVID DATA complete')
    except:
        traceback.print_exc()
    finally:
        if cursor:
            cursor.close()

def update_history(history_data:dict):
    try:
        print(f'{time.asctime()} Start update COVID HISTORY')
        cursor=db.cursor()
        sql = 'select confirm from history where ds=%s'
        sql_query='insert into history value (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for i,j in history_data.items():
            if not cursor.execute(sql,i):
                

                cursor.execute(sql_query,[i,j.get('confirm'),j.get('confirm_add'),j.get('suspect'),j.get('suspect_add'),
                j.get('heal'),j.get('heal_add'),j.get('dead'),j.get('dead_add')])
        db.commit()
        print(f'{time.asctime()} Update COVID HISTORY complete')
    except:
        traceback.print_exc()
    finally:
        if cursor:
            cursor.close()

def update_news():
    
    try:
        option = ChromeOptions()
        option.add_argument('--headless') 
        url="https://top.baidu.com/board?tab=realtime"
        Xpath='//*[@id="sanRoot"]/main/div[2]/div/div[2]/div/div[2]/a/div[1]'
        Xpath_hotindex='//*[@id="sanRoot"]/main/div[2]/div/div[2]/div/div[1]/div[2]'
        browser=Chrome(options=option)
        browser.get(url)

        res=browser.find_elements(by='xpath', value=Xpath)
        res_index=browser.find_elements(by='xpath', value=Xpath_hotindex)
        daily_news = [element.text for element in res]
        hotindex=[i.text for i in res_index]
        leng=len(daily_news)
        cursor=db.cursor()
        
        print(f'{time.asctime()} Start update Chinese Trendy news')
        dele='delete from hotsearch'
        cursor.execute(dele)
        sql='insert into hotsearch (dt,content,hotindex) value (%s,%s,%s)'
        today=datetime.today()
        date=today.strftime("%Y-%m-%d")
        for i in range(leng):
            cursor.execute(sql,[date,daily_news[i],hotindex[i]])
        db.commit()
        print(f'{time.asctime()} Update Chinese Trendy news finish')
    except:
        traceback.print_exc()
    finally:
        if cursor:
            cursor.close()

def update_google_news():
    try:
        option = ChromeOptions()
        option.add_argument('--headless') 
        url="https://trends.google.com/trends/trendingsearches/daily?geo=US"
        ele='title'
        clas='search-count-title'
        browser=Chrome(options=option)
        browser.get(url)
        sleep(2)
        res = browser.find_elements(By.CLASS_NAME, ele)
        res_index=browser.find_elements(By.CLASS_NAME, clas)

        daily_news = [element.text for element in res]
        hotindex=[]
        for i in res_index:
            ind=i.text
            hotindex.append(ind.replace('万+',''))

        leng=len(daily_news)
        cursor=db.cursor()

        print(f'{time.asctime()} Start update US Trendy news')
        dele='delete from googletrend;'
        cursor.execute(dele)
        sql='insert into googletrend (dt,content,hotindex) value (%s,%s,%s)'
        today=datetime.today()
        date=today.strftime("%Y-%m-%d")
        for i in range(leng):
            cursor.execute(sql,[date,daily_news[i],hotindex[i]])
        db.commit()
        print(f'{time.asctime()} Update US Trendy news finish')
    except:
        traceback.print_exc()
    finally:
        if cursor:
            cursor.close()


def insert_world_covid():

    option = ChromeOptions()
    
    url="https://www.worldometers.info/coronavirus/#main_table"
    xpath='//*[@id="main_table_countries_today"]/tbody[1]/tr'
    
    browser=Chrome()
    browser.get(url)
    res = browser.find_elements(by='xpath', value=xpath)
    

    world_covid = [[element.text] for element in res]
    return world_covid

if __name__ == '__main__':
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWORD, database=DATABASE)
    data=get_tencentdata()
    # insert_history(data['history'])
    update_history(data['history'])
    update_today(data['today_data'])
    update_news()
    update_google_news()

    #test
    # cursor=db.cursor()
    # query='select * from history '
    # cursor.execute(query)
    # res=cursor.fetchall()
    # print(res)
    db.close()


