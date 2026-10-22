import yfinance as yf
import csv 
def get_current_price(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    price = ticker.fast_info['last_price']   
    return price

def user_data():
    f=open("portfolio_summary.csv","w")
    rec=csv.writer(f)
    while True:
        user_name=input("Enter your name: ")
        ticker=input("Enter your Ticker symbol ")
        current_price=get_current_price(ticker)
        user_data=["user_name","ticker","buy_price","quantity","Percentage profit & loss","status"]
        rec.writerow(user_data)
        buy_price=int(input("The price at which you bought the stock"))
        quantity=int(input("enter the quantity of stock you bought"))
        user_data=[user_name,ticker,buy_price,quantity]  
        total_invested_capital=buy_price*quantity
        current_price=current_price*quantity
        if current_price>total_invested_capital:
            percentage_profit_loss=(current_price-total_invested_capital)/total_invested_capital*100
            user_data.append(percentage_profit_loss)
            user_data.append("profit")
        elif current_price==total_invested_capital:
            percentage_profit_loss=0
            user_data.append(percentage_profit_loss)
            user_data.append("neither profit nor loss")
        else:
            percentage_profit_loss=(current_price-total_invested_capital)/total_invested_capital*100
            user_data.append(percentage_profit_loss)
            user_data.append("loss")
        rec.writerow(user_data)
        check=input("do u want to continue store data answer in 'yy'")
        if check not in "yY":
            break
user_data()

