RESET = "\033[0m"
WHITE= "\033[48;5;15m" 


def romb_mask(size):
    high_romb = 2 * size - 1
    center = size - 1
    mask = []
    for y in range(high_romb):
        strok = []
        for x in range(high_romb):
            if abs(x - center) + abs(y - center) == size - 1:
                strok.append(1)
            else:
                strok.append(0)
        mask.append(strok)
    return mask


def karkas_line(mask_line, color_off, color_on=""):
    parts = []
    for contour in mask_line:
        if contour == 1:
            parts.append(color_off + " ")
        else:
            parts.append(color_on + " ")
    return "".join(parts) + RESET


def draw_romb(size, cols, strok):
    mask = romb_mask(size)
    for i in range(strok):
        for mask_line in mask:
            line = "".join(karkas_line(mask_line, RESET, WHITE) for i in range(cols))
            print(line)
    print(RESET)


if __name__ == "__main__":
    draw_romb(size=8, cols=7, strok=5)

