import cv2

#from time import sleep
#import RPi.GPIO as GPIO

#def map(x,in_min,in_max,out_min,out_max):
#    return (x - in_min)/(in_max-in_min)*(out_max-out_min)+out_min

#def set_servo(pin,degree):
#    if degree < -90:
#        degree = -90
#    elif degree > 90:
#        degree = 90
#    degree2 = map(degree,-90,90,2.5,11) # 90 is 0 front
#    GPIO.setup(pin, GPIO.OUT)
#    pwm_servo = GPIO.PWM(pin, 50)
#    pwm_servo.start(2.5)
#    pwm_servo.ChangeDutyCycle(degree2)
#    sleep(0.2)
#    GPIO.cleanup([pin])
#    return degree

#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
#servo_x,servo_y = 12,35
#x_pos = set_servo(servo_x,0)
#y_pos = set_servo(servo_y,-35)

cap = cv2.VideoCapture(0)
frame = cap.read()[1]
xframe, yframe =  len(frame[0]), len(frame)
xcenter,ycenter = xframe // 2 , yframe // 2


