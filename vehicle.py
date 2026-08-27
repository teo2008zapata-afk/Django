class Vehicle:
    def __init__(self, brand, color, plate):
        self.brand = brand
        self.color = color
        self.plate = plate
        self.speed = 0
        self.brake = 0
        
    def acelerar (self):
        self.speed += 10
        print(f"El{self.brand} acelero a {self.speed} km/h")
        
    def desacelerar(self):
        self.brake -= 10
        print(f"El {self.brand} desacelero a {self.brake} km/h")
        
#creacion de los objetos:
my_vehicle = Vehicle("Ford", "Plateado", "ABC123")
my_vehicle.acelerar()
my_vehicle.desacelerar()
my_vehicle.desacelerar()

#agrgar el atributo plate
#agregar metodo desacelerar
#subir a git