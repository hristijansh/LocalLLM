def my_function(endparameters):
    even_numbers = []
    #TODO: End number needs to be an input parameter in the function, not a fixed number 11. Example, my_function(10), my_function(15)
    for i in range(1, endparameters):
        if i % 2 == 0:
            even_numbers.append(i)
    print()        
    print("Even numbers up to", endparameters - 1, "are:")
    print(even_numbers)


    sum_even = 0
    for number in even_numbers:
        sum_even += number
        
    print()
    print("Sum of even numbers up to", endparameters - 1, "is:")
    print(sum_even)

my_function(11)
