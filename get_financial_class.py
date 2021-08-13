
"""
________________________________________________________________________________

    File        :   get_financial_class.py
    Author      :   Luis de la Barba
    Date        :   08-Aug-2021
    Purpose     :   Class for getting the financial data
    Requisites  :
        pandas -> 'pip3 install pandas'
    Register    :
        Ref     Date            Author                  Description
--------------------------------------------------------------------------------
        01      08-Aug-2021     Luis de la Barba        File created
________________________________________________________________________________
"""
import debug_class
import json
import requests
import pandas as pd

# Variables
var = debug_class.DEBUG_CLASS(__name__)
var.changeLevelToDebug()                # Call this function for showing debug messages
shoot = var.log_file

class GET_FINANCIAL_CLASS:
    api_key = "83TM5W22XXKUNWW8"
    search_comp = "AMD"
    company_daily_close = []
    company_daily_high = []
    company_daily_low = []
    marketwatch_analisys = []
# ******************************************************************************
#   Function name:  __init__
#   Descriptions:   Function for initializing the class
# ******************************************************************************
    def __init__(self,id="AMD"):
        self.search_comp = id

        shoot.info("Class initiated for " + self.search_comp)
        self.get_company_overview()
        self.get_company_daily()
        self.get_analisys_info()

# ******************************************************************************
#   Function name:  get_company_overview
#   Descriptions:   Function for getting the company data
# ******************************************************************************
    def get_company_overview(self):
        url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+ self.search_comp +'&apikey='+ self.api_key
        r = requests.get(url)
        self.company_overview = r.json()

# ******************************************************************************
#   Function name:  get_company_overview
#   Descriptions:   Function for getting the company data
# ******************************************************************************
    def get_company_daily(self):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ self.search_comp +'&apikey='+ self.api_key
        r = requests.get(url)
        text = r.json()
        self.company_daily = text["Time Series (Daily)"]

        for i in self.company_daily:
            self.company_daily_close.append(self.company_daily[i]["4. close"])
            self.company_daily_high.append(self.company_daily[i]["2. high"])
            self.company_daily_low.append(self.company_daily[i]["3. low"])
            #cont += 1

        self.company_daily_close = self.company_daily_close[::-1]
        self.company_daily_high = self.company_daily_high[::-1]
        self.company_daily_low = self.company_daily_low[::-1]

# ******************************************************************************
#   Function name:  get_analisys_info
#   Descriptions:   Get the data from the marketwatch website
# ******************************************************************************
    def get_analisys_info(self):
        tables = pd.read_html('https://www.marketwatch.com/investing/stock/' + self.search_comp + '/analystestimates?mod=mw_quote_analyst')
        self.marketwatch_analisys.append(tables[5].iloc[0,1])
        self.marketwatch_analisys.append(tables[5].iloc[2,1])
        self.marketwatch_analisys.append(tables[5].iloc[3,1])

# *******************************************************************************
#   Function name:  info
#   Descriptions:   Class for potting managemant
# *******************************************************************************
    def info(self):
        shoot.debug("*****************************************")
        shoot.debug(" - Name: " + self.company_overview["Name"])
        shoot.debug(" - " + self.company_overview["Exchange"] + ", " + self.company_overview["Symbol"])
        shoot.debug("*****************************************")
        shoot.debug(" - Analyst Price:  " + self.company_overview["AnalystTargetPrice"])
        shoot.debug(" - Clossing price: " + self.company_daily_close[-1])
        shoot.debug(" - Highest:        " + self.company_daily_high[-1])
        shoot.debug(" - Lowest:         " + self.company_daily_low[-1])
        shoot.debug("*****************************************")
        shoot.debug(" MARKET WATCH ANALYSIS")
        shoot.debug(" - High:           " + self.marketwatch_analisys[0])
        shoot.debug(" - Low:            " + self.marketwatch_analisys[1])
        shoot.debug(" - Average:        " + self.marketwatch_analisys[2])
        shoot.debug("*****************************************")
        shoot.debug("")

if __name__ == "__main__":

    company = "AMD"
    company = "INTC"
    #company = "NVDA"
    #company = "AGR"

    enterprise = GET_FINANCIAL_CLASS(company)
    enterprise.info()
