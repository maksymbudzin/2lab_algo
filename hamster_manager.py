from binary_search_tree import BinaryTree
from hamster_model import Hamster


def get_data(filename):
    with open(filename, 'r') as file:
        S = int(file.readline())
        C = int(file.readline())
        binary_tree = BinaryTree(lambda x: (x.daily_norm, x.daily_norm + x.avarice))
        for line in file.readlines():
            val1, val2 = line.split()
            binary_tree.add_elem(Hamster(int(val1), int(val2)))

    return {'s': S, 'c': C, 'hamstr': binary_tree}


def write_data(filename, change_data):
    filename = filename.replace('in_put', 'out_put')
    with open(filename, 'w') as file:
        file.write(str(change_data))


def algorithm(file_to_read, file_to_write):
    data = get_data(filename=file_to_read)

    daily_food_supply = data['s']  # Отримаємо денний запас їжі  19

    total_hamsters = data['c']  # Отримаємо заг к-ть хомяків  4

    hamstr = data['hamstr']  # Отримаємо денну норму та жадібність

    fed_hamsters = 0

    available_daily_supply = daily_food_supply

    previous_avarice = 0  # попередня жадібність хомяка
    checked_hamsters = 0
    while available_daily_supply > 0 and checked_hamsters < total_hamsters:
        cur_hamster = hamstr.get_min_value()

        checked_hamsters += 1
        if fed_hamsters > 0:
            if available_daily_supply >= (cur_hamster.daily_norm + (fed_hamsters) *
                                          previous_avarice):  # віднімаємо жадібність першого з урахуванням наявності наступногоо+те, що він їсть
                fed_hamsters += 1
                available_daily_supply -= cur_hamster.daily_norm  # яякщо наш, то мінус їжа
                previous_avarice += cur_hamster.avarice * fed_hamsters  # врахуємо жадібність надалі
                hamstr.remove_elem()
            else:
                if available_daily_supply == (fed_hamsters * previous_avarice):
                    fed_hamsters += 1
                    available_daily_supply -= fed_hamsters * previous_avarice
                    previous_avarice += cur_hamster.avarice * fed_hamsters
                    hamstr.remove_elem()
                break
        else:  # коли додали першого лише
            if cur_hamster.daily_norm <= available_daily_supply:
                fed_hamsters += 1
                available_daily_supply -= cur_hamster.daily_norm  # яякщо наш, то мінус їжа
                previous_avarice += cur_hamster.avarice  # врахуємо жадібність надалі
                hamstr.remove_elem()
    print(fed_hamsters)
    write_data(file_to_write, fed_hamsters)
    return fed_hamsters


if __name__ == '__main__':
    file_name = 'in_put/hamstr.in2'
    algorithm(file_name, "out_put/hamstr.in2")
