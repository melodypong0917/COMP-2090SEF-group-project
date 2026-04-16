def shell_ciura(list):
    n = len(list)
    span = n//2
    while span > 0:
        for i in range(span, n):
            number_a = list[i]
            number_b = i
            while number_b >= span and list[number_b-span] > number_a:
                list[number_b] = list[number_b-span]
                number_b = number_b - span
            list[number_b] = number_a
        span = span//2

number_input = input("Enter numbers that you want to sort(PLease separate them by ,):")
list = [int(x) for x in number_input.split(",")]
shell_ciura(list)
print(list)