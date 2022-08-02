from calendar import day_abbr
import pymysql
import time



from Config import *

def gettime():
    t=time.strftime("%Y/%m/%d %X")

    return t


def close_data(db,cursor):
    db.close()
    cursor.close()

def process_query(sql):
    db = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    if db.open:
        cursor = db.cursor()
        
    else:
        raise Exception('Failed to connect Database')
    
    
    cursor.execute(sql)
    res=cursor.fetchall()
    close_data(db,cursor)
    
    return res

def get_mid1():
    sql= """
    select 
    sum(confirm),
    (select confirm from history order by ds desc limit 1),
    sum(heal),
    sum(dead)
    from details
    where update_time=(select update_time from details order by update_time desc limit 1)
    """
    
    return process_query(sql)[0]

def get_mid2():
    sql = """
    select province,sum(confirm_add) from details
    where update_time=(select update_time from details order by update_time desc limit 1)
    group by province
    """
    
    return process_query(sql)

def get_left1():
    sql =  """
    select ds,confirm,suspect,heal,dead from history
    """
    
    return process_query(sql)


def get_left2():
    sql =  """
    select ds,confirm_add,suspect_add,heal_add,dead_add from history
    """
    
    return process_query(sql)

def get_right1():

    sql="""
    select province, sum(confirm_add) from details  
    where update_time=(select update_time from details order by update_time desc limit 1) 
    group by province
    order by sum(confirm_add) desc limit 5
    """
    
    return process_query(sql)

def get_right2():
    sql =  """
    select content,hotindex from hotsearch
    """
    
    return process_query(sql)

def get_word():
    sql =  """
    select content,hotindex from googletrend;
    """
    
    return process_query(sql)



# data=get_right2()
# content=[]
# for a in data:
#     content.append(a)


# print(content)