RED = "\033[48;5;196m" 
RESET = "\033[0m" 


def function_y_3x(height, width):
    max_x = width 
    max_y = 3 * max_x 
    y_scale = max_y // (height)
    grid = [[' ' for i in range(width)] for i in range(height)]

    n = 1
    k = 0
    for x in range(width):
        if k % 3 == 0 and k != 0:
            grid[height - 1][x] = str(n)
            n += 1
        else:
            grid[height - 1][x] = '─' 
        k += 1
        
    k = height - 1
    for y in range(height):
        if k % 3 == 0 and k != 0:
            grid[y][0] = str(k)
        else:
            grid[y][0] = '│' 
        k -= 1 
    grid[height - 1][x] = '>'
    grid[0][0] = '^'

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
    function_y_3x(height=13, width=15)

