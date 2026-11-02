from machine import Pin, I2C
import time
from micropython_lsm6dsox.lsm6dsox import LSM6DSOX
from bmp280 import BMP280

# Initialize I2C (Pins GP8=SDA, GP9=SCL)
i2c_l = I2C(1, scl=Pin(19), sda=Pin(18))

# Initialize the LSM6DSOX sensor
sensor_l = LSM6DSOX(i2c_l)

# Initialize I2C
I2C_SCL = Pin(17)  # Adjust based on your wiring
I2C_SDA = Pin(16)  # Adjust based on your wiring
i2c_b = I2C(0, scl=I2C_SCL, sda=I2C_SDA, freq=100000)

#Initialises bmp280 sensor
sensor_b = BMP280(i2c_b)

while True:
    # Read acceleration (x, y, z) in m/s^2
    accel_x, accel_y, accel_z = sensor_l.acceleration
    accel_x = (accel_x -0.60) #account for zero error   
    accel_y = (accel_y +0.27) #account for zero error   
    accel_z = -1*(accel_z -9.94) #account for zero error
    print(f"Acceleration - X: {accel_x:.2f}, Y: {accel_y:.2f}, Z: {accel_z:.2f} m/s²")

    # Read gyroscope (x, y, z) in degrees per second (dps)
    gyro_x, gyro_y, gyro_z = sensor_l.gyro
    print(f"Gyroscope - X: {gyro_x:.2f}, Y: {gyro_y:.2f}, Z: {gyro_z:.2f} dps")
    
    #Reads temp and pressure from bmp280
    temperature = sensor_b.temperature
    pressure = sensor_b.pressure
    print(f"Temperature: {temperature:.2f} °C, Pressure: {pressure:.2f} hPa")

    print("-" * 40)
    time.sleep(0.5)  # Delay for readability
