import numpy as np
from matplotlib import pyplot as plt

def init_spin_array(rows, cols):
    return np.ones((rows, cols))

def find_neighbors(spin_array, lattice, x, y):
    top   = (x, (y - 1)%lattice)
    bottom  = (x, (y + 1) % lattice)
    left    = ((x - 1)%lattice, y)
    right = ((x + 1) % lattice, y)

    return [spin_array[top[0], top[1]],
            spin_array[bottom[0], bottom[1]],
            spin_array[left[0], left[1]],
            spin_array[right[0], right[1]]]

def energy(spin_array, lattice, x ,y):
    return 2 * spin_array[x, y] * sum(find_neighbors(spin_array, lattice, x, y))

RELAX_SWEEPS = int(input('RELAX_SWEEPS = '))
lattice = int(input('lattice = '))
sweeps = int(input('sweeps = '))
Temp_array = []
Mag_array = []
Interval_temp = np.arange(0.1, 4.1, 0.1)
for temperature in(Interval_temp):
    spin_array = init_spin_array(lattice, lattice)
    mag = np.zeros(sweeps + RELAX_SWEEPS)
    for sweep in range(sweeps + RELAX_SWEEPS):
        for i in range(lattice):
            for j in range(lattice):
                e = energy(spin_array, lattice, i, j)
                if e <= 0:
                    spin_array[i, j] *= -1
                elif np.exp((-1*e)/temperature) > np.random.rand():
                    spin_array[i, j] *= -1
        mag[sweep] = abs(sum(sum(spin_array))) / (lattice ** 2)
    x = (temperature)
    y = (sum(mag[RELAX_SWEEPS:]/sweeps))
    print(f'Temp = {x:.2f},  Mag = {y:.4f}')
    Temp_array.append(x)
    Mag_array.append(y)
plt.xlim(1.,4.)
plt.ylim(0.,1.)
plt.xlabel('Temperature')
plt.ylabel('Magnetizaton')
plt.title('2D Ising Model')
plt.plot(Temp_array, Mag_array, 'r', linestyle = '-', linewidth = 1.0)
plt.show()
