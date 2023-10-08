list = [2, 4, 5, 6, 8, 9, 190, 230, 204, 100, 106, 107, 103, 500, 509, 600, 501, 700, 800, 900, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1010, 1011, 1012, 1013, 1014, 1015, 1016]
even_numbers = []
odd_numbers = []
odd_number_sum = 0
even_number_sum = 0
#print the orginal list
print("Original list: ", list)

for i in list:
    if i % 2 == 0:
        even_numbers.append(i)
        even_number_sum += i
    else:
        odd_numbers.append(i)
        odd_number_sum += i
        
print("Even number list: ", even_numbers)
print("Odd number list: ", odd_numbers)
print("Even number sum: ", even_number_sum)
print("Odd number sum: ", odd_number_sum)