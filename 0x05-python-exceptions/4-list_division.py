#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            # Check if the index is within the range of both lists
            if i < len(my_list_1) and i < len(my_list_2):
                # Try to perform the division
                quotient = my_list_1[i] / my_list_2[i]
            else:
                # If one of the lists is too short, raise an IndexError
                raise IndexError("out of range")

            # Check if the result is a valid number (integer or float)
            if not isinstance(quotient, (int, float)):
                raise TypeError("wrong type")

            result.append(quotient)

        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result.append(0)

        except (TypeError, IndexError) as e:
            # Handle wrong type or out of range
            print(e)
            result.append(0)

        finally:
            # This block will be executed no matter what
            pass

    return result
