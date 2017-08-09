import random
import matplotlib.pyplot as plt
import os
import csv

def createblobs(bias):
    if bias:
        on_off_bias = random.choice([True, False])
        if on_off_bias:
            how_many_on = random.randint(6,10)
        else:
            how_many_on = random.randint(1,5)
        high_value = random.randint(1,300)
        blob_values = [high_value] * how_many_on + [0] * (10-how_many_on)
        random.shuffle(blob_values)
    
    else:
        blob_values = random.sample(range(1,300),10)
    x_values = range(5,51,5)
    blob_dict = dict(zip(x_values,blob_values))

    blob_dict = zip(x_values,blob_values)
    #plot
    #plt.plot(x_values,blob_values,'go')
#plt.xlabel('time')
#   plt.ylabel('expression levels')
#   plt.axis([0,55,0,max(blob_values)+5])
#   plt.savefig('plot_blobs.png')

    #plot blob values as csv
    currentdir = os.getcwd()
    os.chdir(currentdir)
    with open("blobvalues.csv","wb") as f:
        writer = csv.writer(f)
        writer.writerows(blob_dict)
    return blob_dict

bias = 0 #bias of 0 means blobs are randomly generated within range 0,300
# otherwise they are generated so all blobs have either a high or low value
blob_dict = createblobs(bias)
#print blob_dict


