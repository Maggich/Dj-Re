class Vehicle:
    vehicles_created = 0
    
    def __init__(self, brand, max_speed):
        self.brand = brand
        self._max_speed = max_speed
        self._mileage = 0
        Vehicle.vehicles_created += 1
        
    def get_max_speed(self):
        return self._max_speed

    def get_mileage(self):
        return self._mileage
    
    def drive(self, distance):
        self._mileage += distance
    
    def display_info(self):
        return f"Марка: {self.brand} Макс. скорость: {self.get_max_speed()} км/ч Пробег: {self.get_mileage()} км"


class Car(Vehicle):
    def __init__(self, brand, max_speed, engine_type):
        super().__init__(brand, max_speed)
        self.engine_type = engine_type
       
    def display_info(self):
        return f"{super().display_info()} Тип двигателя: {self.engine_type}"


class Bicycle(Vehicle):
    def __init__(self, brand, max_speed, frame_material):
        super().__init__(brand, max_speed)
        self.frame_material = frame_material
        
    def display_info(self):
        return f"{super().display_info()} Материал рамы: {self.frame_material}"


# 👇 ВАЖНО: оборачиваем запуск
if __name__ == "__main__":
    tesla = Car("Tesla", 250, "Электро")
    bmw = Car("BMW", 280, "Бензин")
    trek = Bicycle("Trek", 40, "Карбон")

    vehicles = [tesla, bmw, trek]

    for vehicle in vehicles:
        print("---")
        print(vehicle.display_info())
        vehicle.drive(100)
        print(f"Пробег после поездки: {vehicle.get_mileage()} км")

    print("\n" + "=" * 30)
    print(f"Всего создано транспортных средств: {Vehicle.vehicles_created}")