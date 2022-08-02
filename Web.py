
from flask import Flask, request, render_template,jsonify
from jieba.analyse import extract_tags
import Connect
import string
import threading
import json
from os import popen

from Config import *

app = Flask(__name__)

@app.route('/') 
def init():
    return render_template('index.html')

@app.route('/time') 
def get_time():
    
    return Connect.gettime()

@app.route('/mid1')
def getmid1():
    res=Connect.get_mid1()
    
    return jsonify({"confirm":res[0],"new_case":res[1],"heal":res[2],"death":res[3]})

@app.route('/mid2')
def getmid2():
    res = []
    data=Connect.get_mid2()
    for i in data:
        res.append({'name': i[0], 'value': int(i[1])})

    return jsonify({'key': res})

@app.route('/left1')
def getleft1():
    
    data=Connect.get_left1()
    date,confirm,suspect,heal,dead=[],[],[],[],[]
    for a,b,c,d,e in data:
        date.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({'date': date,'confirm': confirm,'suspect': suspect,'heal': heal,'dead': dead})

@app.route('/left2')
def getleft2():
    
    data=Connect.get_left2()
    date,confirm_add,suspect_add,heal_add,dead_add=[],[],[],[],[]
    for a,b,c,d,e in data:
        date.append(a.strftime("%m-%d"))
        confirm_add.append(b if b else 0)
        suspect_add.append(c if c else 0)
        heal_add.append(d if d else 0)
        dead_add.append(e if e else 0)
    return jsonify({'date': date,'confirm_add': confirm_add,'suspect_add': suspect_add,'heal_add': heal_add,'dead_add': dead_add})

@app.route('/right1')
def getright1():
    
    data=Connect.get_right1()
    province,confirm_add=[],[]
    for a,b in data:
        province.append(a)
        confirm_add.append(b if b else 0)

    return jsonify({'province': province,'confirm_add': confirm_add})

@app.route('/right2')
def getright2():
    
    data=Connect.get_right2()
    res=[]
    
    for a,b in data:
        # tag=extract_tags(a)
        # for i in tag:
        #     if not i.isdigit():

        #         res.append({'name': i,'value':b})
        res.append({'name': a,'value':b})

    return jsonify({'key':res})

@app.route('/word_l2')
def getword_l2():
    
    data=Connect.get_word()
    res=[]
    
    for a,b in data:
        res.append({'name': a,'value':b})


    return jsonify({'key':res})
    
@app.route('/USA')
def USA():
    with open("./Crawls/static/json/USA.json", 'r') as j:
        contents = json.loads(j.read())
        
    return jsonify(contents)

@app.route('/login') 
def handle():
    Username=request.values.get('user')
    Password=request.values.get('pswd')
    return f'name is {Username}, password is {Password}'

@app.route('/account') 
def handle2():

    return """    
    <form action='/login'>
        Username: <input name='user'> 
        Password: <input name='pswd'>
        <input type='submit'>
    </form>
    """
    
def cron_task():
    from datetime import datetime
    from time import sleep
    
    print(f'Every {PAUSE} hour update Data')
    while True:
        now = datetime.now()
        if  (now.hour % PAUSE) == 0 and now.minute == 0 and now.second == 0:
            task = popen('python ./Crawls/Getdata.py')
            sleep(10)
            result = task.read()
            print(result)
            task.close()
            sleep(60*60*1 - 100)
        sleep(0.8)

if __name__ == '__main__':
    threading.Thread(target=cron_task).start()
    app.run(host='127.0.0.1')

