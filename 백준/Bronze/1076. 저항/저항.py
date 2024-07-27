def get_resistor_value(colors):
    color_map = {
        'black': (0, 1),
        'brown': (1, 10),
        'red': (2, 100),
        'orange': (3, 1_000),
        'yellow': (4, 10_000),
        'green': (5, 100_000),
        'blue': (6, 1_000_000),
        'violet': (7, 10_000_000),
        'grey': (8, 100_000_000),
        'white': (9, 1_000_000_000)
    }
    
    # 첫 번째와 두 번째 색의 값
    first_color_value = color_map[colors[0]][0]
    second_color_value = color_map[colors[1]][0]
    
    # 세 번째 색의 곱
    multiplier = color_map[colors[2]][1]
    
    # 최종 저항 값 계산
    resistance_value = (first_color_value * 10 + second_color_value) * multiplier
    
    return resistance_value

# 입력 받기
colors = [input().strip() for _ in range(3)]
result = get_resistor_value(colors)
print(result)