import datetime
from dateutil.relativedelta import relativedelta
import webbrowser
import re
import sys


credit_karma_link = "www.creditkarma.com"
sub_prime_card_link = "https://www.creditcards.com/fair-credit/"
two_yrs_ago = str(datetime.date.today() - relativedelta(years=2))
two_yrs_format = datetime.datetime.strptime(two_yrs_ago, '%Y-%m-%d').strftime('%m/%d/%Y')
six_mnth_ago = str(datetime.date.today() - relativedelta(months=6))
six_mnth_ago_format = datetime.datetime.strptime(six_mnth_ago, '%Y-%m-%d').strftime('%m/%d/%Y')
three_mnth_ago = str(datetime.date.today() - relativedelta(months=3))
three_mnth_ago_format = datetime.datetime.strptime(three_mnth_ago, '%Y-%m-%d').strftime('%m/%d/%Y')



def launch_credit_karma():
    attempts = 0
    for attempts in range(4):
        open_site = input("Do you want to open Credit Karma so you can count your credit \n"
                          "card account open dates and check your credit score? (Remember, even if they are now \n"
                          "closed, you STILL have to count accounts opened in the last 24 months) Yes/No: ").lower()
        if open_site == 'yes':
            webbrowser.open_new(credit_karma_link)
            break
        elif open_site == 'no':
            break
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**\n")
    else:
        print("\nSorry, you only had four attempts to answer\n")
        exit()


def get_credit_score():
    attempts = 0
    for attempts in range(4):
        credit_score = int(input("\nWhat is your current credit score? "))
        if 349 < credit_score < 901:
            print("**Your credit score has been saved as {}.**".format(credit_score))
            if credit_score > 659:
                return credit_score
            else:
                open_subprime_cards = input("\nBefore applying for a premium travel credit card it is"
                                            " recommended to have a credit score over 660. Do you want to see a list of"
                                            " credit cards that are aimed at building your credit? Yes/No ").lower()
                if open_subprime_cards == 'yes':
                    webbrowser.open_new(sub_prime_card_link)
                    print("***Please come back once your credit score exceeds 660. This program will now close***")
                    sys.exit(1)
                else:
                    print("***Please come back once your credit score exceeds 660. This program will now close***")
                    sys.exit(1)
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter a number between 350 and 900, "
                  "you have " + attempts_remaining + " attempts remaining**\n")
    else:
        print("\nSorry, you only had four attempts to answer\n")
        exit()


def get_chase_card_last_six():
    attempts = 0
    for attempts in range(4):
        last_six = input("\nHave you signed up for a new Chase personal "
                         "credit card between " + six_mnth_ago_format + " and today? Yes/No: ").lower()
        if last_six == 'yes':
            print("**Signed up for a new Chase personal "
                  "credit card in the last six months - Response stored as: Yes**")
            return True
        elif last_six == 'no':
            print("**Signed up for a new Chase personal "
                  "credit card in the last six months - Response stored as: No**")
            return False
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**")
    else:
        print("\nSorry, you only had four attempts to answer")
        exit()


def get_num_of_cards_twenty_four():
    attempts = 0
    for attempts in range(4):
        num_twenty_four = int(input("\nHow many credit cards have you opened between " + str(two_yrs_format) +
                                    " and today? (count cards even if they are now closed, but only"
                                    " if they reported to Credit Karms) "))
        if 0 <= num_twenty_four <= 40:
            print("Number of credit card accounts created since " +
                  str(two_yrs_format) + " stored as " + str(num_twenty_four) + ".")
            if 0 <= num_twenty_four < 5:
                return num_twenty_four
            else:
                pass
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only a number between 0 and 40, "
                  "you have " + attempts_remaining + " attempts remaining**")
    else:
        exit()


def get_app_in_last_ninety():
    attempts = 0
    for attempts in range(4):
        num_ninety = int(input("\nHow many credit cards have you applied for "
                               "between " + str(three_mnth_ago_format) + " and today? "))
        if 0 <= num_ninety < 15:
            if num_ninety == 0:
                print("Since you haven't applied for a credit card in the last 90 days, feel free to apply today!")
            elif 0 < num_ninety < 4:
                print("Since you've applied for " + str(num_ninety) + " cards in the last 90 days,"
                      " it best best to wait 30 more days")
            else:
                print("You've opened too manny credit cards in the last 90 days, "
                      "do not apply for a credit card for at least 60 days.")
            return num_ninety
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only a number between 0 and 15, "
                  "you have " + attempts_remaining + " attempts remaining**")
    else:
        pass


def get_aa_citi_personal_card():
    attempts = 0
    for attempts in range(4):
        aa_cards = input("\nHave you opened OR closed ANY Citi American Airlines "
                   "personal credit card since " + two_yrs_format + "? Yes/No ").lower()
        if aa_cards == 'yes':
            print("**Opened or closed Citi AA personal "
                  "credit card in the last 24 months - Response store as: Yes**")
            return True
        elif aa_cards == 'no':
            print("**Opened or closed Citi AA personal "
                  "credit card in the last 24 months - Response store as: No**")
            return False
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**")
    else:
        print("\nSorry, you only had four attempts to answer")
        exit()


