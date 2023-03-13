def solution(wallpaper):
    x, y = [], []
    for row, wall in enumerate(wallpaper):
        for col, w in enumerate(wall):
            if w == '#':
                x.append(row)
                y.append(col)
    return [min(x), min(y), max(x) + 1, max(y) + 1]