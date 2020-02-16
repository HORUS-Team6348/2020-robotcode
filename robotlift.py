import wpilib
import ctre
import rev

class RLift:
    def __init__(self, elevator_motor: wpilib.PWMSpeedController, main_lift: rev.CANSparkMax):
        self.elevator_motor = elevator_motor
        self. main_lift     = main_lift

    def HookElevator(self, stick:wpilib.Joystick):
        trigger = stick.getRawAxis(2)
        stick = stick.getRawAxis(1)
        self.elevator_motor.set((stick * trigger) * .5)

    def Climb(self, stick:wpilib.Joystick):
        if stick.getRawButton(9) == True:
            self.main_lift.set(-.7)
        elif stick.getRawButton(7) == True:
            self.main_lift.set(.7)
        else:
            self.main_lift.set(0)


