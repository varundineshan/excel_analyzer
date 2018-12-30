from flask import Flask, render_template, jsonify,request
import pandas as pd
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))



app = Flask(__name__)
@app.route('/')
def index():
    return render_template('upload.html')

#---------------- processing selected date------------------------------------

@app.route('/get_data/', methods=['GET','POST'])
def _get_data():
    #df = pd.read_excel("F:\\mybook.xlsx")
    df=pd.read_excel("sheets/testing_file.xlsx")
    date = request.form['date']

    another=request.form['selected']

    print(another)
    df_new=pd.DataFrame()
    df_new=df[df['date']>date]
    print(df_new)
    temp = []
    indexer=[]
    for row in df_new.iterrows():
        index, data = row
        temp.append(data.tolist())
    print(temp)
    indexer = list(df_new)

    return jsonify({'data': render_template('response.html', myList=temp,header=indexer)})


#--------------uploading section below----------------------------------------------------

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'sheets/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        #filename = file.filename
        destination = "/".join([target,"testing_file.xlsx"])
        print(destination)
        file.save(destination)
    return render_template("index.html")

@app.route("/learn")
def learn():
    return render_template("testing.html")

if __name__ == "__main__":
    app.run(debug=True)