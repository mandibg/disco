
from sense_hat import *
from time import sleep

from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

sense = SenseHat()

while True:
    e = sense.stick.wait_for_event()
    if e.direction == DIRECTION_UP:
        synth = ':blade'
    elif e.direction == DIRECTION_DOWN:
        synth = ':cnoise'
    elif e.direction == DIRECTION_LEFT:
        synth = ':dsaw'
    else: 
        synth = ':chipbass'
    
    data = sense.get_orientation()
    yaw = data['yaw']
    roll = data['roll']
#   pitch = data['pitch']    
     
    note = round(yaw - 50)
 #   print (note)
    tempo1 = round(roll)
    if 0 <= tempo1 <= 25:
        tempo = 0.2
    elif 25 < tempo1 <= 50:
        tempo = 0.4
    elif 50 < tempo1 <= 100:
        tempo = 0.6
    elif 100 < tempo1 <= 125:
        tempo = 0.8     
    elif 125 < tempo1 <= 150:
        tempo = 1
    elif 150 < tempo1 <= 175:
        tempo = 1.2 
    elif 175 < tempo1 <= 200:
        tempo = 1.4  
    elif 200 < tempo1 <= 225:
        tempo = 1.6
    elif 225 < tempo1 <= 250:
        tempo = 1.8     
    elif 275 < tempo1 <= 300:
        tempo = 2
    elif 300 < tempo1 <= 325:
        tempo = 2.2 
    elif 325 < tempo1 <= 350:
        tempo = 2.4    
    else:
        tempo = 3
        
    print (tempo)
    sender.send_message('/play_this', (note,tempo,synth))
    sleep(0.1)
        
    