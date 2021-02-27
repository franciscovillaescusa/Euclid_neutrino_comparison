import numpy as np
import Pk_library as PKL
import sys,os

#################################### INPUT ###########################################
BoxSize = 512.0 #Mpc/h
grid    = 1024

#fin     = '../../../param_files/0.3eV/reps_files/0.3eV_Pm_rescaled_z127.0000.txt'
#fout    = 'Pk_binned_CLASS_0.3eV_matter_z=127.txt'

#fin     = '../../../param_files/0.3eV/reps_files/0.3eV_Pcb_rescaled_z127.0000.txt'
#fout    = 'Pk_binned_CLASS_0.3eV_cb_z=127.txt'

fin     = '../../../param_files/0.3eV/reps_files/0.3eV_Pn_rescaled_z127.0000.txt'
fout    = 'Pk_binned_CLASS_0.3eV_n_z=127.txt'
######################################################################################

# read Pk
k, Pk = np.loadtxt(fin, unpack=True)
k  = k.astype(np.float32)
Pk = Pk.astype(np.float32)

# compute binned Pk and save results to file
k, Pk, Nmodes = PKL.expected_Pk(k, Pk, BoxSize, grid)
np.savetxt(fout, np.transpose([k, Pk]))
