# Safety Stock is the stock level that limits stock shortages due to unforeseen events. 

import argparse

def basic_safety_stock(average_sales, days):
    # Safety Stock = Average Sales * X Safety Days
    # Average Sales ex: 100 qty / day
    ss = average_sales * days
    print("Safety Stock is: %s" % ss)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for determing safety stock levels')
    parser.add_argument('command', choices=[
        'basic'
    ])

    args = parser.parse_args()
    if args.command == 'basic':
        basic_safety_stock(100, 5)

