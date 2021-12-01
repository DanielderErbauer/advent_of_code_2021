
def read_values():
    file = open("input.txt")
    return [int(line) for line in file]


def count_increases(values, window_size=1):
    last = 0
    count = 0
    for i in range(len(values) - window_size + 1):
        w_sum = 0
        for w in range(window_size):
            w_sum += values[i + w]
        if last != 0 and w_sum > last:
            count += 1
        last = w_sum
    return count


def main():
    values = read_values()
    increases = count_increases(values)
    print(increases)
    increases_w3 = count_increases(values, 3)
    print(increases_w3)


if __name__ == "__main__":
    main()
