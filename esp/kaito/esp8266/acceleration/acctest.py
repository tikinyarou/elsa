import mpu6050
import machine,time
i2c = machine.I2C(scl=machine.Pin(23), sda=machine.Pin(22))
mpu = mpu6050.accel(i2c)
#for i in range(100):
data = mpu.get_values()
print(data.vals["Tmp"])
