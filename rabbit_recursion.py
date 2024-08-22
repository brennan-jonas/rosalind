month_total_pair = {1: 1, 2: 1}

n = int(input("Please Enter Month! : N =   "))
k = int(input("Please Enter litter of rabbit pairs!: k =  "))

if n == 1 or n == 2:
    print(month_total_pair[n])
else:
    for x in range(3, 45):
        total_pair = month_total_pair[x-1] + month_total_pair[x-2] * k
        month_total_pair.update({x: total_pair})

    print(month_total_pair[n])
