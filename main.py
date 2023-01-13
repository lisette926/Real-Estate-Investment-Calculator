# Name: Lisette Hawkins
# Description: This program will help investors see how much they will earn from buying a rental property
import tkinter
from tkinter import *
from tkinter import ttk
from functions import *

# ---------------------------- INVESTMENT CALCULATOR ------------------------------- #

def calcInvestment():
    # Obtain User Input
    salePrice = float(salePriceLabelEntry.get())
    monthlyHOA = int(monthlyHOAEntry.get())
    state = stateComboBox.get()
    downPaymentPercent = float(downPaymentEntry.get())
    loanType = loanTypeComboBox.get()
    monthlyInterestRate = float(interestRateSpinbox.get()) / 100 / 12
    rent = int(rentalRateEntry.get())

    # Calculations
    downPayment = calcDownPayment(salePrice, downPaymentPercent)
    closingCost = calcClosingCost(salePrice)
    initialInvest = downPayment + closingCost
    taxes = calcTaxes(salePrice, state)
    HOA = yearlyHOA(monthlyHOA)
    principal = salePrice-downPayment
    monthlyPayment = Payment(loanType, monthlyInterestRate, principal)
    yearlyRent = rent * 12
    yearlyInvest = taxes + HOA + (monthlyPayment*12.0)
    profit = yearlyRent - yearlyInvest

    # Output to User
    downPaymentLabel.config(text=f"Down Payment.......................................${downPayment:,.2f}")
    closingCostLabel.config(text=f"Closing Costs.......................................${closingCost:,.2f}")
    initialInvestLabel.config(text=f"Initial Investment.......................................${initialInvest:,.2f}")
    yearlyTaxLabel.config(text=f"Yearly Taxes.......................................${taxes:,.2f}")
    HOALabel.config(text=f"Yearly HOA.......................................${HOA:,.2f}")
    monthlyMortgageLabel.config(text=f"Monthly Principal & Interest.......................................${monthlyPayment:,.2f}")
    yearlyInvestmentLabel.config(text=f"Yearly Investment.......................................${yearlyInvest:,.2f}")
    yearlyRentLabel.config(text=f"Yearly Rent.......................................${yearlyRent:,.2f}")
    totalProfitLabel.config(text=f"Total Profit.......................................${profit:,.2f}")

    if profit > 5000:
        profitIndicatorLabel.config(text="This property is profitable!", fg='green')
    elif profit > 0:
        profitIndicatorLabel.config(text="This property is not the best but profitable!", fg='#A5A52A')
    else:
        profitIndicatorLabel.config(text="This property is NOT profitable!", fg='red')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Real Estate Calculator")
window.geometry("500x800")

# FRAMES
frame = tkinter.Frame(window)
frame.pack()

propertyInfoFrame = tkinter.LabelFrame(frame, text="Property Information")
propertyInfoFrame.grid(row=0, column=0, padx=20, pady=20)

loanInformationFrame = tkinter.LabelFrame(frame, text="Loan Information")
loanInformationFrame.grid(row=1, column=0, padx=20, pady=20)

rentalFrame = tkinter.LabelFrame(frame)
rentalFrame.grid(row=2, column=0, padx=20, pady=20)

# LABELS
salePriceLabel = tkinter.Label(propertyInfoFrame, text="Sale Price")
salePriceLabel.grid(row=0, column=0)

monthlyHOALabel = tkinter.Label(propertyInfoFrame, text="Monthly HOA")
monthlyHOALabel.grid(row=0, column=1)

stateLabel = tkinter.Label(propertyInfoFrame, text="State")
stateLabel.grid(row=0, column=2)

downPaymentPercentLabel = tkinter.Label(loanInformationFrame, text="Down Payment (%)")
downPaymentPercentLabel.grid(row=1, column=0)

loanTypeLabel = tkinter.Label(loanInformationFrame, text="Loan Type")
loanTypeLabel.grid(row=1, column=1)

interestRateLabel = tkinter.Label(loanInformationFrame, text="Interest Rate (%)")
interestRateLabel.grid(row=1, column=2)

rentalRateLabel = tkinter.Label(rentalFrame, text="Estimated Monthly Rent")
rentalRateLabel.grid(row=2, column=0)


# ENTRIES
salePriceLabelEntry = tkinter.Entry(propertyInfoFrame)
salePriceLabelEntry.grid(row=1, column=0)

monthlyHOAEntry = tkinter.Entry(propertyInfoFrame)
monthlyHOAEntry.grid(row=1, column=1)

stateComboBox = ttk.Combobox(propertyInfoFrame, values=['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL',
                                                        'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA',
                                                        'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE',
                                                        'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI',
                                                        'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV',
                                                        'WY'])
stateComboBox.grid(row=1, column=2)

downPaymentEntry = tkinter.Entry(loanInformationFrame)
downPaymentEntry.grid(row=2, column=0)

loanTypeComboBox = ttk.Combobox(loanInformationFrame, values=["15-Year Fixed", "30-Year Fixed"])
loanTypeComboBox.grid(row=2, column=1)

interestRateSpinbox = tkinter.Spinbox(loanInformationFrame, from_=0, to=30)
interestRateSpinbox.grid(row=2, column=2)

rentalRateEntry = tkinter.Entry(rentalFrame)
rentalRateEntry.grid(row=2, column=1)

# PADDING
for widget in propertyInfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
for widget in loanInformationFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# BUTTON
button = tkinter.Button(frame, text="Calculate Investment", command= calcInvestment)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

# OUTPUT
resultsFrame = tkinter.LabelFrame(frame, text="Results")
resultsFrame.grid(row=4, column=0, padx=20, pady=20)

profitFrame = tkinter.LabelFrame(frame, text="Profit")
profitFrame.grid(row=5, column=0, padx=20, pady=20)

downPaymentLabel = Label(resultsFrame, text="", font=("Helvetica", 12))
downPaymentLabel.grid(row=0, column=0)

closingCostLabel = Label(resultsFrame, text="", font=("Helvetica", 12))
closingCostLabel.grid(row=1, column=0)

initialInvestLabel = Label(resultsFrame, text="", font=("Helvetica", 12), fg='red')
initialInvestLabel.grid(row=2, column=0)

yearlyTaxLabel = Label(resultsFrame, text="", font=("Helvetica", 12))
yearlyTaxLabel.grid(row=3, column=0)

HOALabel = Label(resultsFrame, text="", font=("Helvetica", 12))
HOALabel.grid(row=4, column=0)

monthlyMortgageLabel = Label(resultsFrame, text="", font=("Helvetica", 12))
monthlyMortgageLabel.grid(row=5, column=0)

yearlyInvestmentLabel = Label(resultsFrame, text="", font=("Helvetica", 12), fg='red')
yearlyInvestmentLabel.grid(row=6, column=0)

yearlyRentLabel = Label(profitFrame, text="", font=("Helvetica", 12))
yearlyRentLabel.grid(row=0, column=0)

totalProfitLabel = Label(profitFrame, text="", font=("Helvetica", 12), fg='red')
totalProfitLabel.grid(row=1, column=0)

profitIndicatorLabel = Label(profitFrame, text="", font=("Helvetica", 18))
profitIndicatorLabel.grid(row=2, column=0)


window.mainloop()
