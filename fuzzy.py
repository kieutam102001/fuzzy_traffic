import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


emv_waiting_time_green_lane = ctrl.Antecedent(np.arange(0, 17, 1), 'emv_waiting_time_green_lane')
emv_waiting_time_red_lane = ctrl.Antecedent(np.arange(0, 17, 1), 'emv_waiting_time_red_lane')

traffic_light_signal = ctrl.Consequent(np.arange(0, 10, 1), 'traffic_light_signal')



# waiting_time_current_lane.view()

emv_waiting_time_green_lane['rat it'] = fuzz.trimf(emv_waiting_time_green_lane.universe, [0, 0, 2])
emv_waiting_time_green_lane['it'] = fuzz.trimf(emv_waiting_time_green_lane.universe, [0, 2, 4])
emv_waiting_time_green_lane['binh thuong'] = fuzz.trimf(emv_waiting_time_green_lane.universe, [2, 4, 6])
emv_waiting_time_green_lane['nhieu'] = fuzz.trapmf(emv_waiting_time_green_lane.universe, [4, 6, 8,8])
# emv_waiting_time_green_lane.view()

emv_waiting_time_red_lane['rat it'] = fuzz.trimf(emv_waiting_time_red_lane.universe, [0, 0, 2])
emv_waiting_time_red_lane['it'] = fuzz.trimf(emv_waiting_time_red_lane.universe, [0, 2, 4])
emv_waiting_time_red_lane['binh thuong'] = fuzz.trimf(emv_waiting_time_red_lane.universe, [2,4, 6])
emv_waiting_time_red_lane['nhieu'] = fuzz.trapmf(emv_waiting_time_red_lane.universe, [4, 6, 8,8])
# emv_waiting_time_red_lane.view()


traffic_light_signal['khong keo dai'] = fuzz.trimf(traffic_light_signal.universe, [0, 0, 2])
traffic_light_signal['ngan'] = fuzz.trimf(traffic_light_signal.universe, [0, 2, 4])
traffic_light_signal['trung binh'] = fuzz.trimf(traffic_light_signal.universe, [2, 4, 6])
traffic_light_signal['dai'] = fuzz.trimf(traffic_light_signal.universe, [4, 6, 8])
# traffic_light_signal.view()

##### FUNCTIONS THAT PASSS IN THE INPUT ####
### no_vehicle_current_lane too-small small much  too-much

rule1 = ctrl.Rule(emv_waiting_time_green_lane['rat it'] ,
                   traffic_light_signal['khong keo dai'])

rule2 = ctrl.Rule(emv_waiting_time_green_lane['it'] & emv_waiting_time_red_lane['rat it']
                   | emv_waiting_time_green_lane['it'] & emv_waiting_time_red_lane['it'],
                   traffic_light_signal['ngan'])

rule3 = ctrl.Rule(emv_waiting_time_green_lane['it'] & emv_waiting_time_red_lane['binh thuong']
                   | emv_waiting_time_green_lane['it'] & emv_waiting_time_red_lane['nhieu'],
                   traffic_light_signal['khong keo dai'])

rule4 = ctrl.Rule(emv_waiting_time_green_lane['binh thuong'] & emv_waiting_time_red_lane['rat it']
                   | emv_waiting_time_green_lane['binh thuong'] & emv_waiting_time_red_lane['it'],
                   traffic_light_signal['trung binh'])

rule5 = ctrl.Rule(emv_waiting_time_green_lane['binh thuong'] & emv_waiting_time_red_lane['binh thuong']
                   | emv_waiting_time_green_lane['binh thuong'] & emv_waiting_time_red_lane['nhieu'],
                   traffic_light_signal['ngan'])

rule6 = ctrl.Rule(emv_waiting_time_green_lane['nhieu'] & emv_waiting_time_red_lane['rat it'],
                   traffic_light_signal['dai'])

rule7 = ctrl.Rule(emv_waiting_time_green_lane['nhieu'] & emv_waiting_time_red_lane['it']
                   | emv_waiting_time_green_lane['nhieu'] & emv_waiting_time_red_lane['binh thuong'],
                   traffic_light_signal['trung binh'])

rule8 = ctrl.Rule(emv_waiting_time_green_lane['nhieu'] & emv_waiting_time_red_lane['nhieu'],
                   traffic_light_signal['ngan'])


traffic_light_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
traffic_status = ctrl.ControlSystemSimulation(traffic_light_ctrl)

def fuzzy_controller_function(emv_waiting_time_green_lanes,emv_waiting_time_red_lanes):



    traffic_status.input['emv_waiting_time_red_lane'] = int(emv_waiting_time_red_lanes)
    traffic_status.input['emv_waiting_time_green_lane'] = int(emv_waiting_time_green_lanes)



    print('Xe dang den o den xanh ' + str(emv_waiting_time_green_lanes))
    print('Xe dang doi o den do ' + str(emv_waiting_time_red_lanes))


    traffic_status.compute()
    output = traffic_status.output['traffic_light_signal']
    return round(output)

print(fuzzy_controller_function(1,1))