RED = "\033[48;5;196m" 
RESET = "\033[0m"


def plot_y_3x(height, width):
    max_x = width - 1
    max_y = 3 * max_x 

    y_scale = max_y / (height - 1) if max_y > 0 else 1
    grid = [[' ' for i in range(width)] for i in range(height)]

    for x in range(width):
        grid[height - 1][x] = '─' 
    for y in range(height):
        grid[y][0] = '│' 
    grid[height - 1][0] = '└'   
    grid[height - 1][x] += '>'

    for x in range(width):
        y = 3 * x
        y_row = round((height - 1) - (y / y_scale))
        if 0 <= y_row < height:
            grid[y_row][x] = '*'

    for y in range(height):
        line = ""
        for x in range(width):
            blank = grid[y][x]
            if blank == '*':
                line += RED + " " + RESET 
            else:
                line += blank
        print(line)


if __name__ == "__main__":
    plot_y_3x(height = 20, width = 25)