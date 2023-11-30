import math

calculations = [
    "Площадь параллелограмма", "Диагонали параллелограмма", "Угол между диагоналями"
]

def calculate_area_case1(side_a, height_b, angle):
    # Известна сторона а, высота к стороне б и меньший угол
    return round(side_a * height_b * math.sin(math.radians(angle)), 2)

def calculate_diagonals_case1(side_a, height_b, angle):
    # Известна сторона а, высота к стороне б и меньший угол
    side_b = math.sqrt(side_a**2 + height_b**2)
    diagonal_1 = side_a / math.sin(math.radians(angle))
    diagonal_2 = side_b / math.sin(math.radians(180 - angle))
    return round(diagonal_1, 2), round(diagonal_2, 2)

def calculate_angle_between_diagonals_case1(side_a, height_b, angle):
    # Известна сторона а, высота к стороне б и меньший угол
    _, diagonal_2 = calculate_diagonals_case1(side_a, height_b, angle)
    angle_between_diagonals = math.degrees(math.asin(height_b / diagonal_2))
    return round(angle_between_diagonals, 2)

def calculate_area_case2(side_a, side_b, height):
    # Известна сторона а, сторона б и высота
    return round(0.5 * (side_a + side_b) * height, 2)

def calculate_diagonals_case2(side_a, side_b, height):
    # Известна сторона а, сторона б и высота
    diagonal_1 = math.sqrt(side_a**2 + side_b**2 + 2 * side_a * side_b)
    diagonal_2 = math.sqrt(side_a**2 + side_b**2 - 2 * side_a * side_b)
    return round(diagonal_1, 2), round(diagonal_2, 2)

def calculate_angle_between_diagonals_case2(side_a, side_b, height):
    # Известна сторона а, сторона б и высота
    diagonal_1, diagonal_2 = calculate_diagonals_case2(side_a, side_b, height)
    angle_between_diagonals = math.degrees(math.acos((side_a**2 + side_b**2 - diagonal_1**2) / (2 * side_a * side_b)))
    return round(angle_between_diagonals, 2)
