def calcDownPayment(price, DPPercent):
    return (DPPercent/100)*price

def calcClosingCost(price):
    return price*0.04

def calcTaxes(price, state):
    # tax rates are in percent
    taxRate = {'AK': 1.19, 'AL': 0.41, 'AR': 0.62, 'AZ': 0.66, 'CA': 0.76, 'CO': 0.51, 'CT': 2.14,
               'DC': 0.56, 'DE': 0.57, 'FL': 0.89, 'GA': 0.92, 'HI': 0.28, 'IA': 1.57, 'ID': 0.69,
               'IL': 2.27, 'IN': 0.85, 'KS': 1.41, 'KY': 0.86, 'LA': 0.55, 'MA': 1.23, 'MD': 1.09,
               'ME': 1.36, 'MI': 1.54, 'MN': 1.12, 'MO': 0.97, 'MS': 0.81, 'MT': 0.84, 'NC': 0.84,
               'ND': 0.98, 'NE': 1.73, 'NH': 2.18, 'NJ': 2.49, 'NM': 0.80, 'NV': 0.60, 'NY': 1.72,
               'OH': 1.56, 'OK': 0.90, 'OR': 0.97, 'PA': 1.58, 'RI': 1.63, 'SC' : 0.57, 'SD': 1.31,
               'TN': 0.71, 'TX': 1.80, 'UT': 0.63, 'VA': 0.82, 'VT': 1.90, 'WA': 0.98, 'WI': 1.85,
               'WV': 0.58, 'WY': 0.61}
    return float((taxRate[state]/100) * price)


def yearlyHOA(monthlyHOA):
    return monthlyHOA*12

def Payment(loanType, monthlyInterestRate, principal):
    # 15 years = 180 months
    # 30 years = 360 months
    if loanType == "15-Year Fixed":
        monthlyPayment = (monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-180))) * principal
    else:
        monthlyPayment = (monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-360))) * principal
    #monthlyPayment = f"{monthlyPayment:,.2f}"
    return monthlyPayment
