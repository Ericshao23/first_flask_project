from flask import Flask,render_template,url_for,redirect,request,session
import config
from models import User
from  exts import db


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history/')
def history():
    return render_template('history.html')

@app.route('/scenery/')
def scenery():
    return render_template('scenery.html')

@app.route('/autumn/')
def autumn():
    return render_template('autumn.html')

@app.route('/celebrity/')
def celebrity():
    return render_template('celebrity.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        phonenumber = request.form.get('phonenumber')
        password = request.form.get('password')
        user = User.query.filter(User.phonenumber == phonenumber,User.password == password).first()
        if user:
            session['user_id']=user.id
            #如果想在31天内都不需要登录
            # session.permanent = True
            return redirect(url_for('index'))
        else:
           return u'手机号码或者密码错误，请确认后在登录'

@app.route('/registered/',methods=['GET','POST'])
def registered():
    if request.method == 'GET':
        return render_template('registered.html')
    else:
        phonenumber = request.form.get('phonenumber')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #手机号码验证，如果已经注册则不能被注册
        user = User.query.filter(User.phonenumber == phonenumber).first()
        if user:
            return u'该手机号码已经被注册，请更换手机号码！！！'
        else:
            #验证输入的两个密码是否一致
            if password1 !=password2:
                return u'两次密码不一致，请核对后在填写'
            else:
                user = User(phonenumber=phonenumber,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                #注册成功，让页面跳转到登录页面
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))


@app.route('/qinhan/')
def qinhan():
    return render_template('qinhan.html')

@app.route('/songyuan/')
def songyuan():
    return render_template('songyuan.html')

@app.route('/spring/')
def spring():
    return render_template('spring.html')

@app.route('/suitang/')
def suitang():
    return render_template('suitang.html')

@app.route('/summer/')
def summer():
    return render_template('summer.html')

@app.route('/weijin/')
def weijin():
    return render_template('weijin.html')

@app.route('/winter/')
def winter():
    return render_template('winter.html')

@app.route('/yan/')
def yan():
    return render_template('yan.html')

@app.route('/yang/')
def yang():
    return render_template('yang.html')

@app.context_processor
def my_context_processer():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id==user_id).first()
        if user:
            return {'user':user}
    else:
        return {}


if __name__ == '__main__':
    app.run(debug=True)
