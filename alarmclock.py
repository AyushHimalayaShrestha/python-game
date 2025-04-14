import time
from playsound import playsound

def set_alarm():
    alarm_time =input("Enter time for alarm (in HH:MM:SS format)")
    print(f"Alarm set for {alarm_time}. Waiting... ")


    while True:
        current_time =time.strftime("%H:%M:%S")

        if current_time == alarm_time:
            print("Time's up! The alarm is ringing!")
            playsound('alarm_sound.mp3')
            break
        time.sleep(1)
set_alarm()