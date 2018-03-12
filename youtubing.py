import sys
from pprint import pprint


class CreditCards:

    num_of_cards = 0

    def __init__(self, name, bank, currency, bonus, annual_fee, earn_rate, min_spend):
        self.name = name
        self.bank = bank
        self.currency = currency
        self.bonus = '{0:,}'.format(bonus)
        self.annual_fee = annual_fee
        self.earn_rate = earn_rate
        self.min_spend = min_spend

        CreditCards.num_of_cards +=1


    #getters
    def getCardBankAndName(self):
        return self.bank + " " + self.name
    def getCurrentBonus(self):
        return self.bonus
    def getCurrentAnnualFee(self):
        return "$" + str(self.annual_fee) + " annual fee"

    #setters
    def setCurrentBonus(self, newBonus):
        self.bonus = newBonus
    def setCurrentAnnualFee(self, newAnnualFee):
        self.annual_fee = newAnnualFee

    def __str__(self):
        if self.annual_fee > 1:
            return "The {} {} credit card " \
                   "is currently offering {} {} points with a ${} annual fee.".format(self.bank, self.name, self.bonus,
                                                                                      self.currency, self.annual_fee)
        else:
            return "The {} {} credit card " \
                   "is currently offering {} {} points with a no annual fee.".format(self.bank, self.name,
                                                                                          self.bonus, self.currency,)


class AirlineCards(CreditCards):

    def __init__(self, name, bank, currency, bonus, annual_fee, earn_rate, min_spend,
                 eqm_bonus, boarding_perk, baggage_waiver):
        super().__init__(name, bank, currency, bonus, annual_fee, earn_rate, min_spend)
        self.boarding_perk = boarding_perk
        self.eqm_bonus = eqm_bonus
        self.baggage_waiver = baggage_waiver


    def __str__(self):
        if self.annual_fee > 1:
            return "The {} {} credit card " \
                   "is currently offering {} {} points after spending ${} with a ${} annual fee.".format(self.bank,
                   self.name, self.bonus, self.currency, self.min_spend, self.annual_fee)
        else:
            return "The {} {} credit card " \
                   "is currently offering {} {} points after spending ${} with a no annual fee.".format(self.bank,
                   self.name, self.bonus, self.currency, self.min_spend, self.currency)


    def getairlinecards(self):
        return self.bank + self.name

    def addNewAirlineCard(self):
        cancel = False
        airline_list = []

        while (True):
            bank = input("What is the bank name? ").title()
            name = input("What is the name of the card? ").title()
            miles_prog = input("What is the name of the miles program? ").title()
            bonus = int(input("What is the current sign up bonus? ".strip(",")))
            annual = int(input("What is the current annual fee? ").strip("$"))
            earn_rate = float(input("What is the earning rate? e.g. 1.5x or 2.0x; ").strip("x"))
            min_spend = int(input("What is the minimum spend amount? ").strip("$"))
            board_perk = input("Does the card include a boarding perk? yes/no; ").lower()
            eq_bonus = int(input("What is the current elite qualifying bonus amount? e.g. 10,000; ").strip(","))
            bag_waiver = input("Does the card include a baggage fee waiver? yes/no; ").lower()

            airline_list.append({
                "bank": bank,
                "name": name,
                "miles_prog": miles_prog,
                "bonus": bonus,
                "annual": annual,
                "earn_rate": earn_rate,
                "min_spend": min_spend,
                "board_perk": board_perk,
                "eq_bonus": eq_bonus,
                "bag_waiver": bag_waiver
            })

            cont = input("Do you want to create another? Yes/No ").lower()
            if cont == 'no':
                break

class HotelCards(CreditCards):

    def __init__(self, name, bank, currency, bonus, annual_fee, earn_rate, min_spend,
                 status_included=False):
        super().__init__(name, bank, currency, bonus, annual_fee, earn_rate, min_spend)
        self.status_included = status_included


class RewardsCards(CreditCards):

    def __init__(self, name, bank, currency, bonus, annual_fee, earn_rate, min_spend,
                 bonus_spend_cat, bonus_spend_mult, transferrable=False):
        super().__init__(name, bank, currency, bonus, annual_fee, earn_rate, min_spend)
        self.bonus_spend_mult = bonus_spend_mult
        self.transferable = transferrable






def main():
    cancel = False
    airline_list = []

    while (True):
        AirlineCards.bank = input("What is the bank name? ").title()
        AirlineCards.name = input("What is the name of the card? ").title()
        AirlineCards.miles_prog = input("What is the name of the miles program? ").title()
        AirlineCards.bonus = int(input("What is the current sign up bonus? ".strip(",")))
        AirlineCards.annual = int(input("What is the current annual fee? ").strip("$"))
        AirlineCards.earn_rate = float(input("What is the earning rate? e.g. 1.5x or 2.0x; ").strip("x"))
        AirlineCards.min_spend = int(input("What is the minimum spend amount? ").strip("$"))
        AirlineCards.board_perk = input("Does the card include a boarding perk? yes/no; ").lower()
        AirlineCards.eq_bonus = int(input("What is the current elite qualifying bonus amount? e.g. 10,000; ").strip(","))
        AirlineCards.bag_waiver = input("Does the card include a baggage fee waiver? yes/no; ").lower()

        airline_list.append({
            "bank": AirlineCards.bank,
            "name": AirlineCards.name,
            "miles_prog": AirlineCards.miles_prog,
            "bonus": AirlineCards.bonus,
            "annual": AirlineCards.annual,
            "earn_rate": AirlineCards.earn_rate,
            "min_spend": AirlineCards.min_spend,
            "board_perk": AirlineCards.board_perk,
            "eq_bonus": AirlineCards.eq_bonus,
            "bag_waiver": AirlineCards.bag_waiver
        })

        cont = input("Do you want to create another? Yes/No ").lower()
        if cont == 'no':
            break

    print(*airline_list, sep='\n')

if __name__ == '__main__':
    main()
