from tabulate import tabulate
import locale
import matplotlib.pyplot as plt
locale.setlocale(locale.LC_NUMERIC, 'de_DE')

def calculate(starting_value, real_rate, savingsrate_monthly, years):

    interest_gesamt = 0
    einlagen_gesamt = starting_value
    einlagen_data = []
    interest_data = []
    gesamt_data = []

    for year in range(0, years):
        interest = starting_value * (real_rate / 100)
        interest_gesamt += interest

        einlagen_gesamt += savingsrate_monthly * 12
        einlagen_data.append(einlagen_gesamt)
        interest_data.append(interest_gesamt)

        starting_value = starting_value * (1 + (real_rate) / 100) + savingsrate_monthly * 12
        gesamt_data.append(starting_value)

    # Plotting
    plt.plot(range(1, years + 1), einlagen_data, label='Einlagen')
    plt.plot(range(1, years + 1), interest_data, label='Interest')
    plt.plot(range(1, years + 1), gesamt_data, label='Gesamt')
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.legend()
    plt.title('Einlagen and Interest Over the Years')
    plt.show()

    return round(starting_value, 2), interest_gesamt, einlagen_gesamt


def main():
    starting_value = 0 
    inflation_rate = 2 
    interest_rate_yearly = 9 
    savingsrate_monthly = 1500  
    years = 36
    capital_tax = 30

    real_rate = interest_rate_yearly - inflation_rate

    result, interest_gesamt, einlagen_gesamt = calculate(starting_value, real_rate, savingsrate_monthly, years)

    # ohne und mit steuern 
    # lassen inflationsanpassungen der Sparrate weg und betrachten die Kaufkfraft, als wenn es heute wäre 
    # wissen aber das die Sparrate um die zukünftige Kaufkraft des Sparziels zu erreichen mit der INfaltion steigen muss
    tax_to_be_payed = interest_gesamt * (capital_tax / 100)

    print(f"The worth will be {result} in {years} years.")
    print(f"Thereof own contributions will be: {einlagen_gesamt}")
    print(f"Thereof interest will be: {interest_gesamt}")
    print(f"Thereof tax must be payed: {tax_to_be_payed}")
    print(f"The net worth will be {result - tax_to_be_payed}")

if __name__ == "__main__":
    main()