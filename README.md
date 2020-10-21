This repository contains the codes used by the particle-based group as part of the Euclid neutrino comparison project.

** CLASS **

This folder contains the CLASS parameter file needed to define the cosmological model for each cosmology


** Codes **

This folder contains 

- reps: the code used to compute the initial matter power spectrum, transfer functions, and growth rate functions needed to generate the ICs

- N-GenIC_growth: the code used to generate the ICs in cosmologies with massive neutrinos, where the scale factor/growth are scale-dependent.

** ICs **

This folder contain the ICs, in Gadget-I format, together with the coordinates, amplitudes and phases of the modes used the generate the ICs. This folder is not visible in github, but can be accessed via globus.org by typing Euclid_NU_comparison in collection. Data can be easily transferred from there either to personal computers or super computers.

The way the ICs files are structured is as follows:

- ics.Y: These are the Gadget format-I initial condition files
- Coordinates_ptype_X.Y. These files contain the coordinates of the modes. X is the particle type (1-CDM, 2-NU). Y goes from 0 to the number of subfiles - 1. Each mode comes from a grid with 

** param_files **

This folder contain the parameter files used to generate the input power spectra, transfer functions, and growth rates (param_file.reps) and the parameter file for N-GenIC_growth (N-GenIC.param). We also store the file logfile, containing the output generated when running N-GenIC_growth.

