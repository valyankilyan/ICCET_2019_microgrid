from smbus2 import SMBus, i2c_msg
import time

address = 16

with SMBus(1) as bus:
    # Read 64 bytes from address 80
    msg = i2c_msg.read(address, 64)
    bus.i2c_rdwr(msg)

    time.sleep(3)
    # Write some bytes to address 80
    msg = i2c_msg.write(address, [65, 66, 67, 68])
    bus.i2c_rdwr(msg)	