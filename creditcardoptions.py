from dateutil.relativedelta import relativedelta
import datetime
import webbrowser
import re
import sys


DATE_AS_REG_EXP = re.compile('\d{2}[-/]\d{2}[-/]\d{4}')
CREDIT_SCORE_AS_REG_EXP = re.compile('^[0-9]{3}$')
NUMBER_OF_CREDIT_CARDS = re.compile('^[0-9]{1,2}$')
CREDIT_KARMA_LINK = "www.creditkarma.com"
SUBPRIME_CARD_LINK = "https://www.creditcards.com/fair-credit/"
TWO_YEARS_AGO = str(datetime.date.today() - relativedelta(years=2))
TWO_YEAR_FORMATTED = datetime.datetime.strptime(TWO_YEARS_AGO, '%Y-%m-%d').strftime('%m/%d/%Y')
SIX_MONTHS_AGO = str(datetime.date.today() - relativedelta(months=6))
SIX_MONTHS_AGO_FORMATTED = datetime.datetime.strptime(SIX_MONTHS_AGO, '%Y-%m-%d').strftime('%m/%d/%Y')
THREE_MONTHS_AGO = str(datetime.date.today() - relativedelta(months=3))
THREE_MONTHS_AGO_FORMATTED = datetime.datetime.strptime(THREE_MONTHS_AGO, '%Y-%m-%d').strftime('%m/%d/%Y')
TODAY = datetime.datetime.today().strftime("%m/%d/%Y")



def get_valid_date_format(last_date):
    return bool(DATE_AS_REG_EXP.search(last_date))


def get_valid_credit_score(credit_score):
    return bool(CREDIT_SCORE_AS_REG_EXP.search(credit_score))


def get_valid_credit_cards(num):
    return bool(NUMBER_OF_CREDIT_CARDS.search(num))


def check_for_future_dates(now, then):
    now = datetime.datetime.strptime(now, '%m/%d/%Y')
    then = datetime.datetime.strptime(then, '%m/%d/%Y')
    return now > then

#prompts the user if they'd like to open Credit Karma to check their score and accounts
def launch_credit_karma():
    for attempts in range(4):
        open_site = input("\nDo you want to open Credit Karma so you can count your credit \n"
                          "card account open dates and check your credit score? Yes/No: ").lower()
        if open_site == 'yes':
            webbrowser.open_new(CREDIT_KARMA_LINK)
            return
        elif open_site == 'no':
            return
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**\n")
    else:
        print("\nSorry, you only had four attempts to answer\n")
        sys.exit(1)

#checks for a valid credit score input, if less than 661, will warn and prompt the user to open a relevant website 
def get_credit_score():
    for attempts in range(4):
        credit_score = input("\nWhat is your current credit score? ")
        #checks for a properly formatted credit score, three digits (nnn), then validates for input between 349 and 901
        if get_valid_credit_score(credit_score) and 349 < int(credit_score) < 901:
            print("**Your credit score has been saved as {}.**".format(credit_score))
            for attempts in range(4):
                if int(credit_score) < 661:
                    open_subprime_cards = input("\n*NOTE* Before applying for a premium travel credit card it is"
                                                " recommended to have a credit score over 660. "
                                                "Do you want to see a list of"
                                                " credit cards that are aimed at building your credit? Yes/No ").lower()
                    if open_subprime_cards == 'yes':
                        webbrowser.open_new(SUBPRIME_CARD_LINK)
                        break
                    elif open_subprime_cards == 'no':
                        break
                    else:
                        attempts_remaining = 3 - attempts
                        if attempts_remaining != 0:
                            print("\n**Please enter only yes or no, "
                                  "you have " + str(attempts_remaining) + " attempts remaining**\n")
                        else:
                            print("Sorry, you only had four attempts to answer")
                            sys.exit(1)
            return credit_score
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only a number between 350 and 900, "
                  "you have " + attempts_remaining + " attempts remaining**\n")
    else:
        print("\nSorry, you only had four attempts to answer. The program will now exit")
        sys.exit(1)

