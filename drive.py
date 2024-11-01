from pybricks.hubs import ThisHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase


# Initialize the hub for sending and receiving.
hub = ThisHub(broadcast_channel=2, observe_channels=[1])

# Initialize the drive base.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
drive_base = DriveBase(
    left_motor, right_motor, wheel_diameter=56, axle_track=112
)


while True:
        drive_base.drive( 8,  3)

