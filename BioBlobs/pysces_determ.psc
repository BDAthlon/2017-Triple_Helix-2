# PySCeS test input file
# Simple linear pathway (2004)

#FIX: mRNA protein

R1:
    mRNA > {2} mRNA
    Ksynmrna

R2:
    mRNA > $pool
    Kdeg1*mRNA

R3:
    protein > {2} protein
    Ksynprotein*mRNA

R4:
    protein > $pool
    Kdeg2*protein

# Fixed species
 
# Variable species
mRNA = 1
protein = 0
 
# Parameters
Ksynmrna = 0.05
Kdeg1 = 0.1

Ksynprotein = 0.3
Kdeg2 = 0.6
