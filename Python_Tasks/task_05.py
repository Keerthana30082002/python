icecream=input('Vanilla/Strawberry/Chocolate: ')
size=input('Small/Medium/Large/Extra Large: ')
if icecream == 'Vanilla':
    if size == 'Small':
        total_price=100.00*1.00
    elif size == 'Medium':
        total_price=100.00*1.50
    elif size == 'Large':
        total_price=100.00*2.00
    else:
        total_price=100.00*2.50
elif icecream == 'Strawberry':
    if size == 'Small':
        total_price=120.00*1.00
    elif size == 'Medium':
        total_price=120.00*1.50
    elif size == 'Large':
        total_price=120.00*2.00
    else:
        total_price=120.00*2.50
else:
    if size == 'Small':
        total_price=130.00*1.00
    elif size == 'Medium':
        total_price=130.00*1.50
    elif size == 'Large':
        total_price=130.00*2.00
    else:
        total_price=130.00*2.50
       
print(f'You have selected a {size} {icecream} icecream.Total Price: ₹{total_price} .Enjoy!')
            