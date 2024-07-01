counter=1
while counter <= 10:
    print(counter)
    if counter % 3 == 0:
        print('divisible by 3')
        counter+=1
        continue

    if counter > 7:
        break
    
    counter+=1
print('loop completed successfully!!!')
    