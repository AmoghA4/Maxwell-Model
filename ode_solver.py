import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def nonlinear_maxwell_solver():
    # time span for the solution
    tspan = (0, 10)
    t_eval = np.linspace(0, 10, 500)

    # initial conditions
    gamma0 = 0  # assuming system had 0 memory of strain
    sigma0 = 0  # assuming system had 0 memory of stress
    y0 = [gamma0, sigma0]

    # solve the ODE
    sol = solve_ivp(maxwell_ode, tspan, y0, t_eval=t_eval)

    # find the strain and strain rate
    A = 5   # max strain
    omega = 2 * np.pi  # frequency of driver
    gamma = A * np.sin(omega * sol.t)  # assuming the driver has sinusoidal perturbations
    gamma_dot = A * omega * np.cos(omega * sol.t)  # strain rate

    # Extract stress from solution
    sigma = sol.y[1]

    # plot!!!!!!!!
    plt.figure(figsize=(12, 4))

    # stress strain plot
    plt.subplot(1, 3, 1)
    plt.plot(gamma, sigma, 'b', linewidth=2)
    plt.xlabel('Strain γ')
    plt.ylabel('Stress σ')
    plt.title('Stress-Strain Response')
    plt.grid()

    # stress strain-rate plot
    plt.subplot(1, 3, 2)
    plt.plot(gamma_dot, sigma, 'r', linewidth=2)
    plt.xlabel('Strain Rate γ̇')
    plt.ylabel('Stress σ')
    plt.title('Stress-Strain Rate Response')
    plt.grid()

    # strain strain-rate plot
    plt.subplot(1, 3, 3)
    plt.plot(gamma, gamma_dot, 'g', linewidth=2)
    plt.xlabel('Strain γ')
    plt.ylabel('Strain Rate γ̇')
    plt.title('Strain vs Strain Rate')
    plt.grid()

    plt.show()

def maxwell_ode(t, y):
    # parameters
    eta = 1  # viscosity of pot
    E = 1  # elastic modulus of  spring

    # Extract strain and stress
    sigma = y[1]


    A = 5  # amplitude
    omega = 2 * np.pi  # frequ
    gamma_dot = A * omega * np.cos(omega * t)

    # nonlinear stress response
    gamma = A * np.sin(omega * t)
    sigma_nl = E * gamma + 0.1 * gamma**3 - 0.01 * gamma**5

    # maxwell equation modified for nonlinearity
    sigma_dot = (sigma_nl - sigma) / eta + gamma_dot * E

    return [gamma_dot, sigma_dot]

if __name__ == "__main__":
    nonlinear_maxwell_solver()