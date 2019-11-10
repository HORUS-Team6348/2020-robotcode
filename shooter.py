import wpilib
import ctre

class Shooter:
    def __init__(self, intake_motor: wpilib.PWMSpeedController, left_shooter: ctre.WPI_TalonSRX, right_shooter: ctre.WPI_TalonSRX):
        self.intake_motor  = intake_motor
        self.left_shooter  = left_shooter
        self.right_shooter = right_shooter

        self.left_shooter.setInverted(True)

        self.right_shooter.configVoltageCompSaturation(10.0, 0)
        self.right_shooter.enableVoltageCompensation(True)
        self.right_shooter.configVoltageMeasurementFilter(32, 0)

        self.left_shooter.configVoltageCompSaturation(10.0, 0)
        self.left_shooter.enableVoltageCompensation(True)
        self.left_shooter.configVoltageMeasurementFilter(32, 0)


    
    def shoot(self, stick: wpilib.Joystick):
        if stick.getPOV() == 180:
            self.left_shooter.set(ctre.ControlMode.PercentOutput, -0.6) #rocket bajo
            self.right_shooter.set(ctre.ControlMode.PercentOutput, -0.6)

            self.intake_motor.set(-0.6)

        elif stick.getPOV() == 0:
            self.left_shooter.set(ctre.ControlMode.PercentOutput, -0.4) #rocket bajo
            self.right_shooter.set(ctre.ControlMode.PercentOutput, -0.4)

            self.intake_motor.set(-0.6)

        elif stick.getRawAxis(2) > 0.50: #intake main
            self.intake_motor.set(-0.8)

            self.left_shooter.set(ctre.ControlMode.PercentOutput, -0.3)
            self.right_shooter.set(ctre.ControlMode.PercentOutput, -0.3)

        elif stick.getRawButton(5) or stick.getRawButton(6): #regresar pelota
            self.intake_motor.set(0.4)

            self.left_shooter.set(ctre.ControlMode.PercentOutput, 0.4)
            self.right_shooter.set(ctre.ControlMode.PercentOutput, 0.4)

        else: #nada presionado
            self.left_shooter.set(ctre.ControlMode.PercentOutput, 0)
            self.right_shooter.set(ctre.ControlMode.PercentOutput, 0)
            self.intake_motor.set(0)
            
