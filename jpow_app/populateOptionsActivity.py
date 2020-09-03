import yfinance as yf
import pandas as pd
pd.options.mode.chained_assignment = None
import concurrent.futures
import os
from jpow_app.models import UnusualOption
import itertools

#get tickers into list format
def getAvailableTickers(filename):
    with open(filename, 'r') as file:
        s = file.read()
        tickers = s.split(",")
    return tickers
        
#parse tickers for calls and options where vol > oi by atleast senstivity threshold
def getUnusualActivity(ticker, sensitivity):
    company = yf.Ticker(ticker)
    unusual_activity = pd.DataFrame(columns = ['volume', 'openInterest', 'Ticker', 'Expiration Date', 'Type'])
    try:
        option_dates = company.options
        #parse options data and show unsual activity (volume > OI)
        for date in option_dates:
            opt = company.option_chain(date)
            calls = opt.calls
            calls_result = calls[calls['volume'] - calls['openInterest'] > sensitivity][['volume', 'openInterest', 'strike']]
            calls_result['Ticker'] = ticker
            calls_result['Expiration Date'] = date
            calls_result['Type'] = 'Call'

            puts = opt.puts
            puts_result = puts[puts['volume'] - puts['openInterest'] > sensitivity][['volume', 'openInterest', 'strike']]
            puts_result['Ticker'] = ticker
            puts_result['Expiration Date'] = date
            puts_result['Type'] = 'Put'

            results = [unusual_activity, calls_result, puts_result]
            unusual_activity = pd.concat(results)

        return unusual_activity
    #no options data
    except IndexError:
        return unusual_activity

if __name__ == "__main__":
    tickers = getAvailableTickers("tickers.txt")

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(getUnusualActivity, tickers, itertools.repeat(100))
    for result in results:
        if len(result) > 0:
            df_records = result.to_dict('records')
            model_instances = [UnusualOption(
                Ticker=record['Ticker'],
                Type=record['Type'],
                Strike=record['strike'],
                OpenInterest=record['openInterest'],
                Volume=record['volume'],
                ExpirationDate=record['Expiration Date'],
                ) for record in df_records]

            UnusualOption.objects.bulk_create(model_instances)
