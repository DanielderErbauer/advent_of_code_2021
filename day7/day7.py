
def read_input(name):
    file = open(name)
    nums = []
    for line in file:
        nums = [int(num) for num in line.split(",")]
    return nums


def find_min(nums):
    min_val = 2**31
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


def find_max(nums):
    max_val = 0
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val


def generate_points(nums):
    return [num for num in range(find_min(nums), find_max(nums) + 1)]


def calculate_best_consumption(nums, increase_rate=0):
    evolve_points = generate_points(nums)
    consumptions = []
    for point in evolve_points:
        total_consumption = 0
        for num in nums:
            delta = abs(num - point)
            total_consumption += delta
            if increase_rate > 0:
                # ONLY WORKS FOR INCREASE_RATE == 1
                total_consumption += int(delta/2 * (0 + delta - 1))
        consumptions.append(total_consumption)
    least_consumed = find_min(consumptions)
    print(consumptions)
    print(least_consumed)


def main():
    nums = read_input("input.txt")
    calculate_best_consumption(nums)
    calculate_best_consumption(nums, 1)


if __name__ == "__main__":
    main()
