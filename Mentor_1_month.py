# Задача №1

def find_area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs((x1 - x2) * (y1 + y2) + (x2 - x3) * (y2 + y3) + (x3 - x1) * (y1 + y3))
    with open('area.txt', 'w') as file:
        file.write(f'Площадь треугольника - {area}')
    side_1 = (x2 - x1) * 2 + (y2 - y1) * 2
    side_2 = (x3 - x2) * 2 + (y3 - y2) * 2
    side_3 = (x1 - x3) * 2 + (y1 - y3) * 2
    if (side_1 == side_2 + side_3) or (side_2 == side_1 + side_3) or (side_3 == side_2 + side_1):
        with open('truefalse.txt', 'w') as file:
            file.write('True')
    else:
        with open('truefalse.txt', 'w') as file:
            file.write('False')

# Задача №2

sentense = input()
results = {}
for word in sentense.lower().split():
    results[sentense.count(word)] = word
a = max(results.keys())
print(results[a])

# Задача №3

n = int(input())
l = list()
for i in range(n):
    hours, minutes, seconds = map(int, input().split())
    l.append((hours, minutes, seconds))
l.sort()
for i in l:
    print(*i)
