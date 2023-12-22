def sum_nums(num1,num2):
    result =  0
    try:
        result = float(num1) + float(num2)
    except ValueError:
        print('Функция сложения работает только с числами.')
    finally:
        return  result


def sub_nums(num1,num2):
    result = 0
    try:
        result = float(num1) - float(num2)
    except ValueError:
        print('Функция сложения работает только с числами.')
    finally:
        return result









def multiply_nums(num1,num2):
    result = 0
    try:
        result = float(num1) * float(num2)
    except ValueError:
        print('Функция сложения работает только с числами.')
    finally:
        return result


def divide_nums(num1,num2):
    result = 0
    try:
        result = float(num1) / float(num2)
    except ValueError:
        print('Функция сложения работает только с числами.')
    except ZeroDivisionError:
        print('Нельзя делить на ноль.')
    finally:
        return result


print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление')
choice = int(input('Введите номер действия: '))
if choice == 1:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    print(sum_nums(num1,num2))
elif choice == 2:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    print(sub_nums(num1,num2))
elif choice == 3:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    print(multiply_nums(num1,num2))
elif choice == 4:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    print(divide_nums(num1,num2))
else:
    print("Такого действия нет.")
