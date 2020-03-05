from flask import Flask,render_template,request
from datetime import datetime as dt
import os

now=dt.today()
info={}

app=Flask(__name__)
@app.route('/')
def main():
    return render_template('Form.html')

@app.route('/NextPage',methods=['POST'])
def main2():
    username=request.form['Name'] 
    email=request.form['Email']
    username=username.replace(' ','')
    if username in info.keys() or email in info.values():
        return render_template('taken.html')
    info[username]=email
    user_name=username
    return render_template('NextPage.html',name=user_name)

@app.route('/login')
def main3():
    return render_template('login.html')

@app.route('/profile',methods=['POST'])
def main4():
    username=request.form['username']
    email=request.form['email']
    username=username.replace(' ','')
    if username in info.keys() and email==info.get(username):
        return render_template('profile.html', username=username,email=email)
    else:
        return render_template('Wrong.html')         
@app.route('/profile/receivedata',methods=['POST'])
def main5():
    text=request.form['text']
    title=request.form['title']
    username=request.form['name']
    email=request.form['email']
    now=dt.today()
    try:
        os.mkdir(f'Info/{username}',511)
    except:
        pass
    now=str(now)
    now=now.split('.')
    now=now[0]
    now=now.replace(':','-')
    with open(f'Info/{username}/{title}-{now}.txt','a') as file:
        file.write(text)
    return render_template('receivedata.html',name=username,email=email)
@app.route('/profile/datamanager',methods=['POST'])
def main6():
    username=request.form['username']
    email=request.form['email']
    filelist=os.listdir(f"Info/{username}")
    return render_template("datamanager.html",filelist=filelist,username=username,email=email)
@app.route('/profile/datamanager/readdata',methods=['POST'])
def main7():
    username=request.form['username']
    email=request.form['email']
    filename=request.form['filename']
    filename=filename.replace('.txt','')
    with open(f'Info/{username}/{filename}.txt','r') as file:
        text=file.read()
    return f'<h3>Your Data :</h3><p>{text}</p>'+render_template('readdata.html',username=username,email=email)
app.run(debug=True)
