# Homework-3
This repository includes four apps including a CSTR-PRF modeling app, distillation app, liquid-liquid extraction app, and and OTR app that can be run through streamlit cloud. 
## CSTR-PFR
Chemical reactors are central to chemical engineering processes, where chemical reactions occur under controlled conditions. This app is used for designing an isothermal Continuous Stirred Tank Reactor (CSTR) and a Plug Flow Reactor (PFR) for a first-order irreversible reaction. This app calculates the reactor volume required to achieve a specified conversion and compare the performance of CSTR and PFR reactors. The app calculates the reactor volume (V) for both CSTR and PFR given the feed rate, rate constant, and target conversion, compares the performance of CSTR and PFR, showing the volume required to achieve the same conversion in both reactors and plots the conversion profile for a PFR along the reactor length and the conversion as a function of reactor volume for the CSTR while allowing the user to input reaction rate constants, flow rates, and initial concentrations, and dynamically adjust the conversion and reactor volumes. (https://ky-cstr-pfr.streamlit.app/)

## Distillation
Distillation is a key separation technique used in chemical engineering to separate liquid mixtures based on differences in their volatilities. This app acts as a calculator for the design and performance evaluation of a distillation column. This app calculates the number of theoretical stages required for separating a binary mixture given the feed composition, reflux ratio, and product specifications using the McCabe-Thiele method and plot the corresponding equilibrium curve and operating lines (rectifying and stripping sections) on an x-y diagram, showing the relationship between the liquid and vapor compositions in the distillation column. (https://ky-distillation.streamlit.app/)

## Liquid-liquid extraction
Liquid – Liquid extraction is useful in the separation of compounds based on their different solubilities in two immiscible liquids. This app acts as a calculator for a liquid-liquid extraction process, which is a common separation technique in chemical engineering. The app calculates the equilibrium compositions of two immiscible phases and plot the distribution curve (also known as the tie-line diagram) for a ternary liquid-liquid system. The app calculates the distribution ratio (D) of a solute between two immiscible solvents, uses a distribution curve to visualize the relationship between the solute concentration in the two phases and plots a tie-line diagram, showing the equilibrium compositions in both phases across different initial solute concentrations. (https://ky-lle.streamlit.app/)

## OTR
In wastewater treatment, oxygen is supplied to support biological processes in an aeration tank. The oxygen transfer rate (OTR) is crucial for maintaining sufficient dissolved oxygen (DO) levels to meet biological oxygen demand (BOD). This app is used for calculating the oxygen transfer rate (OTR) in an aeration tank, which involves iteratively calculating the dissolved oxygen (DO) levels based on oxygen transfer and consumption rates. This app simulates the dissolved oxygen (DO) profile over time in the aeration tank, iteratively calculate DO levels using the oxygen transfer and consumption rates and allows users to adjust parameters such as oxygen transfer efficiency (OTE), oxygen consumption rate, and initial DO.	This app also outputs a plot of the DO concentration over time. (https://ky-otr.streamlit.app/)