#prompts the user if they've previously applied for a credit card in the past, if no, the program will exit 
def get_has_applied_previously(credit_score):
    for attempts in range(4):
        ever_applied = (input("\nHave you ever applied for a credit card in the past? Yes/No ")).lower()
        if ever_applied == 'no' and int(credit_score) > 660:
            print("Since you've never applied for a card and your credit score is " + credit_score +
                  "you are 'technically' qualified for ANY credit card bonus on the market, "
                  "I'd go for the Chase Sapphire Preferred!")
            sys.exit(1)
        elif ever_applied == 'no' and int(credit_score) < 661:
            print("You are 'technically' qualified for any credit card bonus since you've never had a card before. "
                  "However, it is NOT recommended to apply until your credit score exceeds 660. ")
            break
        elif ever_applied == 'yes':
            print("Response stored as: Yes ")
            break
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter either yes or no, "
                  "you have " + attempts_remaining + " attempts remaining**")
    else:
        sys.exit(1)

#prompts the user for a data in mm/dd/yyyy format
def get_most_recent_inquiry_date():
    date_format = "%m/%d/%Y"
    for attempts in range(4):
        last_date = input("\nWhat was the date of your most recent credit inquiry? e.g.: 07/26/2017 ")
        try:
            #formats the user's input date and today's date to perform a time delta difference
            now = datetime.datetime.strptime(TODAY, date_format)
            then = datetime.datetime.strptime(last_date, date_format)
        except ValueError:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only a date formatted as such: mm/dd/yyyy, "
                  "you have " + attempts_remaining + " attempts remaining**")
            continue
            #validates for the proper date, cannot be a future date and must be in mm/dd/yyyy format
        if check_for_future_dates(TODAY, last_date) and get_valid_date_format(last_date):
            #subtracts the two dates to produce a positve number as a difference called 'delta'
            delta = (now - then).days
            print("Days since last inquiry: " + str(delta))
            return delta
        elif not check_for_future_dates(TODAY, last_date) and get_valid_date_format(last_date):
            attempts_remaining = str(3 - attempts)
            print("You can't enter a future date, silly! "
                  "You have " + attempts_remaining + " attempts remaining**")
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only a date formatted as such: mm/dd/yyyy, "
                  "you have " + attempts_remaining + " attempts remaining**")
    else:
        sys.exit(1)

#informs the users, if their latest inquiry was less than three months ago, that it is not advised to apply for a card now
def cont_prog_with_recent_inquiry(delta):
    if 0 <= delta < 90:
        for attempts in range(4):
            print("\nSince you've applied for a card " + str(delta) + " days ago, you should wait an additional "
                  + str(90 - delta) + " days before applying for any card. ")
            wants_to_cont = input("Do you still want to continue with the questions? Yes/No ").lower()
            if wants_to_cont == 'yes':
                return True
            elif wants_to_cont == 'no':
                print("\n The program will now exit, have a great day!")
                sys.exit(1)
            else:
                attempts_remaining = str(3 - attempts)
                print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**")
    else:
        return

#prompts the user if they've signed up for a Chase personal credit card in the last six months
def get_chase_card_last_six():
    for attempts in range(4):
        last_six = input("\nHave you signed up for a new Chase personal "
                     "credit card between " + SIX_MONTHS_AGO_FORMATTED + " and today? Yes/No: ").lower()
        if last_six == 'yes':
            print("**Signed up for a new Chase personal "
                  "credit card in the last six months - Response store as: Yes**")
            return True
        elif last_six == 'no':
            print("**Signed up for a new Chase personal "
                  "credit card in the last six months - Response store as: No**")
            return False
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**")
    else:
        print("\nSorry, you only had four attempts to answer")
        sys.exit(1)

#prompts the users for num of credit cards opened in last twenty four months 
def get_num_of_cards_twenty_four():
    for attempts in range(4):
        num_twenty_four = input("\nHow many credit cards have you opened between " + str(TWO_YEAR_FORMATTED) +
                                " and today? (count cards even if they are now closed, but only"
                                " if they reported to Credit Karma) i.e. 5: ")
        if get_valid_credit_cards(num_twenty_four) and 0 <= int(num_twenty_four) <= 50:
            print("Number of credit card accounts created since " +
                  str(TWO_YEAR_FORMATTED) + " stored as: " + str(num_twenty_four))
            return num_twenty_four
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only a number between 0 and 50, "
                  "you have " + attempts_remaining + " attempts remaining**")
    else:
        sys.exit(1)

#prompts user if they've opened or closed a Citi personal AA card in the last 24 months
def get_aa_citi_personal_card():
    for attempts in range(4):
        aa_cards = input("\nHave you opened OR closed ANY Citi American Airlines "
                   "personal credit card since " + TWO_YEAR_FORMATTED + "? Yes/No ").lower()
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
        sys.exit(1)

