from flask import Flask,render_template,request
import pandas as pd 


# 实例化Flask对象，传的参数默认使用__name__
app = Flask(import_name=__name__,
            # static_url_path='/python', # 配置静态文件的访问 url 前缀
            # static_folder='static',    # 配置静态文件的文件夹
            template_folder='templates') # 配置模板文件的文件夹

# 首页
# 获取当前时间的状况
@app.route("/")
def index():
    name = str(pd.datetime.now())[:10] + ".html" 
    return render_template(name)

@app.route('/history')
def get_year():
    date = request.args.get("date",str(pd.datetime.now())[:10])
    name = str(date) + ".html"
    return render_template(name)

# @app.route('/shiwen')
# def show_all():
#     content =  df.to_dict("records")
#     return render_template('one_for_all.html',content=content)

if __name__ == '__main__':
    app.run(host= "0.0.0.0",port=5000,debug=False)