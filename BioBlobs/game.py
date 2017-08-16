from flask import Flask
from flask import render_template
from flask import request
import createblobs as createblobs
import score as score
import json
#import playgame as playgame
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
	return render_template("hello.html", trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2y, trace3x=trace3x, trace3y=trace3y, trace4x=trace4x, trace4y=trace4y)


@app.route("/signup", methods=["POST"])
def submittted():
	form_data = request.form
	print 'form submitted, data in form:'
	print form_data
	scores = score.score()
	simvalues = score.playgametest(form_data['param1'], form_data['param2'])
	print 'scores:' + str(scores)
	print 'simvalues:' + str(simvalues)
	try:
		trace1x= score.convert_to_integers(scores[0][0])
		trace1y= score.convert_to_integers(scores[0][1])
	except:
		trace1x=[1]
		trace1y=[1]
	trace2x= score.convert_to_integers(scores[1][0])
	trace2y= score.convert_to_integers(scores[1][1])
	trace3x= simvalues[0]
	trace3y= simvalues[1]
	trace4x= simvalues[0]
	trace4y= simvalues[2]


	return render_template("hello.html", trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2y, trace3x=trace3x, trace3y=trace3y, trace4x=trace4x, trace4y=trace4y)

app.run(
	debug = True)
