import matplotlib.pyplot as plt
import numpy as np

class HousingLoan:
    def __init__(self, principal, annual_rate, months):
        self.principal = principal
        self.annual_rate = annual_rate
        self.months = months
        self.monthly_rate = annual_rate / 12 / 100

    def calculate_emi(self):
        emi = self.principal * self.monthly_rate * (1 + self.monthly_rate)**self.months / ((1 + self.monthly_rate)**self.months - 1)
        return emi

    def calculate_amortization_schedule(self):
        emi = self.calculate_emi()
        balance = self.principal
        schedule = []
        
        for _ in range(self.months):
            interest_payment = balance * self.monthly_rate
            principal_payment = emi - interest_payment
            balance -= principal_payment
            schedule.append((emi, interest_payment, principal_payment, balance))
        
        return schedule

    def plot_emi_chart(self):
        schedule = self.calculate_amortization_schedule()
        months = np.arange(1, self.months + 1)
        emis = [x[0] for x in schedule]
        balances = [x[3] for x in schedule]

        plt.figure(figsize=(12, 6))
        plt.plot(months, emis, label='EMI', color='blue')
        plt.plot(months, balances, label='Remaining Balance', color='red')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.title('EMI and Remaining Balance Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()

    def calculate_early_closure_interest(self, remaining_months):
        original_schedule = self.calculate_amortization_schedule()
        remaining_schedule = original_schedule[:remaining_months]
        
        total_paid = sum(x[0] for x in remaining_schedule)
        remaining_balance = remaining_schedule[-1][3] if remaining_months > 0 else 0
        
        total_interest_paid = total_paid - (self.principal - remaining_balance)
        interest_loss_per_month = total_interest_paid / remaining_months if remaining_months > 0 else 0
        
        return interest_loss_per_month

principal = 500000
annual_rate = 7.5
months = 240

loan = HousingLoan(principal, annual_rate, months)
loan.plot_emi_chart()

remaining_months = 120
interest_loss_per_month = loan.calculate_early_closure_interest(remaining_months)
print(f"Interest loss distributed over remaining months: {interest_loss_per_month:.2f}")
