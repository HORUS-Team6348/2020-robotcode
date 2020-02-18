import wpilib
import ctre

class Arm:
    def __init__(self, arm: ctre.WPI_TalonSRX):
        self.arm = arm
        self.GoalIsEvaluated = False
        self.goal = 0



    def ControlPosition(self, stick:wpilib.Joystick):
        if stick.getRawButton(4) == True:
            if self.GoalIsEvaluated == False:
                self.goal = (self.arm.getSelectedSensorPosition() + (4161*11))
                self.GoalIsEvaluated = True

            elif self.GoalIsEvaluated == True:
                if self.arm.getSelectedSensorPosition() < (self.goal -100):
                    self.arm.set(ctre.ControlMode.PercentOutput, .4)
                if self.arm.getSelectedSensorPosition() > self.goal:
                    self.arm.set(ctre.ControlMode.PercentOutput, 0)
                    self.GoalIsEvaluated = False




            wpilib.SmartDashboard.putNumber(keyName="goal", value=self.goal)
            wpilib.SmartDashboard.putBoolean(keyName="GoalIsEvaluated", value=self.GoalIsEvaluated)





