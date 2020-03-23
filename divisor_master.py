# делители числа
def get_divisors(numb):
    return [i for i in range(1, numb + 1) if numb % i == 0]


# проверка числа на простоту
def is_simple(numb):
    divisors_simple = [1, numb]
    divisors_all = get_divisors(numb)

    return divisors_all == divisors_simple


# самый большой делитель числа
def get_max_divisor(numb):
    return max([i for i in get_divisors(numb)])


# самый большой простой делитель числа
def get_max_divisor_simple(numb):
    return max([i for i in get_divisors(numb) if is_simple(i)])


# самый малый простой делитель числа
def get_min_divisor_simple(numb):
    return min([i for i in get_divisors(numb) if is_simple(i)])


# разложение числа на простые множители
def get_factors_simple(numb):
    divisors_simple = []
    divisor_min = get_min_divisor_simple(numb)
    remain = numb // divisor_min
    divisors_simple.append(divisor_min)
    while not is_simple(remain):
        divisor_min = get_min_divisor_simple(remain)
        remain = remain // divisor_min
        divisors_simple.append(divisor_min)

    divisors_simple.append(remain)

    return divisors_simple

