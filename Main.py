class Motor:
    presion = 0
    torque = 5
    def setPresion(self,presion):
        self.presion = presion
    def getVelocidad(self):
        return self.presion*self.torque

class Vehiculo:

    motor = None

    def setMotor(self, motor):
        self.motor = motor

    def aceleracion(self,presion):
        if not self.motor is None:
            self.motor.setPresion(presion)
            velocidad = self.motor.getVelocidad()
        return velocidad

class VehiculoFactory:
    def construirVehiculo(self):
        vehiculo = Vehiculo()
        motor = Motor()
        vehiculo.setMotor(motor)
        return vehiculo;

vF = VehiculoFactory()

v1 = vF.construirVehiculo()
v2 = vF.construirVehiculo()
v3 = vF.construirVehiculo()

print(v1.aceleracion(5))
print(v2.aceleracion(7))
print(v3.aceleracion(10))
