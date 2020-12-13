import numpy as np
import MAS_library as MASL
import Pk_library as PKL
import readgadget

root = '/mnt/ceph/users/fvillaescusa/Euclid/Euclid_neutrino_comparison/Sims'

snapshots = ['%s/0.0eV_1000_reps/snap_004'%root,
             '%s/0.0eV_1000_reps_1/snap_004'%root,
             '%s/0.0eV_512_reps/snap_004'%root,
             '%s/0.0eV_512_reps_1/snap_004'%root,
             '%s/0.0eV_1000_2LPT/snap_004'%root,
             '%s/0.0eV_1000_2LPT_1/snap_004'%root,
             '%s/0.0eV_512_2LPT/snap_004'%root,
             '%s/0.0eV_512_2LPT_1/snap_004'%root]

fouts     = ['Pk_0.0eV_1000_reps_z=0.txt',
             'Pk_0.0eV_1000_reps_1_z=0.txt',
             'Pk_0.0eV_512_reps_z=0.txt',
             'Pk_0.0eV_512_reps_1_z=0.txt',
             'Pk_0.0eV_1000_2LPT_z=0.txt',
             'Pk_0.0eV_1000_2LPT_1_z=0.txt',
             'Pk_0.0eV_512_2LPT_z=0.txt',
             'Pk_0.0eV_512_2LPT_1_z=0.txt']

grid     = 512  
ptypes   = [1] 
MAS      = 'CIC' 
do_RSD   = False
axis     = 0 
threads  = 1
verbose  = True

# do a loop over all snapshots
for snapshot,fout in zip(snapshots,fouts):
    
    # read header
    header   = readgadget.header(snapshot)
    BoxSize  = header.boxsize/1e3  #Mpc/h

    delta = MASL.density_field_gadget(snapshot, ptypes, grid, MAS, do_RSD, axis)
    delta /= np.mean(delta, dtype=np.float64);  delta -= 1.0

    # compute Pk
    Pk = PKL.Pk(delta, BoxSize, axis, MAS, threads, verbose)

    np.savetxt(fout, np.transpose([Pk.k3D, Pk.Pk[:,0]]))
