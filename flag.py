ESC = "\033["
RESET = f"{ESC}0m"
WHITE = f"{ESC}48;5;15m"
RED = f"{ESC}48;5;160m"


def draw_flag(width = 55, height = 15): 
    center_x = width // 2
    center_y = height // 2
    radius = 4

    for y in range(height):
        line_parts = []
        for x in range(width):
            dist = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
            if dist <= radius:
                line_parts.append(RED)
            else:
                line_parts.append(WHITE)
        print(" ".join(line_parts) + RESET)

if __name__ == "__main__":

    draw_flag()
