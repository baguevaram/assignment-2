class Motor:
    presion = 0
    torque = 5
    def setPresion(self,presion):
        self.presion = presion
    def getVelocidad(self):
        return self.presion*self.torque


class Vehiculo:
    motor = None

    def transporta(self):
        """ este metodo se debe redefinir """
        pass

    def setMotor(self, motor):
        self.motor = motor

    def aceleracion(self, presion):
        if not self.motor is None:
            self.motor.setPresion(presion)
            velocidad = self.motor.getVelocidad()
        return velocidad


class Bus (Vehiculo):

    def transporta(self):
        return "Transporta personas"


class Camion(Vehiculo):

    def transporta(self):
        return "Transporta carga o mercancias"


class VehiculoFactory:
    def construirVehiculo(self, tipoCarga):
        if "Personas" == tipoCarga:
            vehiculo = Bus()
        elif "Carga" == tipoCarga:
            vehiculo = Camion()
        else:
            vehiculo = Vehiculo()
        motor = Motor()
        vehiculo.setMotor(motor)
        return vehiculo;

vF = VehiculoFactory()

v1 = vF.construirVehiculo("Personas")
v2 = vF.construirVehiculo("Carga")
v3 = vF.construirVehiculo("Otros")

print(v1.aceleracion(5))
print(v1.transporta())
print(v2.aceleracion(7))
print(v2.transporta())
print(v3.aceleracion(10))
print(v3.transporta())
