#TASK1
A = [1, 2, 3, 4, 5]

print("Елементи списку A (цикл for):")
for element in A:
    print(element)

print("\nЕлементи списку A (цикл while):")
i = 0
while i < len(A):
    print(A[i])
    i = i + 1





#TASK2
x = 11
y = 1
while(y < x):
    print(y)
    y = y + 1
    



#TASK3
print("Елементи між -5 і 5 (виключаючи 5):")
for num in range(-5, 5):
    print(num)




#TASK4
squares = ['red', 'yellow', 'green', 'purple', 'blue']
print("Елементи списку squares:")
for color in squares:
    print(color)



#TASK5
squares = ['orange', 'orange', 'purple', 'blue', 'orange']
new_squares = []

i = 0
while i < len(squares):
    if squares[i] == 'orange':
        new_squares.append(squares[i])
    else:
        break
    i = i + 1

print("\n--- Варіант з використанням break ---")
print("Оригінальний список squares:", squares)
print("Новий список new_squares:", new_squares)



#TASK6
def f(a,b):
    return a * b 

a = 4
b = 2 

if a * b == f(a,b):
    print("correct")
else:
    print("incorrect")




#TASK7
class Car(object):
    def __init__(self, make, model, color):
        self.make = make 
        self.model = model
        self.color = color
        self.owner_number = 0

    def car_info(self): 
        print("make: ", self.make)
        print("model:", self.model)
        print("color:", self.color)
        print("number of owners:", self.owner_number)

    def sell(self):
        self.owner_number = self.owner_number + 1




#TASK8
my_car = Car("BMW", "M3", "red")


#TASK9
print("\n--- Інформація про my_car (початкова) ---")
my_car.car_info()


#TASK10
for i in range(5):
    my_car.sell()

print("\n--- Інформація про my_car (після 5 продажів) ---")
my_car.car_info()