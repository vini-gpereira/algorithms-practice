def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
        return 0
    return 1

def print_all_possible_bits(length):
    for i in range(2 ** length):
        number = ""
        for j in range(length):
            number = str(get_bit(i, j)) + number
        print(f"{i}: {number}")

if __name__ == "__main__":
    print_all_possible_bits(3)