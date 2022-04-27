import argparse

def basic(avg_daily_sales, lt, ss):
    rop = (avg_daily_sales * lt) + ss
    print("ReOrder Point is: %s" % rop)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for determing stock reorder point')
    parser.add_argument('command', choices=[
        'basic'
    ])

    args = parser.parse_args()
    if args.command == 'basic':
        basic(2, 5, 28)