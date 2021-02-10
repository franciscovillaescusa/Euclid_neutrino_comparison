import numpy as np
import Pk_library as PKL

####################################### INPUT #########################################
# parameters
root = '/mnt/ceph/users/fvillaescusa/Euclid/Euclid_neutrino_comparison/Sims/0.15eV'
grid          = 1024   #grid size
particle_type = [1,2]  #use dark matter [1]
do_RSD        = False  #move particles to redshift-space and calculate Pk in redshift-space
axis          = 1      #RSD placed along the y-axis
cpus          = 8      #number of openmp threads
folder_out    = './'   #folder where to write results
#######################################################################################

# do a loop over the different snapshots
for snapnum in [1,2,3,4]:

    # snapshot name
    snapshot = '%s/snap_%03d.hdf5'%(root,snapnum)

    # compute power spectrum of the snapshot
    PKL.Pk_Gadget(snapshot, grid, particle_type, do_RSD, axis, cpus, folder_out)
