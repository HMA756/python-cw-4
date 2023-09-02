def my_function():
    print('my name is Hoor')

my_function()

def my_meal(food, drink):
    print (f'i like to eat {food} while drinking {drink}')
my_meal('machbous')

def cube(number):
    return number**3

print(cube(3))

def by_three(number):
    if number%3==0:
        return cube(number)
    else: return False

print(by_three(9))
