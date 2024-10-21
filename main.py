import matplotlib.pyplot as plt
import numpy as np
import glsPlanner as gls

# Define the parameters to vary
mirror_areas = np.arange(0.5, 5, 0.1)
number_of_years = np.arange(0.5, 5, 0.1)
laser_efficiencies = np.arange(0.08, 0.25, 0.01)
payload_powers = np.arange(240, 5000, 100)  # Adjusted step size

y_mirrors = []
y_years = []
y_laser = []
y_payload = []

# Define the figure and axes for 4 plots
fig, axs = plt.subplots(2, 2)

# Iterate over the parameter combinations
for mirror_area in mirror_areas:
    # Calculate the number of satellites required for global coverage
    num_satellites_output_mirror = gls.runGLS(
        A=mirror_area,  # Mirror Area m2
        Le=0.08,  # Laser Efficiency fractional percentage
        Q=0.45,  # Detector Efficiency Fractional percentage
        Edet=0.562 * 10**-15,  # Energy Detected per shot
        Ppay=240,  # Payload Power W
        cFrac=0.55,  # Average Cloud cover fractional percentage
        obsProb=0.8,  # Desired Probability of Cloud Free observation, fractional percentage
        tRes=1,  # Time to global coverage in years
        lat=0,  # Latitude, default 0 degs
        samp=1,  # Spatial Sampling Density? default 1
        Psigma=5,  # Pulse width in m, default 5
        optEff=1.0,  # Optical efficiency, default 1
        pointErr=0.0,  # Pointing error in deg, default 0
        res=30,  # Ground resolution m
        h=400000,  # Satellite Altitude m
        dutyCyc=1.0,
        unAmbigR=150,
    )
    y_mirrors.append(num_satellites_output_mirror.nSat)

for years_amount in number_of_years:
    num_satellites_output_years = gls.runGLS(
        A=0.5,
        Le=0.08,
        Q=0.45,
        Edet=0.562 * 10**-15,
        Ppay=240,
        cFrac=0.55,
        obsProb=0.8,
        tRes=years_amount,
        lat=0,
        samp=1,
        Psigma=5,
        optEff=1.0,
        pointErr=0.0,
        res=30,
        h=400000,
        dutyCyc=1.0,
        unAmbigR=150,
    )
    y_years.append(num_satellites_output_years.nSat)

for laser_eff in laser_efficiencies:
    num_satellites_output_eff = gls.runGLS(
        A=0.5,
        Le=laser_eff,
        Q=0.45,
        Edet=0.562 * 10**-15,
        Ppay=240,
        cFrac=0.55,
        obsProb=0.8,
        tRes=5,
        lat=0,
        samp=1,
        Psigma=5,
        optEff=1.0,
        pointErr=0.0,
        res=30,
        h=400000,
        dutyCyc=1.0,
        unAmbigR=150,
    )
    y_laser.append(num_satellites_output_eff.nSat)

for payload_power in payload_powers:
    num_satellites_output_power = gls.runGLS(
        A=0.5,
        Le=0.08,
        Q=0.45,
        Edet=0.562 * 10**-15,
        Ppay=payload_power,
        cFrac=0.55,
        obsProb=0.8,
        tRes=5,
        lat=0,
        samp=1,
        Psigma=5,
        optEff=1.0,
        pointErr=0.0,
        res=30,
        h=400000,
        dutyCyc=1.0,
        unAmbigR=150,
    )
    y_payload.append(num_satellites_output_power.nSat)

# Plot results
axs[0, 0].plot(mirror_areas, y_mirrors)
axs[0, 0].set_title("Mirror Area")
axs[0, 0].set_xlabel("Mirror Area (m²)")
axs[0, 0].set_ylabel("Satellites Needed")

axs[0, 1].plot(number_of_years, y_years)
axs[0, 1].set_title("Years")
axs[0, 1].set_xlabel("Years")
axs[0, 1].set_ylabel("Satellites Needed")

axs[1, 0].plot(laser_efficiencies, y_laser)
axs[1, 0].set_title("Laser Efficiency")
axs[1, 0].set_xlabel("Laser Efficiency")
axs[1, 0].set_ylabel("Satellites Needed")

axs[1, 1].plot(payload_powers, y_payload)
axs[1, 1].set_title("Payload Power")
axs[1, 1].set_xlabel("Payload Power (W)")
axs[1, 1].set_ylabel("Satellites Needed")

plt.show()

# print(y_laser)
# print(y_mirrors)
# print(y_payload)
# print(y_years)
