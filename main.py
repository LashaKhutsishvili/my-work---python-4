from model.car import Car

car1 = Car("Mercedes", "cls", "2013", "black", 400, False)

print(car1.get_horse_power())
print(car1.increase_horse_power(77))

print(car1.get_color())
print(car1.change_color("brown"))
