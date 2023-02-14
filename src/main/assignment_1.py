"assignment 1"

import numpy as np

def main():

    "main function"

    val = np.array(list("0100000001111110101110010000000000000000000000000000000000000000"), int)

    f_val = val_to_dblpercision(val)
    nor_f_val = normalize(f_val)
    chopped_f_val = digit_chopping(nor_f_val, 3)
    rounded_f_val = digit_rounding(nor_f_val, 3)

    print(f'{f_val}', end='\n\n')
    print(f'{chopped_f_val}', end='\n\n')
    print(f'{rounded_f_val}', end='\n\n')
    calculate_error(nor_f_val, rounded_f_val)
    print(f'{min_terms(1, 0.0001)}', end='\n\n')
    bisection_method(-4, 7, "(x ** 3) + (4 * (x ** 2)) - 10")
    newton_raphson_method(-4, 0.0001, "(x ** 3) + (4 * (x ** 2)) - 10", "(3 * (x ** 2)) + (8 * x)")

def val_to_dblpercision(bit_arr):

    "convert value to float type"

    s_val = bit_arr[0]
    c_val = 0
    f_val = 0

    for i in range(11):
        c_val += bit_arr[i + 1] * (2 ** (10 - i))

    for i in range(52):
        f_val += bit_arr[i + 12] * (0.5 ** (i + 1))

    return ((-1) ** s_val) * (2 ** (c_val - 1023)) * (1 + f_val)

def normalize(num):

    "normalize float"

    if num >= 1:
        while num >= 1:
            num /= 10
    elif num < 0.1:
        while num < 0.1:
            num *= 10
    return num

def digit_chopping(flt, r_val):

    "chop all digits after the rth place"

    r_val = 10 ** r_val

    return (int(flt * r_val)) / (r_val)

def digit_rounding(flt, r_val):

    "round flt to nearest rth place"

    r_val = 10 ** (r_val + 1)

    return (int(int(((flt * r_val) + 5)) / 10)) * 10 / (r_val)

def calculate_error(actual, estimated):

    "calculate the absolute then relative errors"

    abs_error = digit_rounding(abs(actual - estimated), 8)
    rel_error = abs_error/abs(actual)

    print(f'{abs_error}')
    print(f'{rel_error}', end='\n\n')

def min_terms(x_val, tolerance):

    "calculates the minimum number of terms needed to satisfy the tolerance"

    f_x = 0
    k = 1
    temp = 0

    f_x += function_x(x_val, k)

    while abs(temp - f_x) >= tolerance:
        k += 1
        temp = f_x
        f_x += function_x(x_val, k)

    return k - 1

def function_x(x_val, k):

    "((-1) ** k) * (x ** k) / (k ** 3)"

    kth_term = (((-1) ** k) * (x_val ** k)) / (k ** 3)
    return kth_term

def bisection_method(left, right, given_function : str):

    "bisection method of finding roots"

    x = left
    left_bound = eval(given_function)
    x = right
    right_bound = eval(given_function)

    if left_bound * right_bound >= 0:
        print("invalid")
        return

    tolerance = 0.0001
    diff = right - left
    k = 0

    while abs(diff) >= tolerance:
        k += 1
        mid_point = (left + right) / 2
        x = mid_point
        mid_val = eval(given_function)
        x = left
        left_val = eval(given_function)
        if (mid_val > 0 and left_val < 0) or (mid_val < 0 and left_val > 0):
            right = mid_point
        else:
            left = mid_point
        diff = right - left

    print(k, end="\n\n")

def newton_raphson_method(est_val, tolerance, f_x, f_prime_x):

    "the newton-raphson method"

    k = 0

    approx = 0
    new_est_val = est_val

    while True:
        new_est_val -= approx
        x = new_est_val
        f = eval(f_x)
        f_prime = eval(f_prime_x)

        approx = f / f_prime

        k += 1

        if abs(approx) < tolerance:
            break

    print(k)


if __name__ == "__main__":
    main()
