import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants
E = 1.0      
sigma = 0.5 

# Functional form for eta(x, dx/dt)
def eta(x, dxdt):
    return 1 + 0.1 * x + 0.1 * x**2 + 0.1 * x**3

# The system of ODEs
def system(t, yx):
    y, x, dxdt = yx
    
    # Calculate dy/dt from the given equation
    dydt = E * dxdt - (sigma * E / eta(x, dxdt))
    
    # dx/dt is just the velocity dxdt
    dxdt_new = dxdt 

    # Return derivatives
    return [dydt, dxdt, 0] 

# Initial conditions
y0 = 0 
x0 = 0 
dxdt0 = 1  

# Time span for the solution
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 100)

# Solve the system of ODEs
sol = solve_ivp(system, t_span, [y0, x0, dxdt0], t_eval=t_eval)

# Plot y vs. x (Lissajous figure)
plt.figure(figsize=(10, 6))
plt.plot(sol.y[1], sol.y[0], label="y(x)", color='blue')
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.title("Lissajous-like Plot: y(x)")
plt.grid(True)
plt.show()

# Plot y(t), x(t), and dx/dt(t)
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label="y(t)", color='red')
plt.plot(sol.t, sol.y[1], label="x(t)", color='green')
plt.plot(sol.t, sol.y[2], label="dx/dt (velocity)", color='orange')
plt.xlabel("Time (t)")
plt.ylabel("Values")
plt.legend()
plt.title("Solution of the Differential Equation")
plt.grid(True)
plt.show()