#prompts user if they've opened or closed a Citi business AA card in the last 24 months
def get_aa_citi_biz_card():
    for attempts in range(4):
        aa_biz_cards = input("\nHave you opened OR closed ANY Citi American Airlines "
                   "business credit card since " + TWO_YEAR_FORMATTED + "? Yes/No ").lower()
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
        sys.exit(1)

#prompts user if they've opened or closed a Citi ThankYou card in the last 24 months
def get_ty_citi_card():
    for attempts in range(4):
        ty_cards = input("\nHave you opened OR closed ANY Citi ThankYou personal credit card "
                         "since " + TWO_YEAR_FORMATTED + "? Yes/No ")
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
        sys.exit(1)

#prompts user if they currently hold the Capital One Venture card or if they've applied for it in the last six months
def get_capone_cards():
    for attempts in range(4):
        capone_cards = input("\nDo you currently hold the Capital One Venture card OR "
                             "have you applied for this card since " + SIX_MONTHS_AGO_FORMATTED + "? (answer 'yes' "
                             "if either condition applies) Yes/No ").lower()
        if capone_cards == 'yes':
            print("**Currently hold Capital One Venture or applied for it "
                  "in the last 6 months - Response store as: Yes**")
            return True
        elif capone_cards == 'no':
            print("**Currently hold Capital One Venture or applied for it "
                  "in the last 6 months - Response store as: No**")
            return False
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter only 'yes' or 'no', you have " + attempts_remaining + " attempts remaining**")
    else:
        print("\nSorry, you only had four attempts to answer")
        sys.exit(1)

#prompts the user for how many American Express non charge cards that are currently open (maximum of four per Amex)
def get_amex_cards():
    for attempts in range(4):
        amex = input("\nHow many American Express 'non charge-card' credit cards do you currently have open? i.e. 3: ")
        if get_valid_credit_cards(amex):
            if 0 <= int(amex) <= 15:
                return int(amex)
        else:
            attempts_remaining = str(3 - attempts)
            print("\n**Please enter a number between 0 and 15, "
                  "you have " + attempts_remaining + " attempts remaining**\n")
    else:
        print("\nSorry, you only had four attempts to answer\n")
        sys.exit(1)

#prompts the user if they've 
def has_sapphire():
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
        sys.exit(1)


def get_eligible_cards(delta, aa_cards, aa_biz_cards, ty_cards, capone_cards, sapphire_result,
                       amex, last_six, num_twenty_four):
    print("\n \n***************RESULTS***************")
    if aa_cards is False:
        print("\n--You're eligible to receive the bonus for one Citi AA personal credit card.*")
    if aa_biz_cards is False:
        print("\n--You're eligible to receive the bonus for one Citi AA business credit card.*")
    if ty_cards is False:
        print("\n--You're eligible to receive the bonus for one Citi ThankYou credit card.*")
    if capone_cards is False:
        print("\n--You're eligible to receive the bonus for the Capital One Venture credit card.*")
    if 0 <= amex <= 4:
        print("\n--You're eligible to sign-up for an Amex credit card *assuming* "
              "you haven't already received the bonus on that exact card in the past.*")
    if not sapphire_result and int(last_six) == 0 and int(num_twenty_four) <= 4:
        print("\n--You're eligible to sign-up for either of the Chase Sapphire credit cards, go for it!*")
        return
    else:
        print("It doesn't look like you're eligible for any of the popular travel cards at this time, try back later.")
        sys.exit(1)



if __name__ == '__main__':
    launch_credit_karma()
    credit_score = get_credit_score()
    get_has_applied_previously(credit_score)
    delta = get_most_recent_inquiry_date()
    if delta >= 90 or (delta < 90 and cont_prog_with_recent_inquiry(delta)):
        last_six = get_chase_card_last_six()
        num_twenty_four = get_num_of_cards_twenty_four()
        aa_cards = get_aa_citi_personal_card()
        aa_biz_cards = get_aa_citi_biz_card()
        ty_cards = get_ty_citi_card()
        capone_cards = get_capone_cards()
        amex = get_amex_cards()
        sapphire_result = has_sapphire()
        get_eligible_cards(delta, aa_cards, aa_biz_cards, ty_cards, capone_cards, sapphire_result,
                       amex, last_six, num_twenty_four)
    else:
        print("The program will now exit")
        sys.exit(1)







