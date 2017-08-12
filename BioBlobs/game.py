from flask import Flask
from flask import render_template
from flask import request
import createblobs as createblobs
import score as score
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
	trace4x=[]
	trace4y=[]
	return render_template("hello.html", trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2x, trace3x=trace3x, trace3y = trace3y, trace4x=trace4x, trace4y = trace4y)


@app.route("/signup", methods=["POST"])
def submittted():
	form_data = request.form
	simvalues = score.playgametest(form_data['param1'], form_data['param2'])
	scores = score.scoretest()
	trace1x= scores[0][0]
	trace1y= scores[0][1]
	trace2x= scores[1][0]
	trace2y= scores[1][0]
	trace3x= simvalues[0]
	trace3y= simvalues[1]
	trace4x= simvalues[0]
	trace4y= simvalues[2]
	print 'form submitted, data in form:'
	print form_data
	test = createblobs.test(form_data['param1'],form_data['param2'])
	return render_template("hello.html", trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2x, trace3x=trace3x, trace3y = trace3y, trace4x=trace4x, trace4y = trace4y)

app.run(
	debug = True)

