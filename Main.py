class Motor:
    presion = 0
    torque = 5
    def setPresion(self,presion):
        self.presion = presion
    def getVelocidad(self):
        return self.presion*self.torque


class Vehiculo:
    motor = None
    marca = None

    def setMotor(self, motor):
        self.motor = motor
        
    def transporta(self):
        """ este metodo se debe redefinir """
        pass
    
    def setMarca(self, marca):
        self.marca = marca
        """ este metodo se debe redefinir """
        pass
    
    def getMarca(self):
        return self.marca

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
    
class Bus (Vehiculo):
    def transporta(self):
        return "Transporta personas"


class Camion(Vehiculo):
    def transporta(self):
        return "Transporta carga o mercancias"
    
class Ford(Vehiculo):
    def marca(self):
        return "Ford"

class Hyundai(Vehiculo):
    def marca(self):
        return "Hyundai"
    
class Mercedes(Vehiculo):
    def marca(self):
        return "Mercedes"


class Bus (Vehiculo):
    def transporta(self):
        return "Transporta personas"


class Camion(Vehiculo):
    def transporta(self):
        return "Transporta carga o mercancias"


class VehiculoFactory:
    def construirVehiculo(self, tipoCarga, tipoVehiculo):        
        if "Personas" == tipoCarga:
            vehiculo = Bus()
        elif "Carga" == tipoCarga:
            vehiculo = Camion()
        else:
            vehiculo = Vehiculo()
            
        if tipoVehiculo == 'Ford':
            vehiculo.setMarca('Ford')
        elif tipoVehiculo == 'Hyundai':
            vehiculo.setMarca('Hyundai')
        elif tipoVehiculo == 'Mercedes':
            vehiculo.setMarca('Mercedes')
        motor = Motor()
        vehiculo.setMotor(motor)
        #vehiculo.instalacionPiezas()
        #vehiculo.pintura()
        #vehiculo.chasisCarroceria()
        return vehiculo;

vF = VehiculoFactory()

v1 = vF.construirVehiculo("Personas",'Ford')
v2 = vF.construirVehiculo("Personas",'Hyundai')
v3 = vF.construirVehiculo("Carga",'Mercedes')

print(v1.aceleracion(5))
print(v1.transporta())
print(v1.getMarca())
print(v2.aceleracion(7))
print(v2.transporta())
print(v2.getMarca())
print(v3.aceleracion(10))
print(v3.transporta())
print(v3.getMarca())
