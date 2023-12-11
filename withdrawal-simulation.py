from tabulate import tabulate
import locale
import matplotlib.pyplot as plt
locale.setlocale(locale.LC_NUMERIC, 'de_DE')

def calculate_years(net_worth, inflation_rate, interest_rate, first_year_withdrawal, show_table, show_graph):
    
    table_data = [["Year", "Net Worth", "Withdrawal Amount", "X"]]

    net_worth_values = []
    years_values = []

    years = 1
    x = net_worth / first_year_withdrawal

    while net_worth > 0 and years < 100:
        formatted_net_worth = locale.format('%.2f', net_worth, grouping=True)
        formatted_withdrawal = locale.format('%.2f', first_year_withdrawal, grouping=True)
        x = round(net_worth / first_year_withdrawal, 0)
        table_data.append([years, formatted_net_worth, formatted_withdrawal, x])

        net_worth_values.append(net_worth)
        years_values.append(years)

        net_worth = net_worth * (1 + interest_rate / 100) - first_year_withdrawal
        first_year_withdrawal = first_year_withdrawal * (1 + inflation_rate / 100)
        years += 1

    if(show_table):
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

    if(show_graph):
        plt.plot(years_values, net_worth_values, label='Net Worth')
        plt.xlabel('Years')
        plt.ylabel('Net Worth')
        plt.title('Net Worth Over Years')
        plt.legend()
        plt.grid(True)
        plt.show()

    return min(years - 1, 100)

def main():
    net_worth = 1800000
    inflation_rate = 2 
    interest_rate = 3 
    withdrawal_rate = 2.2 

    first_year_withdrawal = net_worth * (withdrawal_rate / 100)

    result = calculate_years(net_worth, inflation_rate, interest_rate, first_year_withdrawal, show_table=True, show_graph=True)

    print(f"The net worth will be positive for {result} years.")

if __name__ == "__main__":
    main()
