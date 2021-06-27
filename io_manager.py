import pyautogui as pg

""" Reference guide from Terranova Tech: https://youtu.be/jESGMTcrhSY """

def prompt_input():
    grid = []
    for i in range(1, 10):
        row = list(input(f"Row {i}: "))
        nums = []

        for n in row:
            nums.append(int(n))
        grid.append(nums)
    return grid

# Note: You only have 5 seconds to press the first tile before autogui runs!
def push_to_screen(puzzle):
    output = []
    for i, row in enumerate(puzzle):
        if i % 2 == 0:
            output.append([str(n) for n in row])
        else:
            rev = row[::-1]
            output.append([str(n) for n in rev])

    direction = 1 # 1 is right, 0 is left
    for row in output:
        if direction == 1:
            for e in row:
                pg.press(e)
                pg.hotkey("right")
        elif direction == 0:
            for e in row:
                pg.press(e)
                pg.hotkey("left")
        pg.hotkey("down")
        direction = not direction




        # if i % 2 == 0:
        #     for _ in range(9):
        #         pg.press(num)
        #         pg.hotkey("right")
            
        #     if counter % 9 == 0:
        #         pg.hotkey("down")
        #         pg.hok
        #         # for _ in range(9):
        #         #     pg.hotkey("left")
            
