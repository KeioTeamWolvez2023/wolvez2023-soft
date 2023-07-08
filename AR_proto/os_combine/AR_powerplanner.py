import numpy as np


def AR_powerplanner(ar_info:dict={"1":{"x":0, "y":3, "z":5} ,"2":{"x":1, "y":0, "z":7} ,"3":{"x":0, "y":0, "z":0}}) -> dict:
    
    # 速度の設定
    STANDARD_POWER = 60
    POWER_RANGE = 10
    aprc_state = False

    marker_1 = np.array([ar_info["1"]["x"],ar_info["1"]["y"],ar_info["1"]["z"]])
    marker_2 = np.array([ar_info["2"]["x"],ar_info["2"]["y"],ar_info["2"]["z"]])
    vec, distance = __targetting(marker_1,marker_2)
    #print(distance,vec[0])
    if distance > -0.03:
        if distance > 0.15:
            '''
            接近するまでは連続的に近づく(アームとモジュールが横並びするまで？)
            '''
            #print(f"distance:{distance}")
            print(f"vec:{vec[0]}")
            if vec[0] < 0.1:
                power_R = int(STANDARD_POWER )
                power_L = int(0)
            else:
                power_R = int(0)
                power_L = int(STANDARD_POWER )
        elif distance > 0.02:
            if vec[0] < 0.02:
                power_R = int(STANDARD_POWER-POWER_RANGE )
                power_L = int(0)
            else:
                power_R = int(0)
                power_L = int(STANDARD_POWER-POWER_RANGE )
        else:
            '''
            接近後なのでアーム動かしたい：要検討
            '''
            print("finish")
            power_R = 0
            power_L = 0
            aprc_state = True

    else:
        '''
        distanceが負のときバックする？iranaikamo
        '''
        print("distance<0")
        power_R = int(-1*STANDARD_POWER)
        power_L = int(-1*STANDARD_POWER)
    
    return {"R":power_R,"L":power_L,"aprc_state":aprc_state}


### module nomi kara sansyutu
def AR_powerplanner_single(ar_info:dict={"1":{"x":0, "y":3, "z":5} ,"2":{"x":1, "y":0, "z":7} ,"3":{"x":0, "y":0, "z":0}}) -> dict:
    
    # 速度の設定
    STANDARD_POWER = 60
    POWER_RANGE = 10
    aprc_state = False

    marker_1_kasou = np.array([0.069,0.028,0.144]) ### arm wo suihei ni sita toki no daitai no iti
    marker_3 = np.array([ar_info["3"]["x"],ar_info["3"]["y"],ar_info["3"]["z"]])
    vec, distance = __targetting(marker_1_kasou,marker_3)
    #print(distance,vec[0])
    if distance > -0.03:
        if distance > 0.15:
            '''
            接近するまでは連続的に近づく(アームとモジュールが横並びするまで？)
            '''
            #print(f"distance:{distance}")
            print(f"vec:{vec[0]}")
            if vec[0] < 0.1:
                power_R = int(STANDARD_POWER )
                power_L = int(0)
            else:
                power_R = int(0)
                power_L = int(STANDARD_POWER )
        elif distance > 0.02:
            if vec[0] < 0.02:
                power_R = int(STANDARD_POWER-POWER_RANGE )
                power_L = int(0)
            else:
                power_R = int(0)
                power_L = int(STANDARD_POWER-POWER_RANGE )
        else:
            '''
            接近後なのでアーム動かしたい：要検討
            '''
            print("finish")
            power_R = 0
            power_L = 0
            aprc_state = True

    else:
        '''
        distanceが負のときバックする？iranaikamo
        '''
        print("distance<0")
        power_R = int(-1*STANDARD_POWER)
        power_L = int(-1*STANDARD_POWER)
    
    return {"R":power_R,"L":power_L,"aprc_state":aprc_state}

def __targetting(marker_1:np.ndarray=np.zeros(3), marker_2:np.ndarray=np.zeros(3)):
    '''
    二つのベクトルの差分と閾値に対する評価を出力
    '''
    target_vec = marker_2 - marker_1
    #print(target_vec)
    distance = (target_vec[2]/abs(target_vec[2]))*(target_vec[0]**2 + target_vec[2]**2)**0.5 
    return target_vec, distance

#print(AR_powerplanner())