def get_aa_citi_biz_card():
    attempts = 0
    for attempts in range(4):
        aa_biz_cards = input("\nHave you opened OR closed ANY Citi American Airlines "
                   "business credit card since " + two_yrs_format + "? Yes/No ").lower()
        if aa_biz_cards == 'yes':
            print("**Opened or closed Citi AA business "
                  "credit card in the last 24 months - Response store as: Yes**")
            return True
        elif aa_biz_cards == 'no':
            print("**Opened or closed Citi AA business "
                  "credit card in the last 24 months - Response store as: No**")
            return False
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**")
    else:
        print("\nSorry, you only had four attempts to answer")
        exit()


def get_ty_citi_card():
    attempts = 0
    for attempts in range(4):
        ty_cards = input("\nHave you opened OR closed ANY Citi ThankYou personal credit card "
                         "since " + two_yrs_format + "? Yes/No ")
        if ty_cards == 'yes':
            print("**Opened or closed Citi ThankYou personal "
              "credit card in the last 24 months - Response store as: Yes**")
            return True
        elif ty_cards == 'no':
            print("**Opened or closed Citi ThankYou personal "
              "credit card in the last 24 months - Response store as: No**")
            return False
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**")
    else:
        print("\nSorry, you only had four attempts to answer")
        exit()


def get_capone_cards():
    attempts = 0
    for attempts in range(4):
        capone_cards = input("\nDo you currently hold the Capital One Venture card OR "
                             "have you applied for this card since " + six_mnth_ago_format + "? (answer 'no' "
                             "if either condition applies) Yes/No ").lower()
        if capone_cards == 'yes':
            print("**currently hold Capital One Venture or applied for it "
                  "in the last 6 months - Response store as: Yes**")
            return True
        elif capone_cards == 'no':
            print("**currently hold Capital One Venture or applied for it "
                  "in the last 6 months - Response store as: No**")
            return False
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**")
    else:
        print("\nSorry, you only had four attempts to answer")
        exit()


def get_amex_cards():
    attempts = 0
    for attempts in range(4):
        amex = (input("\nHow many American Express 'non charge-card' credit cards do you currently have open? "))
        if 0 <= int(amex) <= 15:
            return amex
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter a number between 0 and 15, "
                  "you have " + attempts_remaining + " attempts remaining**\n")
    else:
        print("\nSorry, you only had four attempts to answer\n")
        exit()


def is_sapphire():
    attempts = 0
    for attempts in range(4):
        sapphire = input("\nDo you currently hold the Chase Sapphire Preferred or Reserve card? answer Yes/No ").lower()
        if sapphire == 'yes':
            return True
        elif sapphire == 'no':
            return False
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**")
    else:
        print("\nSorry, you only had four attempts to answer")
        exit()


def get_eligible_cards(aa_cards, aa_biz_cards, ty_cards, capone_cards, sapphire,
                       amex, last_six, num_twenty_four, num_ninety):
    print("\n\nBased on your inputs, here are some cards that you're eligible to receive a sign-up bonus for:")
    if aa_cards is False:
        print("\n--You are eligible to receive the bonus for one Citi AA personal credit card.*")
    if aa_biz_cards is False:
        print("\n--You are eligible to receive the bonus for one Citi AA business credit card.*")
    if ty_cards is False:
        print("\n--You are eligible to receive the bonus for one Citi AA credit card.*")
    if capone_cards is False:
        print("\n--You are eligible to receive the bonus for the Capital One Venture credit card.*")
    if amex == 0 <= amex <= 3:
        print("\n--You are eligible to sign-up for an Amex credit card assuming "
              "you haven't already received the bonus on that exact card in the past.*")
    if not(sapphire and last_six and num_twenty_four > 90 and num_ninety < 3):
        print("\n--You are eligible to sign-up for either of the Chase Sapphire credit cards, go for it!*")
    else:
        sys.exit(1)


if __name__ == '__main__':
    launch_credit_karma()
    credit_score = get_credit_score()
    last_six = get_chase_card_last_six()
    num_ninety = get_app_in_last_ninety()
    num_twenty_four = get_num_of_cards_twenty_four()
    aa_cards = get_aa_citi_personal_card()
    aa_biz_cards = get_aa_citi_biz_card()
    ty_cards = get_ty_citi_card()
    capone_cards = get_capone_cards()
    amex = get_amex_cards()
    sapphire = is_sapphire()
    get_eligible_cards(aa_cards, aa_biz_cards, ty_cards, capone_cards,
                       amex, sapphire, last_six, num_twenty_four, num_ninety)






