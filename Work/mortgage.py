# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 12*5
extra_payment_end_month = extra_payment_start_month + 4*12
extra_payment = 1000

i = 1
extra=0
while principal > 0:
    if i >= extra_payment_start_month and i <= extra_payment_end_month:
        extra = extra_payment
    if ((principal * (1+rate/12)) > (payment + extra)):
        principal = principal * (1+rate/12) - (payment + extra)
        total_paid = total_paid + payment + extra
    else:
        total_paid = total_paid + (principal * (1+rate/12))
        principal = 0
    extra = 0
    print (i, total_paid, principal)
    i = i+1
print('Total paid', total_paid, "months", i-1)