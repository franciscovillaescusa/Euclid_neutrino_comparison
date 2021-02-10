import numpy as np
import Pk_library as PKL
import sys,os

#################################### INPUT ###########################################
BoxSize = 512.0 #Mpc/h
grid    = 1024

fins = ['../../param_files/0.15eV/reps_files/0.15eV_Pm_rescaled_z0.0000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pcb_rescaled_z0.0000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pn_rescaled_z0.0000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pm_rescaled_z0.5000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pcb_rescaled_z0.5000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pn_rescaled_z0.5000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pm_rescaled_z1.0000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pcb_rescaled_z1.0000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pn_rescaled_z1.0000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pm_rescaled_z2.0000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pcb_rescaled_z2.0000.txt',
        '../../param_files/0.15eV/reps_files/0.15eV_Pn_rescaled_z2.0000.txt'] 

fouts = ['Pk_binned_CLASS_0.15eV_matter_z=0.txt',
         'Pk_binned_CLASS_0.15eV_cb_z=0.txt',
         'Pk_binned_CLASS_0.15eV_n_z=0.txt',
         'Pk_binned_CLASS_0.15eV_matter_z=0.5.txt',
         'Pk_binned_CLASS_0.15eV_cb_z=0.5.txt',
         'Pk_binned_CLASS_0.15eV_n_z=0.5.txt',
         'Pk_binned_CLASS_0.15eV_matter_z=1.txt',
         'Pk_binned_CLASS_0.15eV_cb_z=1.txt',
         'Pk_binned_CLASS_0.15eV_n_z=1.txt',
         'Pk_binned_CLASS_0.15eV_matter_z=2.txt',
         'Pk_binned_CLASS_0.15eV_cb_z=2.txt',
         'Pk_binned_CLASS_0.15eV_n_z=2.txt']
######################################################################################

# do a loop over the different files
for fin,fout in zip(fins, fouts):

    # read Pk
    k, Pk = np.loadtxt(fin, unpack=True)
    k  = k.astype(np.float32)
    Pk = Pk.astype(np.float32)

    # compute binned Pk and save results to file
    k, Pk, Nmodes = PKL.expected_Pk(k, Pk, BoxSize, grid)
    np.savetxt(fout, np.transpose([k, Pk]))
