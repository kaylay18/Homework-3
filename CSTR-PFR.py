import streamlit as st
import numpy as np

# Function to calculate solute distribution between two phases (based on distribution ratio)
def calculate_volumeCSTR(F_ao, X, k, C_ao):
    V_CSTR = (F_ao * X) / ((k * C_ao)*(1 - X))
    return V_CSTR
def calculate_volumePFR(F_ao, X, k, C_ao):
    V_PFR = (F_ao/(k * C_ao)) * np.log(1/(1 - X))
    return V_PFR
# Streamlit app interface
st.title("CSTR versus PFR Performance")

# Input section for solute concentration in aqueous phase and distribution ratio
st.header("Input Data for CSTR and PFR performance")
F_ao = st.number_input("Molar flow rate of reactant A at the inlet (mol/s)", value=10.0, min_value=0.0, max_value=None, step=None)
X = st.number_input("Conversion of reaction (fraction between 0 and 1)", value=0.8, min_value=0.0, max_value=1.0, step=None)
k = st.number_input("rate constant (1/s)", value=1.0, min_value=0.0, max_value=None, step=None)
C_ao = st.number_input("Initial concentration of reactant A (mol/L)", value=2.0, min_value=0.0, max_value=None, step=None)

st.write(f"The volume for a CSTR is calculated to be: {calculate_volumeCSTR(F_ao, X, k, C_ao): .2f} L")
st.write(f"The volume for a PFR is calculated to be: {calculate_volumePFR(F_ao, X, k, C_ao): .2f} L")
st.write(f"To achieve a conversion of {X * 100}%, {calculate_volumeCSTR(F_ao, X, k, C_ao): .2f} L is required for a CSTR and {calculate_volumePFR(F_ao, X, k, C_ao): .2f} L is required for a PFR.")

st.header("Input Data for CSTR and PFR Conversion Profiles")

def PFR_conversion(V, F_ao, k, C_ao):
    """Calculates conversion in a PFR."""
    return 1 - np.exp(-k * V / F_ao)

def CSTR_conversion(V, F_ao, k, C_ao):
    """Calculates conversion in a CSTR."""
    return k * V * C_ao / (F_ao + k * V * C_ao)

L = st.number_input("Reactor length (m)", value=10.0)
A = st.number_input("Reactor cross-sectional area (m^2)", value=1.0)

# Calculate reactor volume
V_max = L * A

# PFR conversion profile
Volume_PFR = np.linspace(0, V_max, 100)
X_PFR = PFR_conversion(Volume_PFR, F_ao, k, C_ao)

# CSTR conversion as a function of volume
Volume_CSTR = np.linspace(0, V_max, 100)
X_CSTR = CSTR_conversion(Volume_CSTR, F_ao, k, C_ao)

import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# PFR plot
ax1.plot(Volume_PFR / L, X_PFR)
ax1.set_xlabel('Relative Length (V / L)')
ax1.set_ylabel('Conversion (X)')
ax1.set_title('Conversion Profile in a PFR')

st.pyplot(fig1)

# CSTR plot
ax2.plot(Volume_CSTR, X_CSTR)
ax2.set_xlabel('Reactor Volume (V)')
ax2.set_ylabel('Conversion (X)')
ax2.set_title('Conversion vs. Reactor Volume in a CSTR')

st.pyplot(fig2)