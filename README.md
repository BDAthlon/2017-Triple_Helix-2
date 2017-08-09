# Bio Green Globs


Here we make parameter searching fun by creating a game where users can choose whether to simulate data using stochastic or deterministic means and vary parameters in order to create protein plots that hit certain targets, or blobs.

The game is written as a python web app with flask. To open the GUI, run the game.py file from the command line. (After you installing the requirements.)

The parameters are given in an form and then the new values for the graph are generated with python. The new XY coordinates are passed on to and the new graph is plotted on the fly with javascript library plotly.

The requirements for the python code are: numpy,scipy,matplotlib,pysces,stochpy


Examples of plot:

Glob plots

![alt text](https://github.com/BDAthlon/2017-Triple_Helix-2/blob/master/BioBlobs/plot_blobs.png)


Stochastic simulations

![alt text](https://github.com/BDAthlon/2017-Triple_Helix-2/blob/master/BioBlobs/stoch.png)

Deterministic simulations

![alt text](https://github.com/BDAthlon/2017-Triple_Helix-2/blob/master/BioBlobs/determ.png)


--- as you see it is not finished --- if only we had one more day ---

This is a project by Iulia Gherman, James Scott-Brown and Margarita Kopniczky for the 2017 DBAthlon, IWBDA, Pittsburgh.
