from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError, ContentTooShortError
import bs4

from base_scrapper import BaseScrapper

class InvestingIncomeStatementScrapper(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)
        self._html = self._soup.find_all("td")

        self._years = self.get_year()
        self._total_revenue = self.get_total_revenue()
        self._revenue = self.get_revenue()
        self._other_revenue = self.get_other_revenue()
        self._total_cost_of_revenue = self.get_total_cost_of_revenue()
        self._gross_profit = self.get_gross_profit()
        self._total_operating_expenses = self.get_tot_operating_expenses()
        self._total_general_expenses = self.get_tot_general_expenses()
        self._research_expenses = self.get_research_expenses()
        self._depreciation_amortization = self.get_depreciation_amortization()
        self._interest_expense_income_net_operating = self.get_interest_expense_income_net_operating()
        self._unusual_expense = self.get_unusual_expense()
        self._other_operating_expenses = self.get_other_operating_expenses()
        self._operating_income = self.get_operating_income()
        self._get_interest_income = self.get_interest_income():
        self._gain_on_sales_of_assets = self.get_gain_on_sales_of_assets()
        self._net_other = self.get_net_other()
        self._net_income_before_taxes = self.get_net_income_before_taxes()
        self._provision_for_income_taxes = self.get_provision_for_income_taxes()
        self._net_income_after_taxes = self.get_net_income_after_taxes()
        self._minority_interest = self.get_minority_interest()
        self._equity_in_affiliates = self.get_equity_in_affiliates()
        self._us_gaap_adjustment = self.get_us_gaap_adjustment()
        self._net_income_before_extraordinary_items = self.get_net_income_before_extraordinary_items()
        self._total_extraordinary_items = self.get_total_extraordinary_items()
        self._net_income = self.get_net_income()
        self._total_adjustments_to_net_income = self.get_total_adjustments_to_net_income()
        self._income_avaliable_to_common_excluding_extraordinary_items = self.get_income_avaliable_to_common_excluding_extraordinary_items()
        self._diultion_adjustment = self.get_dilution_adjustment()
        self._diluted_net_income = self.get_diluted_net_income()
        self._diluted_weighted_average_shares = self.get_diluted_weighted_average_shares()
        self._diluted_eps_excluding_extraordinary_items = self.get_diluted_eps_excluding_extraordinary_items()
        self._dps_comon_stock_primary_issue= self.get_dps_common_stock_primary_issue()
        self._diluted_normalised_eps = self.get_diluted_normalised_eps()
    
    def get_year(self):
        years = []
        for i in range(1, 5):
            year = self._html[7].find_all("th")[i].text[:5]
            years.append(year)

        return years

    def get_total_revenue(self):
        holder = []
        for i in range(1, 5):
            total_revenue = self._html[8].find_all("td")[i].text
            holder.append(total_revenue)

        return holder

    def get_revenue(self):
        holder = []
        for i in range(1, 5):
            revenue = self._html[10].find_all("td")[i].text
            holder.append(revenue)

        return holder

    def get_other_revenue(self):
        holder = []
        for i in range(1, 5):
            revenue = self._html[11].find_all("td")[i].text
            holder.append(revenue)

        return holder

    def get_total_cost_of_revenue(self):
        holder = []
        for i in range(1, 5):
            revenue = self._html[12].find_all("td")[i].text
            holder.append(revenue)

        return holder

    def get_gross_profit(self):
        holder = []
        for i in range(1,5):
            gross_profit = self._html[13].find_all("td")[i].text
            holder.append(gross_profit)

        return holder

    def get_tot_operating_expenses(self):
        holder = []
        for i in range(1,5):
            tot_op_exp = self._html[14].find_all("td")[i].text
            holder.append(tot_op_exp)

        return holder

    def get_tot_general_expenses(self):
        holder = []
        for i in range(1,5):
            tot_general_exp = self._html[16].find_all("td")[i].text
            holder.append(tot_general_exp)

        return holder

    def get_research_expenses(self):
        holder = []
        for i in range(1,5):
            exp = self._html[17].find_all("td")[i].text
            holder.append(exp)

        return holder

    def get_depreciation_amortization(self):
        holder = []
        for i in range(1,5):
            exp = self._html[18].find_all("td")[i].text
            holder.append(exp)

        return holder

    def get_interest_expense_income_net_operating(self):
        holder = []
        for i in range(1,5):
            exp = self._html[19].find_all("td")[i].text
            holder.append(exp)

        return holder

    def get_unusual_expense(self):
        holder = []
        for i in range(1,5):
            exp = self._html[20].find_all("td")[i].text
            holder.append(exp)

        return holder

    def get_other_operating_expenses(self):
        holder = []
        for i in range(1,5):
            exp = self._html[21].find_all("td")[i].text
            holder.append(exp)

        return holder

    def get_operating_income(self):
        holder = []
        for i in range(1,5):
            income = self._html[22].find_all("td")[i].text
            holder.append(income)

        return holder

    def get_interest_income(self):
        holder = []
        for i in range(1,5):
            income = self._html[23].find_all("td")[i].text
            holder.append(income)

        return holder

    def get_gain_on_sales_of_assets(self):
        holder = []
        for i in range(1,5):
            gain = self._html[24].find_all("td")[i].text
            holder.append(gain)

        return holder

    def get_net_other(self):
        holder = []
        for i in range(1,5):
            other = self._html[25].find_all("td")[i].text
            holder.append(other)

        return holder

    def get_net_income_before_taxes(self):
        holder = []
        for i in range(1,5):
            nibt = self._html[26].find_all("td")[i].text
            holder.append(nibt)

        return holder

    def get_provision_for_income_taxes(self):
        holder = []
        for i in range(1,5):
            pfit = self._html[27].find_all("td")[i].text
            holder.append(pfit)

        return holder

    def get_net_income_after_taxes(self):
        holder = []
        for i in range(1,5):
            niat = self._html[28].find_all("td")[i].text
            holder.append(niat)

        return holder

    def get_minority_interest(self):
        holder = []
        for i in range(1,5):
            interest = self._html[29].find_all("td")[i].text
            holder.append(interest)

        return holder

    def get_equity_in_affiliates(self):
        holder = []
        for i in range(1,5):
            equity = self._html[30].find_all("td")[i].text
            holder.append(equity)

        return holder

    def get_us_gaap_adjustment(self):
        holder = []
        for i in range(1,5):
            adj = self._html[31].find_all("td")[i].text
            holder.append(adj)

        return holder

    def get_net_income_before_extraordinary_items(self):
        holder = []
        for i in range(1,5):
            income = self._html[32].find_all("td")[i].text
            holder.append(income)

        return holder

    def get_total_extraordinary_items(self):
        holder = []
        for i in range(1,5):
            tot = self._html[33].find_all("td")[i].text
            holder.append(tot)

        return holder

    def get_net_income(self):
        holder = []
        for i in range(1,5):
            income = self._html[34].find_all("td")[i].text
            holder.append(income)

        return holder

    def get_total_adjustments_to_net_income(self):
        holder = []
        for i in range(1,5):
            adj = self._html[35].find_all("td")[i].text
            holder.append(adj)

        return holder

    def get_income_avaliable_to_common_excluding_extraordinary_items(self):
        holder = []
        for i in range(1,5):
            income = self._html[36].find_all("td")[i].text
            holder.append(income)

        return holder

    def get_dilution_adjustment(self):
        holder = []
        for i in range(1,5):
            adj = self._html[37].find_all("td")[i].text
            holder.append(adj)

        return holder

    def get_diluted_net_income(self):
        holder = []
        for i in range(1,5):
            income = self._html[38].find_all("td")[i].text
            holder.append(income)

        return holder

    def get_diluted_weighted_average_shares(self):
        holder = []
        for i in range(1,5):
            exp = self._html[39].find_all("td")[i].text
            holder.append(exp)

        return holder

    def get_diluted_eps_excluding_extraordinary_items(self):
        holder = []
        for i in range(1,5):
            eps = self._html[40].find_all("td")[i].text
            holder.append(eps)

        return holder

    def get_dps_common_stock_primary_issue(self):
        holder = []
        for i in range(1,5):
            dps = self._html[41].find_all("td")[i].text
            holder.append(dps)

        return holder

    def get_diluted_normalised_eps(self):
        holder = []
        for i in range(1,5):
            eps = self._html[42].find_all("td")[i].text
            holder.append(eps)

        return holder

