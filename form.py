from flask import Flask, request, render_template
import numpy
import pickle
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":


        with open('model_pkl', 'rb') as f:
            lr = pickle.load(f)

        spend = request.form.get("spend")
        administration = request.form.get("administration")
        marketspend = request.form.get("marketspend")
        profit = request.form.get("profit")

        statearr = []

        states = request.form['state']

        if (states == 'newYork'):
            statearr = [0,0,1]

        elif (states == 'california'):
            statearr = [1,0,0]

        else:
            statearr = [0,1,0]


        z = []
        z.append(spend)
        z.append(administration)
        z.append(marketspend)
        z.append(profit)

        z.extend(statearr)

        arr = numpy.array(z,dtype = float)

        result = lr.predict([arr])

        return render_template('form.html', prediction_text="Your profit is Rs. {:.2f}".format(result[0,0]))


    return render_template("form.html")

if __name__=='__main__':
   app.run()
