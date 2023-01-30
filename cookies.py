from flask import *

app= Flask(__name__)

@app.route('/set')
def setcookie():
    res = make_response("<h1> Cookie is set </h1>")
    res.set_cookie('framework','flask')
    return res

@app.route('/get')
def getcookie():
    name = request.cookies.get('framework')
    return name
@app.route('/')
def index():
    count=int(request.cookies.get('visit_count',0))
    count+=1
    msg="visited this page"+ str(count)
    resp= make_response(msg)
    resp.set_cookie('visit_count', str(count))
    return resp

if __name__=='__main__':
    app.run(debug=True)

