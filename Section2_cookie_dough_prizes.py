print('COOKIE DOUGH SALES POINTS AND PRIZES TRACKER')
classmates = []
while True:
    name = input('Name: ').strip()
    if not name:
        break
    try:
        buckets_sold = int(input('Cookie dough sold: '))
        if buckets_sold < 0:
            print('Please enter a valid number of buckets sold.')
            continue
    except ValueError:
        print('Invalid input. Please enter a valid number for the buckets sold.')
        continue
points = buckets_sold
prizes = points // 10

classmates.append((name, points, prizes))

print("\nSelling over! Let's see how everyone did!')
for name, points, prizes in classmates:
    print(f'{name} has {points} points and can redeem {prizes} prize(s).')