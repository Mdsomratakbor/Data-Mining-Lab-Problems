
print('Enter Length of Sides of a Triangle\n')
side1 = float(input('Enter Length of Side 1: '))
side2 = float(input('Enter Length of Side 2: '))
side3 = float(input('Enter Length of Side 3: '))

if(side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1:
    print('Triangle is Valid')
else:
    print('Triangle is Invalid')
