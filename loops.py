def sum_of_odds():
    
    while True:
        inputr = 0
        #inputr = int(input)
        if inputr != 0:
            #inputr = input("enter another #: ")
            #inputr = int(input)
            continue
        elif input == 0:
            break


def reverse_char(a_string):
    reverse = ''
    for char in a_string:
        reverse = char + reverse
    return reverse

def  print_range_for(a_range):
    for number in a_range:
        print(number, end= " ")
    print()

# if __name__ == "__main__":
#     print_range_for(range(0,10))
#     #sum_of_odds()

def main():
    print_range_for(range(0,10))
    print(reverse_char("Yiiipeee"))

main()