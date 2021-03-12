import sys
import argparse
import math
parser = argparse.ArgumentParser(description='Loan calculator')
parser.add_argument('--type', type=str, help='Type of Payment')
parser.add_argument('--principal', type=float, help='The Principal amount')
parser.add_argument('--periods', type=float, help='No. of months needed to repay the loan')
parser.add_argument('--interest', type=float, help='Interest on Loan')
parser.add_argument('--payment', type=float, help='Monthly Payment')
args = parser.parse_args()
if (len(sys.argv) < 5) or (args.type != 'annuity' and args.type != 'diff'):
    print('Incorrect parameters')
elif args.type == 'annuity':
    if args.periods is None:
        i = args.interest / (12 * 100)
        n = math.log((args.payment / (args.payment - (i * args.principal))), (1 + i))
        n = round(n, 0)
        if n % 12 == 0:
            if n / 12 > 1:
                print(f'It will take {int(n / 12)} years to repay this loan!')
            elif n / 12 < 1:
                print(f'It will take {int(n % 12)} months to repay this loan!')
            print('Overpayment = ' + str(int((args.payment * n) - args.principal)))
        else:
            print(f'It will take {int(n / 12)} years and {int(n % 12)} months to repay this loan!')
            print('Overpayment = ' + str(int((args.payment * n) - args.principal)))
    elif (args.principal is None) and (args.interest is not None):
        i = args.interest / (12 * 100)
        p = args.payment * ((math.pow(1 + i, args.periods) - 1) / (i * math.pow(1 + i, args.periods)))
        print(f'Your loan principal = {int(p)}!')
        print('Overpayment = ' + str(int((args.payment * args.periods) - int(p))))
    elif (args.payment is None) and (args.principal is not None):
        i = args.interest / (12 * 100)
        a = args.principal * ((i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1))
        print(f'Your monthly payment = {math.ceil(a)}!')
        print('Overpayment = ' + str(math.ceil((a * args.periods) - args.principal)))
elif args.type == 'diff':
    i = args.interest / (12 * 100)
    total_payment = 0.0
    for m in range(1, 11):
        d = (args.principal / args.periods) + i * (args.principal - ((args.principal * (m - 1)) / args.periods))
        print(f'Month {m}: payment is {math.ceil(d)}')
        total_payment += d
    print("""
Overpayment = """ + str(math.ceil(total_payment - args.principal)))
