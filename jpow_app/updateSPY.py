from celery import shared_task
from myapp.models import SPY
import yfinance as yf
import pandas as pd
from datetime import date

#get closing price
def getData():
    tickerData = yf.Ticker('SPY')
    closePrice = tickerData.history(period='1d')['Close'].values[0]
    today = date.today()
    return (today, closePrice)

#create spy object and save to database
def update(data):
    obj = SPY(Date = data[0], closePrice = data[1])
    obj.save()

@shared_task
def update():
    data = getData()
    update(data)