class InvestingBalanceSheetScrapper(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)

class InvestingCashFlowScrapper(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)

class InvestingDividendsScrapper(BaseScrapper):

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)

class InvestingRatioScrapper(BaseScrapper):

    """
    The company class stores metrics for analysis.
    The metrics are taken from uk.investing.com.
    """

    def __init__(self, webpage):
        BaseScrapper.__init__(self, webpage)
        self._html = self._soup.find_all("tr",{"class":"child"})
        
        if not self._html == None: 
            self._pe_ratio = self.get_pe_ratio()
            self._ps_ratio = self.get_ps_ratio()
            self._cash_flow = self.get_cash_flow()
            self._free_cash_flow = self.get_free_cash_flow()
            self._pb_ratio = self.get_pb_ratio()
            self._tangible_pb_ratio = self.get_tangible_pb_ratio()
            
            self._gross_margin_ttm = self.get_gross_margin_ttm()
            self._gross_margin_5ya = self.get_gross_margin_5ya()
            self._operating_margin_ttm = self.get_operating_margin_ttm()
            self._operating_margin_5ya = self.get_operating_margin_5ya()
            self._pretax_margin_ttm = self.get_pretax_margin_ttm()
            self._pretax_margin_5ya = self.get_pretax_margin_5ya()
            self._net_profit_margin_ttm = self.get_net_profit_margin_ttm()
            self._net_profit_margin_5ya = self.get_net_profit_margin_5ya()
            
            self._revenue_per_share = self.get_revenue_per_share()
            self._basic_eps = self.get_basic_eps()
            self._diluted_eps = self.get_diluted_eps()
            self._book_value_per_share = self.get_book_value_per_share()
            self._tangible_book_value_per_share = self.get_tangible_book_value_per_share()
            self._cash_per_share = self.get_cash_per_share()
            self._cash_flow_per_share = self.get_cash_flow_per_share()
            
            self._return_on_equity_ttm = self.get_return_on_equity_ttm()
            self._return_on_equity_5ya = self.get_return_on_equity_5ya()
            self._return_on_assets_ttm = self.get_return_on_assets_ttm()
            self._return_on_assets_5ya = self.get_return_on_assets_5ya()
            self._return_on_investment_ttm = self.get_return_on_investment_ttm()
            self._return_on_investment_5ya = self.get_return_on_investment_5ya()
            
            self._eps_mrq_vs_mrq_1yr_ago = self.get_eps_mrq_vs_mrq_1yr_ago()
            self._eps_ttm_vs_ttm_1yr_ago = self.get_eps_ttm_vs_ttm_1yr_ago()
            self._eps_growth_5ya = self.get_eps_growth_5ya()
            self._sale_mrq_vs_qtr_1ya_ago = self.get_eps_mrq_vs_mrq_1yr_ago()
            self._sale_ttm_vs_ttm_1ya_ago = self.get_eps_ttm_vs_ttm_1yr_ago()
            self._sales_growth_5ya = self.get_sales_growth_5ya()
            self._capital_spending_growth_5ya = self.get_capital_spending_growth_5ya()
            
            self._quick_ratio = self.get_quick_ratio()
            self._current_ratio = self.get_current_ratio()
            self._lt_debt_to_equity = self.get_lt_debt_to_equity()
            self._total_debt_to_equity = self.get_total_debt_to_equity()
            
            self._asset_turnover = self.get_asset_turnover()
            self._inventory_turnover = self.get_inventory_turnover()
            self._revenue_per_employee = self.get_revenue_per_employee()
            self._net_income_per_employee = self.get_net_income_per_employee()
            self._receivable_turnover = self.get_receivable_turnover()
            
            self._dividend_yield = self.get_dividend_yield()
            self._dividend_yield_5ya = self.get_dividend_yield_5ya()
            self._dividend_growth_rate = self.get_dividend_growth_rate()
            self._payout_ratio = self.get_payout_ratio()
            
    def get_pe_ratio(self):
        try:
            pe_ratio = self._html[0].find_all("td",{"class":""})
            if pe_ratio[1].text.replace(",","") == "-" or pe_ratio[1].text.replace(",","") == "":
                return -999
            else:
                return float(pe_ratio[1].text.replace(",",""))
        except:
            return -999
        
    def get_ps_ratio(self):
        try:
            ps_ratio = self._html[1].find_all("td",{"class":""})
            if ps_ratio[1].text.replace(",","") == "-" or ps_ratio[1].text.replace(",","") == "" :
                return -999
            else:
                return float(ps_ratio[1].text.replace(",",""))
        except:
            return -999
        
    def get_cash_flow(self):
        try:
            cash_flow = self._html[2].find_all("td",{"class":""})
            if cash_flow[1].text.replace(",","") == "-" or cash_flow[1].text.replace(",","") == "":
                    return -999
            else:
                return float(cash_flow[1].text.replace(",",""))
        except:
            return -999

    def get_free_cash_flow(self):
        try:
            cash_flow = self._html[3].find_all("td",{"class":""})
            if cash_flow[1].text.replace(",","") == "-" or cash_flow[1].text.replace(",","") == "":
                    return -999
            else:
                return float(cash_flow[1].text.replace(",",""))
        except:
            return -999

    def get_pb_ratio(self):
        try:
            pb_ratio = self._html[4].find_all("td",{"class":""})
            if pb_ratio[1].text.replace(",","") == "-" or pb_ratio[1].text.replace(",","") == "":
                return -999
            else:
                return float(pb_ratio[1].text.replace(",",""))
        except:
            return -999

    def get_tangible_pb_ratio(self):
        try:
            pb_ratio = self._html[5].find_all("td",{"class":""})
            if pb_ratio[1].text.replace(",","") == "-" or pb_ratio[1].text.replace(",","") == "":
                return -999
            else:
                return float(pb_ratio[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_gross_margin_ttm(self):
        try:
            gross_margin = self._html[7].find_all("td",{"class":""})
            if gross_margin[1].text.replace(",","") == "-" or gross_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(gross_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_gross_margin_5ya(self):
        try:
            gross_margin = self._html[8].find_all("td",{"class":""})
            if gross_margin[1].text.replace(",","") == "-" or gross_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(gross_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_operating_margin_ttm(self):
        try:
            operating_margin = self._html[9].find_all("td",{"class":""})
            if operating_margin[1].text.replace(",","") == "-" or operating_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(operating_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_operating_margin_5ya(self):
        try:
            operating_margin = self._html[10].find_all("td",{"class":""})
            if operating_margin[1].text.replace(",","") == "-" or operating_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(operating_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_pretax_margin_ttm(self):
        try:
            pretax_margin = self._html[11].find_all("td",{"class":""})
            if pretax_margin[1].text.replace(",","") == "-" or pretax_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(pretax_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_pretax_margin_5ya(self):
        try:
            pretax_margin = self._html[12].find_all("td",{"class":""})
            if pretax_margin[1].text.replace(",","") == "-" or pretax_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(pretax_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_net_profit_margin_ttm(self):
        try:
            net_profit_margin = self._html[13].find_all("td",{"class":""})
            if net_profit_margin[1].text.replace(",","") == "-" or net_profit_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(net_profit_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_net_profit_margin_5ya(self):
        try:
            net_profit_margin = self._html[14].find_all("td",{"class":""})
            if net_profit_margin[1].text.replace(",","") == "-" or net_profit_margin[1].text.replace(",","") == "":
                return -999
            else:
                return float(net_profit_margin[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_revenue_per_share(self):
        try:
            revenue_per_share = self._html[15].find_all("td",{"class":""})
            if revenue_per_share[1].text.replace(",","") == "-" or revenue_per_share[1].text.replace(",","") == "":
                return -999
            else:
                return float(revenue_per_share[1].text.replace(",",""))
        except:
            return -999

    def get_basic_eps(self):
        try:
            basic_eps = self._html[16].find_all("td",{"class":""})
            if basic_eps[1].text.repace(",","") == "-" or basic_eps[1].text.repace(",","") == "":
                return -999
            else:
                return float(basic_eps[1].text.replace(",",""))
        except:
            return -999

    def get_diluted_eps(self):
        try:
            diluted_eps = self._html[17].find_all("td",{"class":""})
            if diluted_eps[1].text.repace(",","") == "-" or diluted_eps[1].text.repace(",","") == "":
                return -999
            else:
                return float(diluted_eps[1].text.replace(",",""))
        except:
            return -999

    def get_book_value_per_share(self):
        try:
            book_value_per_share = self._html[18].find_all("td",{"class":""})
            if book_value_per_share[1].text.repace(",","") == "-" or book_value_per_share[1].text.repace(",","") == "":
                return -999
            else:
                return float(book_value_per_share[1].text.replace(",",""))
        except:
            return -999

    def get_tangible_book_value_per_share(self):
        try:
            tangible_book_value_per_share = self._html[19].find_all("td",{"class":""})
            if tangible_book_value_per_share[1].text.repace(",","") == "-" or tangible_book_value_per_share[1].text.repace(",","") == "":
                return -999
            else:
                return float(tangible_book_value_per_share[1].text.replace(",",""))
        except:
            return -999

    def get_cash_per_share(self):
        try:
            cash_per_share = self._html[20].find_all("td",{"class":""})
            if cash_per_share[1].text.repace(",","") == "-" or cash_per_share[1].text.repace(",","") == "":
                return -999
            else:
                return float(cash_per_share[1].text.replace(",",""))
        except:
            return -999

    def get_cash_flow_per_share(self):
        try:
            cash_flow_per_share = self._html[21].find_all("td",{"class":""})
            if cash_flow_per_share[1].text.repace(",","") == "-" or cash_flow_per_share[1].text.repace(",","") == "":
                return -999
            else:
                return float(cash_flow_per_share[1].text.replace(",",""))
        except:
            return -999

    def get_return_on_equity_ttm(self):
        try:
            return_on_equity = self._html[23].find_all("td",{"class":""})
            if return_on_equity[1].text.repace(",","") == "-" or return_on_equity[1].text.repace(",","") == "":
                return -999
            else:
                return float(return_on_equity[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_return_on_equity_5ya(self):
        try:
            return_on_equity = self._html[24].find_all("td",{"class":""})
            if return_on_equity[1].text.repace(",","") == "-" or return_on_equity[1].text.repace(",","") == "":
                return -999
            else:
                return float(return_on_equity[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_return_on_assets_ttm(self):
        try:
            return_on_assets = self._html[25].find_all("td",{"class":""})
            if return_on_assets[1].text.repace(",","") == "-" or return_on_assets[1].text.repace(",","") == "":
                return -999
            else:
                return float(return_on_assets[1].text.replace(",",""))
        except:
            return -999

    def get_return_on_assets_5ya(self):
        try:
            return_on_assets = self._html[26].find_all("td",{"class":""})
            if return_on_assets[1].text.repace(",","") == "-" or return_on_assets[1].text.repace(",","") == "":
                return -999
            else:
                return float(return_on_assets[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_return_on_investment_ttm(self):
        try:
            return_on_investment = self._html[27].find_all("td",{"class":""})
            if return_on_investment[1].text.repace(",","") == "-" or return_on_investment[1].text.repace(",","") == "":
                return -999
            else:
                return float(return_on_investment[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_return_on_investment_5ya(self):
        try:
            return_on_investment = self._html[28].find_all("td",{"class":""})
            if return_on_investment[1].text.repace(",","") == "-" or return_on_investment[1].text.repace(",","") == "":
                return -999
            else:
                return float(return_on_investment[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_eps_mrq_vs_mrq_1yr_ago(self):
        try:
            eps_mrq = self._html[29].find_all("td",{"class":""})
            if eps_mrq[1].text[:-1].replace(",","") == "-" or eps_mrq[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(eps_mrq[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_eps_ttm_vs_ttm_1yr_ago(self):
        try:
            eps_ttm = self._html[30].find_all("td",{"class":""})
            if eps_ttm[1].text[:-1].replace(",","") == "-" or eps_ttm[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(eps_ttm[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_eps_growth_5ya(self):
        try:
            eps_growth = self._html[31].find_all("td",{"class":""})
            if eps_growth[1].text[:-1].replace(",","") == "-" or eps_growth[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(eps_growth[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_sales_mrq_vs_qtr_1yr_ago(self):
        try:
            sales_mrq = self._html[32].find_all("td",{"class":""})
            if sales_mrq[1].text[:-1].replace(",","") == "-" or sales_mrq[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(sales_mrq[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_sales_ttm_vs_ttm_1yr_ago(self):
        try:
            sales_ttm = self._html[33].find_all("td",{"class":""})
            if sales_ttm[1].text[:-1].replace(",","") == "-" or sales_ttm[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(sales_ttm[1].text[:-1].replace(",",""))
        except:
            return -999
        
    def get_sales_growth_5ya(self):
        try:
            sales_growth = self._html[34].find_all("td",{"class":""})
            if sales_growth[1].text[:-1].replace(",","") == "-" or sales_growth[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(sales_growth[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_capital_spending_growth_5ya(self):
        try:
            capital_spending_growth = self._html[35].find_all("td",{"class":""})
            if capital_spending_growth[1].text[:-1].replace(",","") == "-" or capital_spending_growth[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(capital_spending_growth[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_quick_ratio(self):
        try:
            quick_ratio = self._html[36].find_all("td",{"class":""})
            if quick_ratio[1].text[:-1].replace(",","") == "-" or quick_ratio[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(quick_ratio[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_current_ratio(self):
        try:
            current_ratio = self._html[37].find_all("td",{"class":""})
            if current_ratio[1].text[:-1].replace(",","") == "-" or current_ratio[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(current_ratio[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_lt_debt_to_equity(self):
        try:
            debt_to_equity = self._html[38].find_all("td",{"class":""})
            if debt_to_equity[1].text[:-1].replace(",","") == "-" or debt_to_equity[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(debt_to_equity[1].text[:-1].replace(",",""))
        except:
            return -999
        
    def get_total_debt_to_equity(self):
        try:
            debt_to_equity = self._html[39].find_all("td",{"class":""})
            if debt_to_equity[1].text[:-1].replace(",","") == "-" or debt_to_equity[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(debt_to_equity[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_asset_turnover(self):
        try:
            asset_turnover = self._html[40].find_all("td",{"class":""})
            if asset_turnover[1].text.replace(",","") == "-" or asset_turnover[1].text.replace(",","") == "":
                return -999
            else:
                return float(asset_turnover[1].text.replace(",",""))
        except:
            return -999

    def get_inventory_turnover(self):
        try:
            inventory_turnover = self._html[41].find_all("td",{"class":""})
            if inventory_turnover[1].text.replace(",","") == "-" or inventory_turnover[1].text.replace(",","") == "":
                return -999
            else:
                return float(inventory_turnover[1].text.replace(",",""))
        except:
            return -999

    def get_revenue_per_employee(self):
        try:
            revenue_per_employee = self._html[42].find_all("td",{"class":""})
            if revenue_per_employee[1].text[:-1].replace(",","") == "-" or revenue_per_employee[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(revenue_per_employee[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_net_income_per_employee(self):
        try:
            net_income_per_employee = self._html[43].find_all("td",{"class":""})
            if net_income_per_employee[1].text[:-1].replace(",","") == "-" or net_income_per_employee[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(net_income_per_employee[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_receivable_turnover(self):
        try:
            receivable_turnover = self._html[44].find_all("td",{"class":""})
            if receivable_turnover[1].text.replace(",","") == "-" or receivable_turnover[1].text.replace(",","") == "":
                return -999
            else:
                return float(receivable_turnover[1].text.replace(",",""))
        except:
            return -999

    def get_dividend_yield(self):
        try:
            dividend_yield = self._html[45].find_all("td",{"class":""})
            if dividend_yield[1].text[:-1].replace(",","") == "-" or dividend_yield[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(dividend_yield[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_dividend_yield_5ya(self):
        try:
            dividend_yield = self._html[46].find_all("td",{"class":""})
            if dividend_yield[1].text[:-1].replace(",","") == "-" or dividend_yield[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(dividend_yield[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_dividend_growth_rate(self):
        try:
            dividend_growth_rate = self._html[47].find_all("td",{"class":""})
            if dividend_growth_rate[1].text[:-1].replace(",","") == "-" or dividend_growth_rate[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(dividend_growth_rate[1].text[:-1].replace(",",""))
        except:
            return -999

    def get_payout_ratio(self):
        try:
            payout_ratio = self._html[48].find_all("td",{"class":""})
            if payout_ratio[1].text[:-1].replace(",","") == "-" or payout_ratio[1].text[:-1].replace(",","") == "":
                return -999
            else:
                return float(payout_ratio[1].text[:-1].replace(",",""))
        except:
            return -999
        
#company = Company("https://uk.investing.com/equities/avast-holdings-ratios")
#print(company._pe_ratio)
#print(company._ps_ratio)
#print(company._cash_flow)
#print(company._pb_ratio)
#print(company._dividend_yield)
#print(company._payout_ratio)
