from file_reader import *


def algorithm(file_to_read, file_to_write):
    daily_food, number_hamsters, hamsters = input_data(file_to_read)

    fed_hamsters = 0
    total_greed = 0
    total_daily_norm = 0
    available_food = daily_food

    hamsters.head = hamsters.merge_sort(hamsters.head)

    for i in range(number_hamsters):

        current = hamsters.get_element(i)

        total_greed += current.greed

        total_daily_norm += current.daily_norm

        fed_hamsters += 1

        available_food = daily_food - (total_daily_norm + (fed_hamsters - 1) * (total_greed))

        if available_food < 0:
            fed_hamsters -= 1
            break

        print(current)

    print(fed_hamsters)

    output_data(file_to_write, str(fed_hamsters))

    return fed_hamsters


if __name__ == '__main__':
    file_to_read = 'in/hamstr.in'
    file_to_write = 'out/hamstr.out'
    algorithm('in/hamstr.in', 'out/hamstr.out')
