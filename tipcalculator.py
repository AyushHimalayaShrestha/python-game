bill = float(input('Enter the total bill amount : '))
tip_percent =float(input('Enter tip percentage : '))
people = int (input('How many people are splitting the bill: '))

tip_amount = (tip_percent/100)* bill
total_bill =(bill + tip_amount)
each_person = total_bill /people

print(f'\nTip amount :{tip_amount:.2f}')
print(f'Total bill with tip:{total_bill:.2f}')
print(f'Each person should pay:{each_person:.2f}')