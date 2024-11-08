h = 4.136E-15  # Planck's constant in eV*s
m = 511000 / (2*10**8)**2 # Electron mass in eV/c^2

def compute_energy(name, length_x, length_y, n_x, n_y):
    energy = (h**2 / (8 * m)) * (n_x**2 / length_x**2 + n_y**2 / length_y**2)
    return energy

def compute_energies(name, length_x, length_y, pi_bonds):
    energies = []

    for n_x in range(1, pi_bonds + 2):  # from 1 to pi_bonds + 1
        for n_y in range(1, pi_bonds + 2):  # from 1 to pi_bonds + 1
            energy = compute_energy(name, length_x, length_y, n_x, n_y)
            energies.append({'nX': n_x, 'nY': n_y, 'E': energy})

    # Sort energies by increasing energy:
    energies.sort(key=lambda x: x['E'])

    # Only include the energy levels up to the number of pi bonds plus one for LUMO:
    energies = energies[:pi_bonds + 1]

    # Print the energies:
    print(f"Energies for {name}:")
    for index, energy in enumerate(energies):
        homo_lumo = ""
        if index == len(energies) - 2:
            homo_lumo = ' (HOMO)'
        elif index == len(energies) - 1:
            homo_lumo = ' (LUMO)'

        print(f"nX={energy['nX']}, nY={energy['nY']}, E = {energy['E']:.6e} eV{homo_lumo}")


# Constants for lengths:
l_x = 0.242E-9  # Length in the X direction (m)
l_y = 0.28E-9   # Length in the Y direction (m)

compute_energies("Napthalene", l_x * 2, l_y, 5)
print("\n")
compute_energies("Anthracene", l_x * 3, l_y, 7)
print("\n")
compute_energies("Tetracene", l_x * 4, l_y, 9)