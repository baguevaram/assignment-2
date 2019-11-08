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
    
    def  instalacionPiezas(self):
        print('instalando piezas...')
    
    def pintura(self):
        print('pintura....')
        
    def chasisCarroceria(self):
        print('ensambe del chasis y la carroceria...')
class Ford:

    motor = None

    def setMotor(self, motor):
        self.motor = motor

    def aceleracion(self,presion):
        if not self.motor is None:
            self.motor.setPresion(presion)
            velocidad = self.motor.getVelocidad()
        return velocidad

class VehiculoFactory:
    def construirVehiculo(self, tipoVehiculo):
        vehiculo = Vehiculo()
        if(tipoVehiculo == 'Ford'):
            print('Soy ford')
        elif(tipoVehiculo == 'Hyundai'):
            print('Soy Hyundai')
        motor = Motor()
        vehiculo.setMotor(motor)
        vehiculo.instalacionPiezas()
        vehiculo.pintura()
        vehiculo.chasisCarroceria()
        return vehiculo;

vF = VehiculoFactory()

v1 = vF.construirVehiculo('Ford')
v2 = vF.construirVehiculo('Hyundai')
v3 = vF.construirVehiculo('Ford')

print(v1.aceleracion(5))
print(v2.aceleracion(7))
print(v3.aceleracion(10))
