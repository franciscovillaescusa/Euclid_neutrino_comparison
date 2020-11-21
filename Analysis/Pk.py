import numpy as np
import MAS_library as MASL
import Pk_library as PKL

snapshot = '/mnt/ceph/users/fvillaescusa/Euclid/Euclid_neutrino_comparison/Sims/0.0eV/snap_004'
fout     = 'Pk_0.0eV_z=0.txt'

#snapshot = '/mnt/ceph/users/fvillaescusa/Euclid/Euclid_neutrino_comparison/ICs/0.0eV/ics'
#fout     = 'Pk_0.0eV_z=127.txt'

#snapshot = '/mnt/ceph/users/fvillaescusa/Euclid/Euclid_neutrino_comparison/param_files/0.0eV/ics'
#fout     = 'Pk_0.0eV_z=127.txt'


grid     = 512  
ptypes   = [1] 
MAS      = 'CIC' 
do_RSD   = False
axis     = 0 
BoxSize  = 512.0 #Mpc/h
threads  = 1
verbose  = True

delta = MASL.density_field_gadget(snapshot, ptypes, grid, MAS, do_RSD, axis)
delta /= np.mean(delta, dtype=np.float64);  delta -= 1.0

# compute Pk
Pk = PKL.Pk(delta, BoxSize, axis, MAS, threads, verbose)

np.savetxt(fout, np.transpose([Pk.k3D, Pk.Pk[:,0]]))
