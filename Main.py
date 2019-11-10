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
    
    def marca(self, marca):
        """ este metodo se debe redefinir """
        pass

    def aceleracion(self, presion):
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

    def descipcion(self):
        return 'Soy un vehiculo'

    def pintar(self, color):
        anteriorDescripcion = self.descipcion
        def nuevaDescripcion():
            return anteriorDescripcion() + ", de color " + color
        self.descipcion = nuevaDescripcion

    def agregarPuertas(self, cantidad):
        anteriorDescripcion = self.descipcion
        def nuevaDescripcion():
            return anteriorDescripcion() + ", con " + str(cantidad) + " puertas"
        self.descipcion = nuevaDescripcion

    def establecerCapacidad(self, capacidad):
        anteriorDescripcion = self.descipcion
        def nuevaDescripcion():
            return anteriorDescripcion() + ", con capacidad para " + str(capacidad) + " personas"
        self.descipcion = nuevaDescripcion

    def elegirPlaca(self, placa):
        anteriorDescripcion = self.descipcion
        def nuevaDescripcion():
            return anteriorDescripcion() + ", con placa " + placa
        self.descipcion = nuevaDescripcion


class Ford(Vehiculo):
    def marca(self):
        return "Ford"

    def descipcion(self):
        return Vehiculo.descipcion(self) + " de marca Ford"


class Hyundai(Vehiculo):
    def marca(self):
        return "Hyundai"

    def descipcion(self):
        return Vehiculo.descipcion(self) + " de marca Hyundai"

class Mercedes(Vehiculo):
    def marca(self):
        return "Mercedes"

    def descipcion(self):
        return Vehiculo.descipcion(self) + " de marca Mercedes"

class VehiculoFactory:
    def construirVehiculo(self,tipoVehiculo):
        if tipoVehiculo == 'Ford':
            vehiculo = Ford()
        elif tipoVehiculo == 'Hyundai':
            vehiculo = Hyundai()
        elif tipoVehiculo == 'Mercedes':
            vehiculo = Mercedes()
        motor = Motor()
        vehiculo.setMotor(motor)
        return vehiculo


vF = VehiculoFactory()

v1 = vF.construirVehiculo('Ford')
v2 = vF.construirVehiculo('Hyundai')
v3 = vF.construirVehiculo('Mercedes')


print(v1.aceleracion(5))
print(v1.marca())
print(v2.aceleracion(7))
print(v2.marca())
print(v3.aceleracion(10))
print(v3.marca())

print(v1.descipcion())
v1.pintar('rojo')
v1.agregarPuertas(4)
v1.establecerCapacidad(6)
v1.elegirPlaca('GOD333')
print(v1.descipcion())
