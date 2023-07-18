import gpiozero
import time

robot = gpiozero.Robot(left=(17,18), right=(27,22))

for i in range(4):
    robot.forward()
    time.sleep(3)
    robot.stop()
    time.sleep(5)
    robot.left()
    time.sleep(3)