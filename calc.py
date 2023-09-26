import math


def calc(exp):
    allowed = '+-*/^!|'
    if exp == '':
        raise TypeError(f'Пустая строка, выражение должно содержать 2 целых числа и 1 знак!')
    if not any(sign in exp for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})!')
    for sign in allowed:
        if sign in exp:
            try:
                left, right = exp.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    try:
                        res = left/right
                    except(ZeroDivisionError):
                        raise ZeroDivisionError('Ошибка деления на ноль!')
                    return left / right
                elif sign == '^':
                    return pow(left, right)
                elif sign == '!':
                    return math.factorial(left)
                elif sign == '|':
                    try:
                        res = math.sqrt(left)
                    except(ValueError):
                        raise ValueError('Число под корнем должно быть положительным!')
                    return res
            except(ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак!')


if __name__ == '__main__':
    print(calc('25|2'))
