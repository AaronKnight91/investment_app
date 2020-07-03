from datetime import datetime
import pandas as pd

class AnalyseRatios:

    def __init__(self, df):
        self._df = df
        self._today = datetime.now().strftime("%Y%m%d")

    def analyse_pe_ratio(self, ratio):
        self._df.drop(self._df[self._df.pe_ratio > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.pe_ratio < 0].index, inplace=True)

    def analyse_ps_ratio(self, ratio):
        self._df.drop(self._df[self._df.ps_ratio > ratio].index,inplace=True)
        self._df.drop(self._df[self._df.ps_ratio < 0].index,inplace=True)

    def analyse_cash_flow(self, ratio):
        self._df.drop(self._df[self._df.cash_flow > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.cash_flow < 0].index, inplace=True)

    def analyse_pb_ratio(self, ratio):
        self._df.drop(self._df[self._df.pb_ratio > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.pb_ratio <= 0].index, inplace=True)

    def analyse_debt_to_equity(self, ratio):
        self._df.drop(self._df[self._df.debt_to_equity > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.debt_to_equity <= 0].index, inplace=True)
        
    def analyse_dividend_yield(self, ratio):
        #self._df.drop(self._df[self._df.dividend_yield > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.dividend_yield < 0].index, inplace=True)

    def analyse_payout_ratio(self, ratio):
        self._df.drop(self._df[self._df.payout_ratio > ratio].index, inplace=True)
        self._df.drop(self._df[self._df.payout_ratio < 0].index, inplace=True)

    def save_to_csv(self):
        self._df.to_csv("data/%s_analysed_companies.csv" % self._today)
