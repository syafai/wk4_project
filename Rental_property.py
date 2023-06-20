class calculate_ROI():
    def __init__(self, property_price, mortgage):
        self.property_price = property_price
        self.rent = 0
        self.units = 0
        self.monthly_income = 0
        self.yearly_income = 0
        self.mortgage = 0
        self.monthly_utility = 0
        self.money_set_aside = 0
        self.laundry_income = 0
        self.other_income = 0
        self.monthly_income = 0
        self.total_monthly_money_set_aside = 0

    def cost_property(self):
        while True:
            prop_price = (input("What is the total price of the property? $"))
            try:
                self.property_price = int(prop_price)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

        while True:
            d_payment = (input("How much was your down payment? $"))
            try:
                down_payment = int(d_payment)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

        while True:
            c_cost =  (input("How much was your closing cost? $"))
            try:
                closing_cost = int(c_cost)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

        while True:        
            r_money = (input("Enter the amount you spent fixing the house. Enter 0 if you spent none. $"))
            try:
                rehab_money = int(r_money)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")  
        print("")

        self.total_investment = int(down_payment + closing_cost + rehab_money)
        print(f"Your total investment is ${self.total_investment:.2f} ")
        print("")


    def rental_income(self):
        print("")
        while True:
            rnt = input("How much are you charging for rent? $")
            try:
                rent = int(rnt)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only. ")
            
        while True:
            unts = input("How many units are available for rent? ")
            try:
                units = int(unts)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only. ")
        
        self.rent_income = int(units * rent)
        print("")
        print(f"Your monthly income from rent is ${self.rent_income:.2f}")
        print("")
    

    def laundry(self):
        while True:
            laundry_use = input("On average, what would you say is the monthly income from laundry services at your property? $")
            try:
                self.laundry_income = int(laundry_use)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

    def other_income_(self):
        while True:
            otr_income = (input("Enter the average of any other income you have: $"))
            try:
                self.other_income = int(otr_income)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

    
    def income(self):
        self.monthly_income = int(self.rent_income + self.laundry_income + self.other_income)
        print(f"Your total monthly income is ${self.monthly_income:.2f}")
        print("")





class Expenses(calculate_ROI):
    def __init__(self, property_price):
        super().__init__(property_price, mortgage=None)


    def mortgage_(self):
        print("")
        self.mortgage = int(input(f"Enter your monthly mortgage bill: $"))
        print("")

    def utilities(self):
        print("Enter any bills that you are paying. Enter 0 if the tenent is paying. ")
        while True:
            gs = (input("Enter your monthly gas bill: $"))
            try:
                gas = int(gs)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

        while True:
            wtr = (input("Enter your monthly water bill: $"))
            try:
                water = int(wtr)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

        while True:
            eltc = (input("Enter your monthly electric bill: $"))
            try:
                electric = int(eltc)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

        while True:
            grbg = (input("Enter your monthly garbage bill: $"))
            try:
                garbage = int(grbg)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

        while True:
            swr = (input("Enter your monthly sewer bill: $"))
            try:
                sewer = int(swr)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")

        while True:
            mangment = (input("Enter the property manager monthly pay. Enter 0 if there is none. $"))
            try:
                property_mangment = int(mangment)
                break
            except ValueError:
                print("That is an invalid entry. Please enter numbers only.")
        
        self.total_monthly_utility = int(gas + water + electric + garbage + sewer + property_mangment)

        print("")
        print(f"Your monthly utility bill is ${self.total_monthly_utility:.2f}")
        print("")


    def set_aside(self):
        print("")
        print("We will be setting aside 5 percent of your monthly total income just in case for any repairs, vacancy or capital expenditures")
        vacancy = int(self.monthly_income * .05)
        repairs = int(self.monthly_income * .05)
        cap_expense = int(self.monthly_income * .05)

        self.total_monthly_money_set_aside = int(vacancy + repairs + cap_expense)

        print(f"This is the recommended amount you should set aside each month: ${self.total_monthly_money_set_aside:.2f} ")
        print("")


    def monthly_expenses(self):
        self.total_expenses = float(self.total_monthly_utility + self.total_monthly_money_set_aside + self.mortgage)

        print(f"Your total monthly expenses is ${self.total_expenses:.2f}")
        print("")

    def cash_flow(self):
        self.total_monthly_cashflow = self.monthly_income - self.total_expenses

        print(f"Your monthly cash flow is: ${self.total_monthly_cashflow:.2f}")
        print("")

    def coc_ROI(self):
        self.yearly_cashflow = int(self.total_monthly_cashflow * 12)

        self.coc_roi = float((self.yearly_cashflow / self.total_investment ) * 100)

        print(f"Your cash on cash return on investment is {self.coc_roi:.2f}%")
        print("")



class Main():
    def run(self):
        main_rental = Expenses(property_price=None)

        print("Welcome to SKY Firm! Let us calculate your return on investment")
        main_rental.cost_property()
        main_rental.rental_income()

        response1 = input("Do you have laundry service at your property? Enter 'Y' for Yes | 'N' for No ")
        if response1.lower() == 'y':
            main_rental.laundry()
        elif response1.lower() == 'n':
            self.laundry_income = 0

        response2 = input("Do have any other monthly income? Enter 'Y' for Yes| 'N' for No. ")
        if response2.lower() == 'y':
            main_rental.other_income_()
        elif response2.lower() == 'n':
            self.laundry_income = 0
    
        main_rental.mortgage_()
        main_rental.utilities()
        main_rental.income()
        main_rental.set_aside()
        main_rental.monthly_expenses()
        main_rental.cash_flow()
        main_rental.coc_ROI()



main_income = Main()
main_income.run()
