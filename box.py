import wpilib
import ctre

class Box:
    def __init__(self, intake_motor: wpilib.PWMSpeedController, box_lift_motor: ctre.WPI_TalonSRX):
        self.intake_motor = intake_motor
        self.box_lift_motor = box_lift_motor


    def BallIntake (self, stick:wpilib.Joystick):
        if stick.getRawButton(1) == True:
            self.intake_motor.set(.8)

        elif stick.getRawButton(10) == True:
            self.intake_motor.set(-.8)

        else:
            self.intake_motor.set(0)

    def BoxLift(self, stick:wpilib.Joystick):
        trigger = stick.getRawAxis(3)
        stick   = stick.getRawAxis(5)
        self.box_lift_motor.set(ctre.ControlMode.Velocity, (stick*trigger)*6000)

