food=input('Biriyani/Manthi: ')
category=input('Chicken/Beef: ')
if food == 'Biriyani':
    if category == 'Chicken':
        print(180)
    else:
        print(200)
else:
    if category == 'Chicken':
        print(200)
    else:
        print(220)