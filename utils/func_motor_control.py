import RPi.GPIO as GPIO
import time
import threading

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for ULN2003AN
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

# Set all pins as output
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Define step sequence for the motor
step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

# Reverse step sequence for counter-clockwise rotation
reverse_step_sequence = step_sequence[::-1]

def set_step(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)

def rotate_clockwise(steps_per_revolution, delay):
    for _ in range(steps_per_revolution):
        for step in step_sequence:
            set_step(step[0], step[1], step[2], step[3])
            time.sleep(delay)

def rotate_counterclockwise(steps_per_revolution, delay):
    for _ in range(steps_per_revolution):
        for step in reverse_step_sequence:
            set_step(step[0], step[1], step[2], step[3])
            time.sleep(delay)

def cleanup_gpio():
    GPIO.cleanup()
