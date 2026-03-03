numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers = numbers[0:4] + numbers[5:]

# TODO заменить значение пропущенного элемента средним арифметическим
arithmetic_mean = sum(numbers) / (len(numbers) + 1)
new_list = [arithmetic_mean]
new_numbers = numbers[0:4] + new_list + numbers[4:]


print("Измененный список:", new_numbers)
