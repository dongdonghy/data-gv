#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
import numpy as np
import matplotlib.pyplot as plt

# init data viriables
vib_num = 100
voi_num = 200
vib_std = [i for i in range(vib_num)]
voi_std = [i for i in range(voi_num)]
vib_real = [i for i in range(vib_num)]
voi_real = [i for i in range(voi_num)]
flag_vib_std = 0
flag_voi_std = 0
flag_screw = 0
vib_std[0] = 150.0
flag_motor_power = 0
for i in range(1, vib_num):
    if i%2 == 0:
        vib_std[i] = vib_std[i-2] + (np.random.randint(-1, 1)+0.5)/abs(np.random.randint(-1, 1)+0.5)*np.random.uniform(5, 15)
        if vib_std[i] > 200 :
            vib_std[i] = np.random.uniform(190, 200)
        if vib_std[i] < 110 :
            vib_std[i] = np.random.uniform(110, 120)
    else:
        vib_std[i] = vib_std[i-1] - np.random.uniform(8, 18)
    vib_real[i] = vib_std[i] + np.random.uniform(2, 8)

def get_voi_std(i):
    if i % 20 == 0:
        result = np.random.uniform(3, 4)
    if i % 20 == 1:
        result = np.random.uniform(-0.3, 0.3)
    if i % 20 == 2:
        result = np.random.uniform(0, 0.2)
    if i % 20 == 3:
        result = np.random.uniform(0, 0.1)
    if i % 20 == 4:
        result = np.random.uniform(0, 0.4)
    if i % 20 == 5:
        result = np.random.uniform(-0.4, -0.1)
    if i % 20 == 6:
        result = np.random.uniform(-0.2, -0.1)
    if i % 20 == 7:
        result = np.random.uniform(-1.5, -1)
    if i % 20 == 8:
        result = np.random.uniform(0.4, 0.7)
    if i % 20 == 9:
        result = np.random.uniform(0, 0.1)
    if i % 20 == 10:
        result = np.random.uniform(-0.8, -0.6)
    if i % 20 == 11:
        result = np.random.uniform(-1, -0.8)
    if i % 20 == 12:
        result = np.random.uniform(-0.5, -0.3)
    if i % 20 == 13:
        result = np.random.uniform(0.2, 0.4)
    if i % 20 == 14:
        result = np.random.uniform(0.1, 0.2)
    if i % 20 == 15:
        result = np.random.uniform(0.8, 1)
    if i % 20 == 16:
        result = np.random.uniform(0.4, 0.6)
    if i % 20 == 17:
        result = np.random.uniform(-0.1, 0.1)
    if i % 20 == 18:
        result = np.random.uniform(-0.5, -0.2)
    if i % 20 == 19:
        result = np.random.uniform(-1.5, -1)
    return result
    
for i in range(0, voi_num):
    voi_std[i] = get_voi_std(i)
    voi_real[i] = voi_std[i] + np.random.uniform(0.3, 0.7)
   
def data_handler(flag):
    global vib_std, flag_vib_std, voi_std, flag_voi_std, flag_screw, flag_motor_power
    if flag == 'vibration_std':
        for i in range(vib_num-1):
            vib_std[i] = vib_std[i+1]
        if flag_vib_std == 0:
            vib_std[vib_num-1] = vib_std[vib_num-3] + (np.random.randint(-1, 1)+0.5)/abs(np.random.randint(-1, 1)+0.5)*np.random.uniform(5, 15)
            if vib_std[vib_num-1] > 200 :
                vib_std[vib_num-1] = np.random.uniform(190, 200)
            if vib_std[vib_num-1] < 110 :
                vib_std[vib_num-1] = np.random.uniform(110, 120)
            flag_vib_std = 1
        else:
            vib_std[vib_num-1] = vib_std[vib_num-2] - np.random.uniform(8, 18)
            flag_vib_std = 0
        return vib_std      

    if flag == 'vibration_real':
        for i in range(vib_num-1):
            vib_real[i] = vib_real[i+1]
        vib_real[vib_num-1] = vib_std[vib_num-1] + np.random.uniform(2, 8)
        return vib_real

    if flag == 'voice_std':
        for i in range(voi_num-1):
            voi_std[i] = voi_std[i+1]
        voi_std[voi_num-1] = get_voi_std(flag_voi_std)
        flag_voi_std = (flag_voi_std+1) % 20
        return voi_std

    if flag == 'voice_real':
        for i in range(voi_num-1):
            voi_real[i] = voi_real[i+1]
        voi_real[voi_num-1] = voi_std[vib_num-1] + np.random.uniform(0.3, 0.7)
        return voi_real

    if flag == 'screw_accuracy':
        if flag_screw < 2000:
            flag_screw+=1  
        if flag_screw < 100 :
            return 0.998
        elif flag_screw < 500 :
            return 0.997
        elif flag_screw < 1000 :
            return 0.996
        else :
            return 0.995

    if flag == 'motor_temperature':
        return 63.0 + round(np.random.uniform(-1, 1), 2)

    if flag == 'motor_power':
        flag_motor_power+=1
        if flag_motor_power>2000:
            flag_motor_power = 0
        if flag_motor_power < 800:
            return (740+np.random.randint(-200, 200))/100
        elif flag_motor_power < 1200:
            return (480+np.random.randint(-200, 200))/100
        elif flag_motor_power < 1700:
            return 8-(flag_motor_power-1200)/500*5
        else:
            return (480+np.random.randint(-200, 200))/100

    if flag == 'env_temp':
        return 23.32 + np.random.randint(-10, 10)/100

    if flag == 'env_humidity':
        return 37.55 + np.random.randint(-10, 10)/100

    if flag == 'env_noise':
        return 78 + np.random.randint(-300, 300)/100

    if flag == 'env_powered':
        return 821.35 + np.random.randint(-400, 400)/100

if __name__ == '__main__':
 
    plt.ion()    
    while(1):
        result_vib_std = data_handler('vibration_std')
        result_vib_real = data_handler('vibration_real')
        result_voi_std = data_handler('voice_std')
        result_voi_real = data_handler('voice_real')
        result_screw_accuracy = data_handler('screw_accuracy')
        result_motor_temperature = data_handler('motor_temperature')
        result_motor_power = data_handler('motor_power')
        result_env_temp = data_handler('env_temp')
        result_env_humidity = data_handler('env_humidity')
        result_env_noise = data_handler('env_noise')
        result_env_powered = data_handler('env_powered')

#visualization
        plt.clf()
        plt.title('voice and vibration data') 
        plt.axis([0, voi_num, -3, 5])
        plt.plot([i for i in range(len(result_vib_std))], result_vib_std, marker='.', mec='b')
        plt.plot([i+0.5 for i in range(len(result_vib_real))], result_vib_real, marker='*', mec='r')
        plt.plot([i for i in range(len(result_voi_std))], result_voi_std, marker='.', mec='r')
        plt.plot([i+0.5 for i in range(len(result_voi_real))], result_voi_real, marker='*', mec='b')
        plt.pause(0.05)   
    





