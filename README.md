This repository contains the codes used by the particle-based group as part of the Euclid neutrino comparison project.

**CLASS**

This folder contains the CLASS parameter file needed to define the cosmological model for each cosmology


**Codes**

This folder contains 

- reps: the code used to compute the initial matter power spectrum, transfer functions, and growth rate functions needed to generate the ICs

- N-GenIC_growth: the code used to generate the ICs in cosmologies with massive neutrinos, where the scale factor/growth are scale-dependent.

**ICs**

This folder contain the ICs, in Gadget-I format, together with the coordinates, amplitudes and phases of the modes used the generate the ICs. This folder is not visible in github, but can be accessed via globus.org by typing Euclid_NU_comparison in collection. Data can be easily transferred from there either to personal computers or super computers.

The way the ICs files are structured is as follows:

- ics.Y: These are the Gadget format-I initial condition files. Y goes from 0 to the number of subfiles - 1.

- Coordinates_ptype_X.Y. These files contain the coordinates of the modes. X is the particle type (1-CDM, 2-NU). Y goes from 0 to the number of subfiles - 1. Each mode comes from a grid with coordinates (Nx, Ny, Nz), where Nx ranges from 0 to (Nmesh-1), Ny ranges from 0 to (Nmesh-1), and Nz goes from 0 to Nmesh/2. The number that is stored in the file is (Nx * Nmesh + Ny) * (Nmesh / 2 + 1) + Nz. Each subfile can be read in python with a script like this:

```python
import numpy as np

# read a particular coordinate file
f_in = 'Coordinates_ptype_1.0'
f = open(f_in, 'rb')
Nfiles = np.fromfile(f, dtype=np.int32, count=1)[0] #Number of coordinate subfiles	
Nmesh  = np.fromfile(f, dtype=np.int32, count=1)[0] #Nmesh size
Nx     = np.fromfile(f, dtype=np.int32, count=1)[0] #slab offset (not used)
coordinates = np.fromfile(f, dtype=np.int64, count=-1)

# get the Nx, Ny, Nz coordinates of the modes
kx = (coordinates//(Nmesh//2 + 1))//Nmesh
ky = (coordinates//(Nmesh//2 + 1))%Nmesh
kz = (coordinates%(Nmesh//2 + 1))%Nmesh
```

- Amplitudes_ptype_X.Y. These files contain the amplitudes of the modes. X is the particle type (1-CDM, 2-NU). Y goes from 0 to the number of subfiles - 1. The coordinates of the modes can be obtained from the Coordinates_ptype_X.Y files; both files have the same particle order (i,e. particle 34 in file 3 of Coordinates will correspond to particle 34 in file 3 of Amplitudes). These files can be read in python with a script like this:

```python
import numpy as np

f_in = 'Amplitudes_ptype_1.0'
f = open(f_in,'rb')
Nfiles = np.fromfile(f, dtype=np.int32, count=1)[0] #Number of coordinate subfiles	
Nmesh  = np.fromfile(f, dtype=np.int32, count=1)[0] #Nmesh size
Nx     = np.fromfile(f, dtype=np.int32, count=1)[0] #slab offset (not used)
amplitudes = np.fromfile(f, dtype=np.float32, count=-1)
f.close()
```

- Phases_ptype_X.Y. These files contain the phases of the modes. X is the particle type (1-CDM, 2-NU). Y goes from 0 to the number of subfiles - 1. The coordinates of the modes can be obtained from the Coordinates_ptype_X.Y files; both files have the same particle order (i,e. particle 34 in file 3 of Coordinates will correspond to particle 34 in file 3 of Phases). These files can be read in python with a script like this:

```python
import numpy as np

f_in = 'Phases_ptype_1.0'
f = open(f_in,'rb')
Nfiles = np.fromfile(f, dtype=np.int32, count=1)[0] #Number of coordinate subfiles	
Nmesh  = np.fromfile(f, dtype=np.int32, count=1)[0] #Nmesh size
Nx     = np.fromfile(f, dtype=np.int32, count=1)[0] #slab offset (not used)
phases = np.fromfile(f, dtype=np.float32, count=-1)
f.close()
```


**param_files**

This folder contain the parameter files used to generate the input power spectra, transfer functions, and growth rates (param_file.reps) and the parameter file for N-GenIC_growth (N-GenIC.param). We also store the file logfile, containing the output generated when running N-GenIC_growth.

