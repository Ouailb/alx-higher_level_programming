#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for i in range(list_length):
        sum = 0
        try:
            sum = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            final_list.append(sum)

    return (final_list)
