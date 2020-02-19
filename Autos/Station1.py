import wpilib
import ctre

class S_1:
    def __init__(self, robot, ):
        self.robot = robot

        self.has_crossed_line = False
        self.has_arrived      = False
        self.has_shot         = False

    def drive(self):
        #una vuelta equivale a 4159
        #una vuelta 47.87cm
        self.goal = (self.robot.left_drivetrain_encoder + (4159*4.))

        if not self.has_crossed_line:
            if self.robot.left_drivetrain_encoder < (self.goal- 100):
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.gyro, .4)

            if self.robot.left_drivetrain_encoder > (self.goal + 100):
                self.has_crossed_line = True
                self.robot.drivetrain.stop()

        wpilib.SmartDashboard.putNumber(keyName="auto goal", value= self.goal)
        wpilib.SmartDashboard.putNumber(keyName="auto encoder", value= self.robot.left_drivetrain_encoder)







