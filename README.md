This repository contains the codes used by the particle-based group as part of the Euclid neutrino comparison project.

Steps:

- Define the cosmological model, i.e. value of the cosmological parameter, neutrino masses and splitting

- Run Reps to get the power spectrum, transfer function, and growth functions needed to generate the ICs

- Run N-GenIC_growth to generate the ICs of the simulations together with the value of the initial amplitudes and phases

- Run Gadget-III in the desired mode; e.g. no tree for neutrinos down to z=10