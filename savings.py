

def calculate_savings(income, business_revenue, saving_percentage, months):
    total_earnings = (income + business_revenue) * months
    savings = (saving_percentage / 100) * total_earnings
    return savings

def main():
    print("Savings Calculator in South Africa")

    income = float(input("Enter your monthly income (in ZAR): "))
    business_revenue = float(input("Enter your monthly business revenue (in ZAR): "))
    saving_percentage = float(input("Enter the percentage of your total earnings you wish to save: "))
    months = int(input("Enter the number of months: "))

    savings = calculate_savings(income, business_revenue, saving_percentage, months)

    print(f"Your total savings after {months} months will be: R{round(savings, 2)}")

if __name__ == "__main__":
    main()