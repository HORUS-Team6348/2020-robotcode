import wpilib
import ctre

class S_1:
    def __init__(self, robot, ):
        self.robot = robot

        self.has_crossed_line = False
        self.has_arrived      = False
        self.has_shot         = False
        self.inicial_state = self.robot.left_drivetrain_motor.getSelectedSensorPosition()
        self.goal = -1*(4159*2)



    def drive(self):
        #una vuelta equivale a 4159
        #una vuelta 47.87cm

        if not self.has_crossed_line:
            if self.robot.left_drivetrain_motor.getSelectedSensorPosition() - self.inicial_state > (self.goal- 100):
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.navx, .4)

            if self.robot.left_drivetrain_motor.getSelectedSensorPosition() -self.inicial_state < (self.goal + 100):
                self.has_crossed_line = True

        elif self.has_crossed_line == True:
            self.robot.drivetrain.turn_with_pid(self.robot.navx, )


        wpilib.SmartDashboard.putNumber(keyName="autogoal", value= self.goal)







