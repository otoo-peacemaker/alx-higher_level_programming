#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret = []
    for i in range(list_length):
        r = 0
        try:
            r = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            ret.append(r)
    return ret
