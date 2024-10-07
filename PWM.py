import RPi.GPIO as GPIO
import tkinter as tk

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the LEDs
RED_PIN = 11
GREEN_PIN = 13
BLUE_PIN = 15

# Set up the GPIO pins as outputs and initialize PWM
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Set PWM frequency to 1000 Hz
red_pwm = GPIO.PWM(RED_PIN, 100)
green_pwm = GPIO.PWM(GREEN_PIN, 100)
blue_pwm = GPIO.PWM(BLUE_PIN, 100)

# Start PWM with 0% duty cycle (LEDs off)
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

# Function to update the PWM duty cycle based on slider value
def update_red(val):
    red_pwm.ChangeDutyCycle(int(val))

def update_green(val):
    green_pwm.ChangeDutyCycle(int(val))

def update_blue(val):
    blue_pwm.ChangeDutyCycle(int(val))

# Function to clean up GPIO and close the application
def close_application():
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()
    app.quit()

# Create the main application window
app = tk.Tk()
app.title("LED Intensity Controller")

# Create and pack the widgets
tk.Label(app, text="Red LED Intensity", font=("Arial", 12)).pack(pady=5)
red_slider = tk.Scale(app, from_=0, to=100, orient=tk.HORIZONTAL, command=update_red)
red_slider.pack(pady=5)

tk.Label(app, text="Green LED Intensity", font=("Arial", 12)).pack(pady=5)
green_slider = tk.Scale(app, from_=0, to=100, orient=tk.HORIZONTAL, command=update_green)
green_slider.pack(pady=5)

tk.Label(app, text="Blue LED Intensity", font=("Arial", 12)).pack(pady=5)
blue_slider = tk.Scale(app, from_=0, to=100, orient=tk.HORIZONTAL, command=update_blue)
blue_slider.pack(pady=5)

tk.Button(app, text="Exit", command=close_application).pack(pady=20)

# Start the Tkinter event loop
app.mainloop()
