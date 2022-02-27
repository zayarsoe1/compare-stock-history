# Stock Price History Comparison

When the stock market crash or gain significantly, the script can be used to compare the gain or loss percentages between current price and point of time.

## Description

The script is to compare the current stock price from a past date. And, the output will show the gain or loss percentage. Additionally, it will also show two useful value metrics -- price per sales, price per book and also the upcoming earning release date.  

For example, assuming that March 9 , 2020 is bottom of market crash due to COVID-19, pick this date and comparing with today's price to see which stocks fully recovered and which are still losing. By looking at price per sales and price per book value to determine whether the price is undervalued or overvalued.



## Getting Started

### Dependencies

* python 3
* yahoo_fin, prettytable, datetime needed before running program. yahoo_fin may have its own dependencies



### Installing

* Download stock.py and stock_list.txt from https://github.com/zayarsoe1/compare-stock-history
* pip3 install yahoo_fin
* pip3 install prettyable

### Executing program

* Open stock_list.txt and enter each stock symbols per line
* Open stock.py and change the following past_date field
```
past_date =  "12/27/2021"
```
* Save and run python3 stock.py


## Authors

Contributors names and contact info

Zayar Soe


## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the GNU GENERAL PUBLIC License - see the LICENSE.md file for details

## Acknowledgments

yahoo_fin, prettytable, datetime
