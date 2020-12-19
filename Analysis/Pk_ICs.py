import numpy as np
import Pk_library as PKL

# parameters
root          = '../ICs/0.0eV'
f_coordinates = '%s/Coordinates_ptype_1'%root 
f_amplitudes  = '%s/Amplitudes_ptype_1'%root  
BoxSize       = 512.0                 #Mpc/h
fout          = 'Pk_ICs_0.0eV.txt'

# compute Pk of the initial field
# k will be in h/Mpc, while P(k) will have (Mpc/h)^3 units
k, Pk, Nmodes = PKL.Pk_NGenIC_IC_field(f_coordinates, f_amplitudes, BoxSize)

# save results to file
np.savetxt(fout, np.transpose([k,Pk,Nmodes]))
