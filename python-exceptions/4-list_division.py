#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l = [0] * list_length
    for i in range(list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
        except Exception as e:
            c = 0
            if isinstance(e, ZeroDivisionError):
                print("division by 0")
            if isinstance(e, TypeError):
                print("wrong type")
            if isinstance(e, IndexError):
                print("out of range")
                break
        finally:
            l[i] = c
    return l
