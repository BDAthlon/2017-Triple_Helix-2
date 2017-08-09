import os
currentdir = os.getcwd()
os.chdir(currentdir)
import random
import pysces
import matplotlib.pyplot as plt
import stochpy
import numpy as np
import csv
import pandas as pd

def playgame(currentdir,type,parameter1,parameter2):
    #parameter 1 determines final level
    #parameter 2 determines
    #type should be 0 or 1 -> toggle between stochastic and deterministic
    
    if type:
        #stochastic
        #change directory
        
        smod = stochpy.SSA()
        os.chdir(currentdir)
        smod.Model(currentdir+'/mRNAproteinIulia.psc')
        
        #change parameters
        smod.ChangeParameter("Ksynmrna",parameter1)
        smod.ChangeParameter("Kdeg2",parameter2)
        #smod.ChangeInitialSpeciesCopyNumber("Kdeg1",parameter2)
        
        #smod.data_stochsim.simulation_endtime
        #smod.data_stochsim.simulation_timesteps = 51.0
        smod.Timesteps(50)
        smod.Endtime(50)
        smod.DoStochSim(end=50)
        
        #Only plot as a test
        #smod.PlotSpeciesTimeSeries()
        #pysces.plt.setAxisLabel('x', label='time')
        #pysces.plt.setAxisLabel('y', label='expression levels')
        #plt.savefig(currentdir+'/stoch.png')
        
        simvalues_stoch = smod.data_stochsim.getSpecies()
        x_values = range(5,51,5)
        
        #arrange results
        time_val = []
        mRNA_val = []
        protein_val =[]
        for list in simvalues_stoch:
            time_val.append(list[0])
            mRNA_val.append(list[1])
            protein_val.append(list[2])
        time_val_rounded = []
        for i in time_val:
            time_val_rounded.append(int(round(i)))
        count = 0
        mRNA_final = []
        protein_final = []
        for val in range(0,len(mRNA_val)-1):
            mRNA_final.append([mRNA_val[val]] * ((time_val_rounded[count+1] - time_val_rounded[count])))
            protein_final.append([protein_val[val]] * ((time_val_rounded[count+1] - time_val_rounded[count])))
            count = count + 1
        time_final = range(1,51)
        mRNA_final = flatten(mRNA_final)
        protein_final = flatten(protein_final)
        simvalues = zip(time_final,mRNA_final,protein_final)

        return simvalues

    else:
        #deterministic
        os.chdir(currentdir)
        print(currentdir+'/pysces_determ.psc')
        mod = pysces.model('pysces_determ',dir=currentdir)
        #change params
        mod.Ksynmrna = parameter1
        mod.Kdeg2 = parameter2
        mod.doSim(end=50.0, points=50.0)
        mod.Simulate()
        #print os.getcwd(), '\n\n\n'
        #mod.doSimPlot()
        
        #plot here to check it works but don't actually plot
        mod.sim_start = 1.0
        mod.doSimPlot(end=50.0, points=51, plot='species', fmt='lines', filename=None)
        #pysces.plt.p_activateInterface('matplotlib')
        #pysces.plt.setAxisLabel('x', label='time')
        #pysces.plt.setAxisLabel('y', label='expression levels')
        #plt.savefig(currentdir+'/simpledeterm.png')
        #plt.close()

        #get simulation values
        simvalues = mod.data_sim.getSpecies()
#       print(mod.data_sim.getSpecies())
        return simvalues

def flatten(l):
    flat_list =[]
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list


type = 0
#sim_yvaluesmRNA, sim_yvaluesprotein = playgame(type)
#print(sim_yvaluesmRNA, sim_yvaluesprotein,'\n')
simvalues = playgame(currentdir,type,50,5)
os.chdir(currentdir)
with open("simvalues.csv","wb") as f:
    writer = csv.writer(f)
    writer.writerows(simvalues)
#print simvalues


#csv_file = "simvalues.csv"
#df = pd.read_csv(csv_file)
#print df(1)
#included_cols = 1


#mod.SimPlot(plot='species', filename=None, title=None, log=None, format='lines')




