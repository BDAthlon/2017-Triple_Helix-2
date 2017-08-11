from flask import Flask
from flask import render_template
from flask import request
import createblobs as createblobs

app = Flask("BioBlobs") #this is defininf our flak app

@app.route("/")
def hello():
	blobs = createblobs.createblobs(0)
	blobxy = zip(*blobs)
	print blobxy
	trace1x= blobxy[0]
	trace1y= blobxy[1]
	trace2x=[]
	trace2y=[]
	trace3x=[]
	trace3y=[]
	return render_template("hello.html", trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2x, trace3x=trace3x, trace3y = trace3y)


@app.route("/signup", methods=["POST"])
def submittted():
	trace1x= blobxy[0]
	trace1y= blobxt[1]
	trace2x=[]
	trace2y=[]
	trace3x=[]
	trace3y=[]
	form_data = request.form
	print 'form submitted, data in form:'
	print form_data
	test = createblobs.test(form_data['param1'],form_data['param2'])
	return render_template("hello.html", trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2x, trace3x=trace3x, trace3y = trace3y)

app.run(
	debug = True)

