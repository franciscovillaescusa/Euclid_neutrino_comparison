import numpy as np
import sys,os

################################ INPUT #######################################
fout = 'grid_file_2comp_1.dat'
N    = 1 #total number of particles in the file will be N^3
##############################################################################

Ntot = N**3

# declare different arrays
npart         = np.zeros(6,  dtype=np.int32)
massarr       = np.zeros(6,  dtype=np.float64)
time          = np.zeros(1,  dtype=np.float64)
redshift      = np.zeros(1,  dtype=np.float64)
flag_sfr      = np.zeros(1,  dtype=np.int32)
flag_feedback = np.zeros(1,  dtype=np.int32)
npartall      = np.zeros(6,  dtype=np.int32)
flag_cooling  = np.zeros(1,  dtype=np.int32)
num_files     = np.ones(1,   dtype=np.int32)
BoxSize       = np.zeros(1,  dtype=np.float64);  BoxSize[0] = 100.0 
extra_array   = np.zeros(30, dtype=np.float32) #120 bytes

# fill the number of particles arrays
npart[1], npartall[1] = Ntot, Ntot
npart[2], npartall[2] = Ntot, Ntot

# declare the arrays hosting the particle positions
pos  = np.zeros((Ntot, 3), dtype=np.float32)
pos2 = np.zeros((Ntot, 3), dtype=np.float32)

# find the particle positions
for i in xrange(0,N):
    for j in xrange(0,N):
        for k in xrange(0,N):
            pos[(i*N+j)*N+k, 0] = (i+0.0)*BoxSize/N
            pos[(i*N+j)*N+k, 1] = (j+0.0)*BoxSize/N
            pos[(i*N+j)*N+k, 2] = (k+0.0)*BoxSize/N

# for the second particle type displace them
pos2[:] = pos[:] + 0.5*BoxSize/N

# arrays with the number of bytes of each block
blocksize1 = np.array([256],                 dtype=np.int32)
blocksize2 = np.array([4*Ntot*3 + 4*Ntot*3], dtype=np.int32)

# write the binary file
f = open(fout, 'wb')
for array in [blocksize1, npart, massarr, time, redshift, flag_sfr,
              flag_feedback, npartall, flag_cooling, num_files,
              BoxSize, extra_array, blocksize1,
              blocksize2, pos, pos2, blocksize2]:
    array.tofile(f)
f.close()
