"""
    01001
    10101
    11111
    00100
    00101

Most common bits in each column:
    00101   -> Gamma Rate

Least common bits in each column:
    11010   -> Epsilon Rate == ~(Gamma Rate)
"""


def read_values():
    file = open("input.txt")
    return [line for line in file]


def find_most_common_bit_in_column(rows, column):
    row_count = len(rows)
    bit_1_count = 0
    for row in rows:
        if row[column] == "1":
            bit_1_count += 1
    bit_0_count = row_count - bit_1_count
    if bit_1_count >= bit_0_count:
        return "1"
    else:
        return "0"


def find_most_common_bit(rows, columns=1):
    row_len = len(rows[0])
    output = str()
    assert columns <= row_len
    for column in range(columns):
        output += find_most_common_bit_in_column(rows, column)
    return output


# I'm not proud of this name...
def find_number_with_most_common_bit_in_each_column(rows, invert_bit=False):
    row_len = len(rows[0])
    remaining_rows = rows
    for column in range(row_len):
        if len(remaining_rows) == 1:
            return int(remaining_rows[0], 2)
        if invert_bit:
            if find_most_common_bit_in_column(remaining_rows, column) == "1":
                most_common_bit = "0"
            else:
                most_common_bit = "1"
        else:
            most_common_bit = find_most_common_bit_in_column(remaining_rows, column)
        remaining = list()
        for row in remaining_rows:
            if row[column] == most_common_bit:
                remaining.append(row)
        remaining_rows = remaining


def main():
    values = read_values()
    gamma_rate = int(find_most_common_bit(values, columns=12), 2)
    epsilon_rate = (gamma_rate ^ 0b111111111111)
    print(f"Gamma Rate: {gamma_rate}; Epsilon Rate: {epsilon_rate}; Power Cosumption: {gamma_rate * epsilon_rate}")
    oxygen_generator = find_number_with_most_common_bit_in_each_column(values)
    co2_scrubber = find_number_with_most_common_bit_in_each_column(values, invert_bit=True)
    print(f"CO2 Scrubber: {co2_scrubber}; Oxygen Generator: {oxygen_generator}; "
          f"Life Support: {co2_scrubber * oxygen_generator}")


if __name__ == "__main__":
    main()
