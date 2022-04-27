import argparse
import math

# Calculation designed to find the optimal order quantity for businesses to minimize logistics costs, warehousing space, stockouts, and overstock costs. 

# EOQ = SQRT(2(SETUP)(DEMAND))/HOLDING

def basic(h, s, d):
    eoq = math.sqrt((2 * s * d) / h)
    print("Economic Order Quantity: %s" % eoq)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for determing economic order quantity')
    parser.add_argument('command', choices=[
        'basic'
    ])

    args = parser.parse_args()
    if args.command == 'basic':
        basic(.75, 500, 10000)