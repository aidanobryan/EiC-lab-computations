import matplotlib.pyplot as plt
import numpy as np

# Environment variables:
NAPTHALENE_FILE_PREFIX = "Wyatt_Ryan_Aidan_Naph_Absorbance__"
ANTHRACENE_FILE_PREFIX = "Wyatt_Ryan_Aidan_Anth_Absorbance__"
TETRACENE_FILE_PREFIX = "Wyatt_Ryan_Aidan_Tetra_Absorbance__"

"""
molecules = (
    ["Napthalene", NAPTHALENE_FILE_PREFIX, [250, 300], [-1, 2]],
    ["Anthracene", ANTHRACENE_FILE_PREFIX, [290, 410], [0, 2]],
    ["Tetracene", TETRACENE_FILE_PREFIX, [320, 500], [0, 2]]
)
"""

molecules = (
    ["Napthalene", NAPTHALENE_FILE_PREFIX, [250, 300], [-1, 2], 5],
    ["Anthracene", ANTHRACENE_FILE_PREFIX, [290, 400], [-1, 2], 10],
    ["Tetracene", TETRACENE_FILE_PREFIX, [340, 500], [-1, 2], 15]
)

# Iterate through each molecule:
for molecule in molecules:
    print("Absorption Spectra for " + molecule[0])

    # All data points for each molecule:
    xWavelengths = []
    yAbsorption = []

    # Iterate through each of the 10 recordings made:
    for i in range(10):
        filePath = "absorption-spectra-data/" + molecule[1] + str(i) + ".txt"

        file = open(filePath, "r")
        arr = file.readlines()

        delimiterFound = False

        for line in arr:
            if line == ">>>>>Begin Spectral Data<<<<<\n":
                delimiterFound = True
                continue

            if not delimiterFound:
                continue

            subArr = line.split("\t")
            xWavelengths.append(float(subArr[0]))
            yAbsorption.append(float(subArr[1].strip()))

    plt.plot(xWavelengths, yAbsorption, ".")

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Absorbance (AU)')
    plt.title(molecule[0] + " Absorption Spectra")
    plt.xticks(np.arange(0, max(xWavelengths) + 5, step=molecule[4]))
    plt.xlim(molecule[2][0], molecule[2][1])
    plt.ylim(molecule[3][0], molecule[3][1])

    plt.show()