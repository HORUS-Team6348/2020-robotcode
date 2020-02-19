import wpilib

from Panel import Arm
from drivetrain import DriveTrain
from box import Box
from robotlift import RLift
import ctre
import rev
from  Autos.Station1 import S_1
import navx




class Robot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        self.driver_stick = wpilib.Joystick(0)
        self.codriver_stick = wpilib.Joystick(1)

        # Drivetrain Motors
        self.left_drivetrain_motor = ctre.WPI_TalonSRX(4)
        self.left_drivetrain_motor_2 = ctre.WPI_TalonSRX(3)

        self.right_drivetrain_motor = ctre.WPI_TalonSRX(6)
        self.right_drivetrain_motor_2 = ctre.WPI_TalonSRX(5)

        #Encoders

        self.left_drivetrain_encoder   = self.left_drivetrain_motor.getSelectedSensorPosition()
        self.right_drivetrain_encoder  = self.right_drivetrain_motor.getSelectedSensorPosition()

        # Box-mechanism Motors
        self.intake_motor = wpilib.Spark(8)
        self.box_lift_motor = ctre.WPI_TalonSRX(2)

        # Lift mechanism Motors
        self.elevator_motor = wpilib.Spark(9)
        self.main_lift      = rev.CANSparkMax(7, rev.MotorType.kBrushless)

        #ControlPanel objects
        self.arm = ctre.WPI_TalonSRX(1)

        self.arm.configSelectedFeedbackSensor(ctre.FeedbackDevice.CTRE_MagEncoder_Relative, 0, 0)
        self.arm.config_kP(0, (0.3 * 1023) / 4161 , 0)
        self.arm.config_kI(0, (0.5 * 1023) / (4161*30), 0)
        self.arm.config_kD(0, 30*(0.5 * 1023) / 4161, 0)
        self.arm.config_kF(0, 0, 0)


        self.timer = wpilib.Timer()

        self.duration = 20

        self.drivetrain   = DriveTrain(self.left_drivetrain_motor, self.left_drivetrain_motor_2, self.right_drivetrain_motor, self.right_drivetrain_motor_2)
        self.box          = Box(self.intake_motor,self.box_lift_motor)
        self.robotlift    = RLift(self.elevator_motor, self.main_lift)
        self.Panel        = Arm(self.arm)

        wpilib.SmartDashboard.putString(keyName="Robot_Station", value= "1")


        wpilib.CameraServer.launch()

        self.auto_timer = wpilib.Timer()
        self.navx       = navx.AHRS.create_spi()
        self.auto = 0


    def autonomousInit(self):
        self.auto_timer.start()
        self.gyro.reset()

        robot_position = wpilib.SmartDashboard.getString(keyName = "Robot position", defaultValue= "1")

        if robot_position[0].lower()    == "1":
            if __name__ == '__main__':
                self.auto = S_1(self)

        #elif robot_position[0].lower()  == "2":

        #elif robot_position[0].lower()  == "3":


    def autonomousPeriodic(self):
        self.auto.drive()
    def teleopInit(self):
        pass

    def teleopPeriodic(self):

        self.drivetrain.drive(self.driver_stick)
        self.box.BallIntake(self.codriver_stick)
        self.box.BoxLift(self.codriver_stick)
        self.robotlift.Climb(self.codriver_stick)
        self.robotlift.HookElevator(self.codriver_stick)
        self.Panel.ControlPosition(self.codriver_stick)
        wpilib.SmartDashboard.putNumber(keyName="encoder", value= self.arm.getSelectedSensorPosition())
        wpilib.SmartDashboard.putNumber(keyName= "Drivetrain_Encoder", value= self.left_drivetrain_motor.getSelectedSensorPosition())





if __name__ == "__main__":
    wpilib.run(Robot)