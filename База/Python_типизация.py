print('----------2. Виды типизаций----------')
print()
# В Python используется неявная типизация.

# Язык Python имеет сильную типизацию.

# В языке Python используется динамическая типизация,
# т.е. "тип переменной" (являющейся по сути ссылкой на объект)
# может меняться во время ее жизни.

# Т.е. не позволяет смешивать в выражениях различные типы и
# не выполняет автоматические неявные преобразования (кроме некоторых особых случаев).

# Основной особый случай:

# арифметические выражения с различными типами чисел (int, float, complex)
# - тут производится автоматическое преобразование к наиболее сложному типу из участвующих в выражении.

# Для таких случаев необходимо использование явного преобразования типов:

print('Сильная типизация')
print(1 + int('7')) # ошибка
print()
print('Динамическая типизация:')
print('n = 5 # автоматическое определение типа переменной')