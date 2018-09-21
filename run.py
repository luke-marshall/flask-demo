from flask import Flask, render_template, request, jsonify
import os


app = Flask(__name__)


# Here you go to http://127.0.0.1:5000/
@app.route('/')
def main():
  return render_template('index.html')



# Here you go to http://127.0.0.1:5000/data
@app.route('/data')
def data():
  return jsonify(
      { 'data' : [1,2,3,4,5] }
    )

if __name__ == '__main__':
  
  app.run(debug=True)

  # init_gui(app)  #This one runs it as a standalone app