import wpilib
import ctre

class S_1:
    def __init__(self, robot, ):
        self.robot = robot

        self.has_crossed_line = False
        self.has_turned       = False
        self.has_arrived      = False
        self.has_shot         = False
        self.inicial_state = self.robot.right_drivetrain_motor.getSelectedSensorPosition()
        self.shot_pos = 0
        self.turning_timestamp = 0
        self.exit_timestamp    = 0
        self.goal = (4159*2)
        self.exit_goal = -1*(4159*4)



    def drive(self):
        #una vuelta equivale a 4159
        #una vuelta 47.87cm

        if not self.has_arrived:
            if self.robot.right_drivetrain_motor.getSelectedSensorPosition() - self.inicial_state < (self.goal - 100):
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.navx, .6)

            if self.robot.right_drivetrain_motor.getSelectedSensorPosition() - self.inicial_state > (self.goal + 100):
                self.has_arrived = True
                self.robot.drivetrain.stop()
                self.turning_timestamp = self.robot.auto_timer.getFPGATimestamp()
                self.shot_pos = self.robot.right_drivetrain_motor.getSelectedSensorPosition()



        elif self.has_arrived == True:
            if wpilib.Timer.getFPGATimestamp() < self.turning_timestamp + 2:
                self.robot.box_lift_motor.set(.6)

            elif wpilib.Timer.getFPGATimestamp() > self.turning_timestamp +2 and  wpilib.Timer.getFPGATimestamp() < (self.turning_timestamp + 4) :
                self.robot.intake_motor.set(-.8)

            elif wpilib.Timer.getFPGATimestamp() > self.turning_timestamp + 4:
                self.robot.box_lift_motor.set(0)
                self.robot.intake_motor.set(0)
                self.has_shot = True
                self.exit_timestamp = self.robot.auto_timer.getFPGATimestamp()

        elif self.has_shot == True:
            wpilib.SmartDashboard.putBoolean(keyName="has_shoot", value=self.has_shot)

            if wpilib.Timer.getFPGATimestamp() < self.exit_timestamp + 15:
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.navx, -.6)

            elif wpilib.Timer.getFPGATimestamp() > self.exit_timestamp + 15:
                self.robot.drivetrain.stop()





















