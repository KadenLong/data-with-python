open_file = open('CupcakeInvoices.csv')

for row in open_file:
    print(row)

open_file.close()
#
open_file = open('CupcakeInvoices.csv')

for line in open_file:
    line = line.split(',')
    print(line[2])

open_file.close()
#
open_file = open('CupcakeInvoices.csv')
profit = 0

for line in open_file:
    line = line.split(',')
    
    quantity = float(line[3])
    price = float(line[4])

    quantity = round(quantity, 2)
    price = round(price, 2)

    total = quantity * price
    print(total)

    profit += total

print("{:.2f}".format(profit))


open_file.close()
