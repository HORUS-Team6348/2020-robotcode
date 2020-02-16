import wpilib
import ctre

class Arm:
    def __init__(self, arm: ctre.WPI_TalonSRX):
        self.arm = arm

    def ControlPosition(self, stick:wpilib.Joystick):
        if stick.getRawButton(4) == True:
            self.arm.set(ctre.ControlMode.Position, 4161)


