#this file use encoding: utf-8


from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "hello Leo. This is from flask."


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

@app.route("/re/<int:code>")
def redirect_demo(code):
    return redirect("/newpath", code=code)


if __name__ == "__main__":
    app.run(debug=True)






