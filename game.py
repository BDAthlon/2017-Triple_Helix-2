from flask import Flask
from flask import render_template
from flask import request
import os

import createblobs as createblobs
import score as score
import playgame as playgame

app = Flask("BioBlobs") #this is defininf our flak app

@app.route("/")
def hello():
	blobs = createblobs.createblobs(0)
	blobxy = zip(*blobs)
	print 'Random blob coordinates: ' + str(blobxy)
	trace1x= blobxy[0]
	trace1y= blobxy[1]
	trace2x=[]
	trace2y=[]
	trace3x=[]
	trace3y=[]
	trace4x=[]
	trace4y=[]
	return render_template("hello.html", trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2y, trace3x=trace3x, trace3y=trace3y, trace4x=trace4x, trace4y=trace4y)


@app.route("/submit", methods=["POST"])
def submittted():
	form_data = request.form
	print 'form submitted, data in form:'
	print form_data

	stochastic = (form_data['stochastic'] == "true")
	
	scores = score.score()
	simvalues = playgame.playgame(os.getcwd(), stochastic, float(form_data['param1']), float(form_data['param2']))
	print 'scores:' + str(scores)
	print 'simvalues:' + str(simvalues)
	try:
		trace2x= score.convert_to_integers(scores[0][0])
		trace2y= score.convert_to_integers(scores[0][1])
	except:
		trace2x=[1]
		trace2y=[1]
	trace1x= score.convert_to_integers(scores[1][0])
	trace1y= score.convert_to_integers(scores[1][1])
	trace3x= score.convert_to_integers(simvalues[0])
	trace3y= score.convert_to_integers(simvalues[1])
	trace4x= score.convert_to_integers(simvalues[0])
	trace4y= score.convert_to_integers(simvalues[2])

	return render_template("hello.html", trace1x=trace1x, trace1y=trace1y, trace2x=trace2x, trace2y=trace2y, trace3x=trace3x, trace3y=trace3y, trace4x=trace4x, trace4y=trace4y)

app.run(
	debug = True)
