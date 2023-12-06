from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2016)
my_tesla = ElectricCar('tesla', 'model y', 2020)

print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())

