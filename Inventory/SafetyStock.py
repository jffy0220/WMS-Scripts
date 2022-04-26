# Safety Stock is the stock level that limits stock shortages due to unforeseen events. 

import argparse
import math

def basic_safety_stock(average_sales, days):
    # Safety Stock = Average Sales * X Safety Days
    # Average Sales ex: 100 qty / day
    ss = average_sales * days
    print("Safety Stock is: %s" % ss)

def average_max_safety_stock(max_lead_time, max_sales, average_lead_time, average_sales):
    # Safety Stock = (Max Lead Time * Max Sales) - (Average Lead Time * Average Sales)
    # Problem with this formula is that if you have an outlier in your data it can cause a problem
    ss = (max_lead_time * max_sales) - (average_lead_time * average_sales)
    print("Safety Stock is %s" % ss)

def std_deviation_demand(z, lt, sd_demand):
    ss = z * math.sqrt(lt) * sd_demand
    print("Safety Stock is: %s" % ss)

def ss_on_variable_leadtime(z, sd_lt, avg_demand):
    ss = z * sd_lt * avg_demand
    print("Safety Stock is: %s" % ss)

def variation_lt_demand(z, lt, sd_demand, sd_lt, avg_demand):
    ss = z * math.sqrt((lt * math.pow(sd_demand, 2)) + (math.pow(sd_lt, 2) * avg_demand))
    print("Safety Stock is: %s" % ss)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for determing safety stock levels')
    parser.add_argument('command', choices=[
        'basic',
        'average-max',
        'all_variation',
        'lt_variation',
        'sd_demand'
    ])

    args = parser.parse_args()
    if args.command == 'basic':
        basic_safety_stock(100, 5)
    elif args.command == 'average-max':
        average_max_safety_stock(40, 39.5, 35, 32.9)
    elif args.command == 'all_variation':
        variation_lt_demand(1.65, 2, 11, .43, 20)
    elif args.command == 'lt_variation':
        ss_on_variable_leadtime(1.65, .43, 20)
    elif args.command == 'sd_demand':
        std_deviation_demand(1.65, 2, 11)

