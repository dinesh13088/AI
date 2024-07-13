import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np

# Define the input and output variables
traffic_density = ctrl.Antecedent(np.arange(0, 101, 1), 'traffic_density')
time_of_day = ctrl.Antecedent(np.arange(0, 24, 1), 'time_of_day')
signal_duration = ctrl.Consequent(np.arange(0, 121, 1), 'signal_duration')

# Define fuzzy membership functions for traffic_density
traffic_density['low'] = fuzz.trimf(traffic_density.universe, [0, 0, 50])
traffic_density['medium'] = fuzz.trimf(traffic_density.universe, [30, 50, 70])
traffic_density['high'] = fuzz.trimf(traffic_density.universe, [60, 100, 100])

# Define fuzzy membership functions for time_of_day
time_of_day['morning'] = fuzz.trimf(time_of_day.universe, [0, 6, 12])
time_of_day['afternoon'] = fuzz.trimf(time_of_day.universe, [10, 14, 18])
time_of_day['evening'] = fuzz.trimf(time_of_day.universe, [16, 20, 24])

# Define fuzzy membership functions for signal_duration
signal_duration['short'] = fuzz.trimf(signal_duration.universe, [0, 0, 60])
signal_duration['medium'] = fuzz.trimf(signal_duration.universe, [40, 60, 80])
signal_duration['long'] = fuzz.trimf(signal_duration.universe, [70, 120, 120])

# Define the rules
rule1 = ctrl.Rule(traffic_density['low'] & time_of_day['morning'], signal_duration['short'])
rule2 = ctrl.Rule(traffic_density['low'] & time_of_day['afternoon'], signal_duration['short'])
rule3 = ctrl.Rule(traffic_density['low'] & time_of_day['evening'], signal_duration['short'])
rule4 = ctrl.Rule(traffic_density['medium'] & time_of_day['morning'], signal_duration['medium'])
rule5 = ctrl.Rule(traffic_density['medium'] & time_of_day['afternoon'], signal_duration['medium'])
rule6 = ctrl.Rule(traffic_density['medium'] & time_of_day['evening'], signal_duration['medium'])
rule7 = ctrl.Rule(traffic_density['high'] & time_of_day['morning'], signal_duration['long'])
rule8 = ctrl.Rule(traffic_density['high'] & time_of_day['afternoon'], signal_duration['long'])
rule9 = ctrl.Rule(traffic_density['high'] & time_of_day['evening'], signal_duration['long'])
rule10 = ctrl.Rule(traffic_density['medium'] & time_of_day['evening'], signal_duration['medium'])

# Create the control system
signal_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])
signal = ctrl.ControlSystemSimulation(signal_ctrl)

# Pass inputs to the system
signal.input['traffic_density'] = 60
signal.input['time_of_day'] = 17

# Compute the result
signal.compute()

print(f"Signal Duration: {signal.output['signal_duration']:.2f} seconds")
signal_duration.view(sim=signal)