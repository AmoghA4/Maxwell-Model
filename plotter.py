import numpy as np
import matplotlib.pyplot as plt

def plot_lissajous_from_file(filename):
    # load data from file
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    
    # extract columns: stress, strain, strain rate
    stress = data[:, 0]
    strain = data[:, 1]
    strain_rate = data[:, 2]
    
    # plot Stress vs. Strain Lissajous figure
    plt.figure()
    plt.subplot(1,2,1)
    plt.plot(strain, stress, 'b', linewidth=2)
    plt.xlabel('Strain γ')
    plt.ylabel('Stress σ')
    plt.title('Stress-Strain Response')
    plt.grid()
    
    # plot Stress vs. Strain Rate Lissajous figure
    plt.subplot(1,2,2)
    plt.plot(strain_rate, stress, 'r', linewidth=2)
    plt.xlabel('Strain Rate γ̇')
    plt.ylabel('Stress σ')
    plt.title('Stress-Strain Rate Response')
    plt.grid()
    
    plt.show()

if __name__ == "__main__":
    filename = "data.csv"  # replace with actual file path
    plot_lissajous_from_file(filename)