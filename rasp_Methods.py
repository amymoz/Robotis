def map(x,in_min,in_max,out_min,out_max):
    return (x - in_min)/(in_max-in_min)*(out_max-out_min)+out_min

def set_servo(pin,degree):
    degree2 = map(degree,-90,90,2.5,11) # 90 is 0 front
    GPIO.setup(pin, GPIO.OUT)
    pwm_servo = GPIO.PWM(pin, 50)
    pwm_servo.start(2.5)
    pwm_servo.ChangeDutyCycle(degree2)
    sleep(0.2)
    GPIO.cleanup([pin])
    return degree
