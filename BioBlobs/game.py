from flask import Flask
from flask import render_template
from flask import request
import createblobs as createblobs

app = Flask("BioBlobs") #this is defininf our flak app

@app.route("/")
def hello():
	test = '0'
	trace1x= [1, 2, 3, 4]
	trace1y= [1, 2, 3, 4]
	trace2x=[]
	trace2y=[]
	trace3x=[]
	trace3y=[]
	return render_template("hello.html", test=test, trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2x, trace3x=trace3x, trace3y = trace3y)


@app.route("/signup", methods=["POST"])
def submittted():
	trace1x= [1, 2, 3, 4]
	trace1y= [1, 2, 3, 4]
	trace2x=[]
	trace2y=[]
	trace3x=[]
	trace3y=[]
	form_data = request.form
	print 'form submitted, data in form:'
	print form_data
	test = createblobs.test(form_data['param1'],form_data['param2'])
	return render_template("hello.html", test=test, trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2x, trace3x=trace3x, trace3y = trace3y)

app.run(
	debug = True)

