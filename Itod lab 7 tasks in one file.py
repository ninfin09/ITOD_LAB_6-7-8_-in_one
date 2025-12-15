#TASK1
list1 = ['rap', 'house', 'electronic music', 'rap']
set1 = set(list1)
print(f"Початковий список: {list1}")
print(f"Отримана множина: {set1}")



#TASK2
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])

sum_A = sum(A)
sum_B = sum(B)

print(f"Сума списку A ({A}): {sum_A}")
print(f"Множина B ({B}): {sum_B}")
print(f"Чи sum(A) = sum(B)? {sum_A == sum_B}")




#TASK3
list2 = ['A', 'B', 'C', 'A', 'B', 'C']
set2 = set(list2)
print(f"Початковий список: {list2}")
print(f"Отримана множина: {set2}")



#TASK4
S = {'A', 'B', 'C'}
S.add('D')
print(f"Множина S після додавання 'D': {S}")



#TASK5
A = {1, 2, 3, 4, 5}
B = {1, 3, 9, 12}
intersection = A.intersection(B)
print(f"Перетин A та B: {intersection}")




#TASK6
album_set1 = set(["Thriller", "AC/DC", "Back in Black"])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print(f"Множина album_set3 (об'єднання): {album_set3}")




#TASK7
is_subset = album_set1.issubset(album_set3)
print(f"Чи є album_set1 підмножиною album_set3? {is_subset}")



#TASK8
D = {'a': '0', 'b': '1', 'c': '2'}
print(f"Словник D: {D}")



#TASK9
value_a = D['a']
print(f"Значення за ключем 'a': {value_a}")




#TASK10
keys_D = D.keys()
print(f"Ключі словника D: {keys_D}")




#TASK11
soundtrack_dic = {"The Bodyguard": "1992", "Saturday Night Fever": "1977"}
print(f"Словник soundtrack_dic: {soundtrack_dic}")




#TASK12
keys_soundtrack = soundtrack_dic.keys()
print(f"Ключі словника soundtrack_dic: {keys_soundtrack}")



#TASK13
values_soundtrack = soundtrack_dic.values()
print(f"Значення словника soundtrack_dic: {values_soundtrack}")





#TASK14
album_sales_dict = {
    "Back in Black": 50,
    "The Bodyguard": 50,
    "Thriller": 65
}
print(f"Словник album_sales_dict: {album_sales_dict}")




#TASK15
sales_thriller = album_sales_dict["Thriller"]
print(f"Загальний обсяг продажів Thriller: {sales_thriller} мільйонів")




#TASK16
album_names = album_sales_dict.keys()
print(f"Імена альбомів: {album_names}")



#TASK17
album_sales = album_sales_dict.values()
print(f"Обсяги продажів: {album_sales}")






