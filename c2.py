#this file use encoding: utf-8


from flask import Flask
from flask import request
from flask import redirect
from flask import render_template,flash,get_flashed_messages

app = Flask(__name__)
#用这个设置JINJA模板中line_statement的标识符
app.jinja_env.line_statement_prefix = "#"
#设置secret_key可以标识用户的session
app.secret_key = "leoeatle"


@app.route("/")
@app.route("/index/")
def index():
    res = ''
    for msg, category in get_flashed_messages(with_categories = True):
        res += res + category + msg + '<br>'

    return "hello Leo. This is from flask." + res


#'/'自动补齐
#可以多映射(添加app.route)
#参数使用尖括号
@app.route("/profile/<uid>/", methods = ["GET","POST"])
def profile(uid):
    colors = {'red','green'}
    return render_template('profile.html', uid = uid, colors = colors)


@app.route("/request")
def request_demo():
    res = ""

    # for property in dir(request):
    #     res = res + str(property) + '左边这是变量' + (str(eval('request.' + property))) + '<br>'

    res2 = request.args.get("key", "defaultkey") + "<br>"
    #res.decode('gb18030')

    res_url = request.url + "++" + request.path + "<br>"
    print  res2
    res3 = res2 +  res_url
    return res3

@app.route('/newpath')
def new_path():
    return "new path"

#如果code是301,就是永久跳转,浏览器会临时保存
#如果code是302,就是暂时跳转
@app.route("/re/<int:code>")
def redirect_demo(code):
    return redirect("/newpath", code=code)

#使用errorhandler对异常情况做统一处理
@app.errorhandler(404)
def page_not_found(error):
    return render_template("not_found.html", url=request.url)

@app.route("/login")
def login():
    #每一次进入login就会在缓存区域存下新的Welcome
    flash('Welcome','info')



if __name__ == "__main__":
    app.run(debug=True)






