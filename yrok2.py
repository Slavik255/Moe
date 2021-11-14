# Классы и экземпляры

class Car():
    """Класс по созданию автомобиля"""
    def __init__(self, make,model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading =  0
    def description_name(self):
        """Возвращаем описание автомобиля"""
        desc = str(self.year) + " " + self.make + " " + self.model
        return desc.title()
    def read_odometer(self):
        """Ввыодим пробег авто"""
        print("Пробег этого авто " + str(self.odometr_reading) + " км")
    def update_odometer(self, km):
        """Устанавливаем значение на одометре"""
        if km >= self.odometr_reading:
            self.odometr_reading = km
        else:
            print("Не стоит с этим баловаться")
    def increment_odometr(self, km):
        """Увеличиваем показания одометра на заданную величину"""
        self.odometr_reading += km

# car1 = Car("audi", "a4", 2017)
# #car1.odometr_reading = 30  - Пример
# car1.update_odometer(33)
# car1.increment_odometr(150)
# car1.read_odometer()


# Наследие
class Battery():
    """Простая модель аккамулятора для электромобиля"""

    def __init__(self, battery=100):
        self.battery = battery
    def description_battery(self):
        """Вывыодит информацию о мощности батареи"""
        print("Этот автомобиль имеет мощность " + str(self.battery) + " Киловат")


class ElectricCar(Car):
    """Аспекты для электроавтомобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов класса родителя"""
        super().__init__(make, model, year)
        self.battery = Battery
    def description_name(self):
        """Переопределение родительского метода"""
        desc = str(self.year) + " " + self.model
        return desc.title()

tesla = ElectricCar("tesla", "s", 2017)




