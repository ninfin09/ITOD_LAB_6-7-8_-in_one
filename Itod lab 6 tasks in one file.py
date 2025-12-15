A = (0, 1, 2, 3)
print(f"1. Кортеж A: {A}")


first_two_A = A[0:2]
print(f"2. Перші два елементи кортежу A: {first_two_A}")


genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")
print(f"3. Кортеж genres_tuple: {genres_tuple}")


length_genres = len(genres_tuple)
print(f"4. Довжина кортежу genres_tuple: {length_genres}")


element_at_index_3 = genres_tuple[3]
print(f"5. Елемент за індексом 3: {element_at_index_3}")


new_tuple_slice = genres_tuple[3:6]
print(f"6. Новий кортеж з індексів 3, 4, 5: {new_tuple_slice}")


first_two_genres = genres_tuple[:2]
print(f"7. Перші два елементи genres_tuple: {first_two_genres}")


index_disco = genres_tuple.index("disco")
print(f"8. Індекс елементу 'disco': {index_disco}")


C_tuple = (-5, 1, -3)
sorted_list = sorted(list(C_tuple))
print(f"9. Відсортований список: {sorted_list}")


a_list = [1, "hello", [1, 2, 3], True]
print(f"10. Список a_list: {a_list}")


value_at_index_1 = a_list[1]
print(f"11. Значення за індексом 1 в a_list: {value_at_index_1}")


slice_a_list = a_list[1:4]
print(f"12. Елементи за індексами 1, 2, 3: {slice_a_list}")


A_list = [1, "a"]
B_list = [2, 1, "d"]
combined_list = A_list + B_list
print(f"13. Об'єднаний список: {combined_list}")


B = ["a", "b", "c"]
print(f"14. Список B: {B}")


first_two_B = B[0:2]
print(f"15. Перші два елементи списку B: {first_two_B}")


B[0] = "A"
print(f"16. Список B після зміни першого елемента: {B}")


