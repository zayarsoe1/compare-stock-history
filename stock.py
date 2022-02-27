from yahoo_fin.stock_info import *
from prettytable import PrettyTable
import sys
from datetime import datetime, timedelta

#Enter past date here (mm/dd/yyyy)
past_date =  "12/27/2021"

#calculating end date
date_1 = datetime.strptime(past_date, "%m/%d/%Y")
next_day = date_1 + timedelta(days=1)
next_day = datetime.strftime(next_day,"%m/%d/%Y")


#Table heading row
t = PrettyTable(['Symbols','Today', past_date , 'Change %', 'Price/Sales', 'Price/Book', 'ER Date' ])

stock_list = []
with open("stock_list.txt") as f:
    for line in f:
        if line != "\n": #skipping empty lines
            line = line.rstrip()
            stock_list.append(line)

#Coloring the percent
R = "\033[0;31;49m" # TRANSPARENT RED
G = "\033[0;32;49m" # TRANSPARENT GREEN
N = "\033[0m" # Reset



def stock_history_compare():

    for stock in stock_list:

        #Get latest price
        print("Getting latest price for ", stock)
        lprice = get_live_price(stock)
        lprice = int(lprice)

        print("Getting past price for ", stock)
        df = get_data(stock, start_date = past_date, end_date = next_day)
        hprice = df.iloc[0,1] #row and column from pandas dataframe
        hprice = int(hprice)

        #difference % calculation
        diffprice = hprice - lprice

        percent = float(diffprice) / float(hprice) * 100

        percent = int(percent)
        percent = -percent

        #coloring the percent
        if percent < 0:
            color = R
        else:
            color = G


        #getting stats
        print("Getting stats for ", stock)
        try:
            stat = get_stats_valuation(stock)

            ps_val = stat.iloc[5,1] #getting price per sales
            pb_val = stat.iloc[6,1] #getting price per book


        except Exception:
            # some stock symbols like ETF indexes have don't this value
            ps_val = "N/A"
            pb_val = "N/A"
            pass



        #get next earning date
        print("Checking ER date for ", stock)
        try:
            er_date = get_next_earnings_date(stock)
        except Exception:
            # some stock symbols like ETF indexes have don't this value
            er_date = "N/A"
            pass


        #printing the table , it only accept string , N to terminate the color

        print("Adding row in table for ", stock)



        t.add_row([stock,"$"+str(lprice),"$"+str(hprice),color+str(percent)+"%"+N,ps_val,pb_val,er_date])

    print(t)

if __name__ == '__main__':
    stock_history_compare()
