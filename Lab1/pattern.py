RESET = "\033[0m"
WHITE= "\033[48;5;15m" 


def romb_mask(size):
    n = 2 * size - 1
    center = size - 1
    mask = []
    for y in range(n):
        strok = []
        for x in range(n):
            if abs(x - center) + abs(y - center) == size - 1:
                strok.append(1)
            else:
                strok.append(0)
        mask.append(strok)
    return mask


def karkas_line(mask_line, color_on, color_off = ""):
    return "".join((color_on + " ") if contour == 1 else (color_off + " ") for contour in mask_line) + RESET


def draw_romb(size, cols, strok):
    mask = romb_mask(size)
    for i in range(strok):
        for mask_line in mask:
            line = "".join(karkas_line(mask_line, WHITE, RESET) for i in range(cols))
            print(line)
    print(RESET)


if __name__ == "__main__":
    draw_romb(size = 6, cols = 8, strok = 10)