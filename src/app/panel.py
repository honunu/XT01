from flask import Flask

app =  Flask(__name__)

@app.route('/')
def panel():
    return '<h2>Control panel</h2>'

if  __name__=='__main__':
    app.run(host="0.0.0.0",debug=True, port=80)
