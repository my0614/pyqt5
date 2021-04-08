from serbot import degrees, collisonDetect
from pop import Pilot
import random
import time

current_direction = 0
flag = True
while flag:
    try:
        if collisonDetect(300)[current_direction]:  
            bot.stop()
            continue
        detect = collisonDetect(800)
        if sum(detect) == 8:
            bot.stop()
            continue
        if detect[current_direction]:
            while True:
                #idx = random.randint(0, 7) 랜덤생성
                num1 = random.sample(range(0,9),1)[0]
                if idx != current_direction and detect[idx] == 0:
                    current_direction = idx
                    break
        bot.move(degrees[current_direction], 50)
        print(detect)
    except:
        flag = False
lidar.stopMotor()
bot.stop()