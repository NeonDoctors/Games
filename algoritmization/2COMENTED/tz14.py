# Задание
# Напишите программу по следующему условию:
# Есть список из N количества символов, необходимо циклом вывести квадраты всех значений, индекс которых является четным. 

LIST = [1, 2, 3, 4, 5] # Список N с рандомными цифрами

for INDEX in range(0, len(LIST)): # Цикл который проверяет все числа листа
	if INDEX % 2 == 0: # Логика, котрая проверяет четность
		ELEMENT = LIST[INDEX] # Находим по ЧЕТНОМУ индексу элементы
		print(ELEMENT * ELEMENT) # Выводим в консоль квадрат числа