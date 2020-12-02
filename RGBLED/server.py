from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/min')
def min():
    return render_template("index_html")

if __name__=='__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)

