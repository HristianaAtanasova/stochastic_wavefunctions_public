#!/usr/bin/env python
import numpy as np
import stochastic_propagation_Nd
import pickle
import sys

if __name__ == '__main__':
    sys.path.insert(0, '')
    from params_Nd import *

    # Neural network propagation
    t = np.linspace(0, tmax, n_t) * -1j
    nn_fitter = stochastic_propagation_Nd.get_neural_fitting_method(bosonic, U, n_particles, dim_physical, n_layers,
                                                                layer_size, epochs,
                                                                batch_size, reg)
    x_t_nn, psi_t_nn, energies_t_nn, mse_t_nn = stochastic_propagation_Nd.propagate_in_time(
        eval_psi0_sample, eval_V, eval_I, load_weights, U, n_particles, dim_physical, nsamples, t, m, hbar, xmax, n_x, step_size, x0, decorrelation_steps, uniform_ratio, nn_fitter, normalize, eta, calculate_energy, bosonic)

    # File output
    results = {
        'x' : x_t_nn,
        't' : t,
        'psi_t' : psi_t_nn,
        'energies_t' : energies_t_nn,
	'mse_t' : mse_t_nn,
    }
    if bosonic:
        output =  "cutoff_{}_neural_{}_{}d_{}N_U={}.pkl".format(cutoff, 'bosons', dim_physical, n_particles, U)
        pickle.dump(results, open( output, "wb" ))
    else:
        output =  "cutoff_{}_neural_{}_{}d_{}N_U={}.pkl".format(cutoff, 'fermions', dim_physical, n_particles, U)
        pickle.dump(results, open( output, "wb" ))
