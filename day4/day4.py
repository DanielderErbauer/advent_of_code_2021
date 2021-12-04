
class BingoPanel:

    def __init__(self, data, size=5):
        self.size = size
        self.data = data
        self.marked = [[False for _ in range(size)] for _ in range(size)]

    def print(self):
        print(self.marked)

    def mark(self, number):
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] == number:
                    self.marked[i][j] = True

    def has_won(self):
        for i in range(self.size):
            horizontal_count = 0
            vertical_count = 0
            for j in range(self.size):
                if self.marked[i][j]:
                    horizontal_count += 1
                if self.marked[j][i]:
                    vertical_count += 1
            if horizontal_count == 5 or vertical_count == 5:
                return True
        return False

    def calculate_score(self, number):
        unmarked_numbers = 0
        for i in range(self.size):
            for j in range(self.size):
                if not self.marked[i][j]:
                    unmarked_numbers += self.data[i][j]
        return number * unmarked_numbers


def read_data(file_name):
    file = open(file_name)
    nums = []
    panels = []
    current_panel_index = 0
    data = []
    for idx, line in enumerate(file):
        if idx == 0:
            nums = [int(m) for m in str(line).split(",")]
            continue
        if 1 <= (idx - 1) % 6 <= 5:
            field = []
            for num in str(line).split(" "):
                if len(num.rstrip()) > 0:
                    field.append(int(num.rstrip()))
            data.append(field)
            current_panel_index += 1
            if current_panel_index == 5:
                current_panel_index = 0
                panels.append(BingoPanel(data))
                data = []
    file.close()
    return nums, panels


# Which panel wins first
def not_main():
    nums, panels = read_data("input.txt")
    for num in nums:
        panel_has_won = False
        for idx, panel in enumerate(panels):
            panel.mark(num)
            if panel.has_won():
                panel_has_won = True
                print(f"Score: {panel.calculate_score(num)}")
                break
        if panel_has_won:
            break


# Which panel wins last
def main():
    nums, panels = read_data("input.txt")
    for num in nums:
        panels_to_remove = []
        for idx, panel in enumerate(panels):
            panel.mark(num)
            if panel.has_won():
                if len(panels) > 1:
                    panels_to_remove.append(panel)
                else:
                    print(f"Score: {panel.calculate_score(num)}")
                    panels_to_remove.append(panel)
        panels = [p for p in panels if p not in panels_to_remove]


if __name__ == "__main__":
    main()
