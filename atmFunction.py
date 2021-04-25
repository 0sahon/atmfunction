import random
ame = input("What is your name? \n")
allowedUsers = ['Osahon','Victor','Mary']
allowedPassword = ['pOsahon','pVictor','pMary']
balance =0

if(name in allowedUsers):
    password = input("Enter Users Password \n")
    userId = allowedUsers.index(name)


    if(password == allowedPassword[userId]):
        print('Welcome %s' % name)
        # Current date time in local system
        print('The time for this transaction is', datetime.now())
        print('These are the available Options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Compliant')

        selectedOption = int(input('Please Select an Option:'))
        balance = 0

        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            withdrawalRequest = int(input('How much would you like to withdraw: \n'))
            if(withdrawalRequest > 0):
               withdrawal=  currentBalance - withdrawalRequest
                print('take your cash')
            else:
                print('insufficient fund, Kindly deposit')
            
        elif(selectedOption == 2):
            print('you selected %s' % selectedOption )
            cashDeposit =  int(input('How Much will you like to deposit'))
            currentBalance = balance + cashDeposit
            print('your current balance is', currentBalance)

        elif(selectedOption == 3):
            print('you selected %s' % selectedOption )
            complainReport = input('What issue will you like to report? \n')
            print('Thank you for contacting us')
        else:
            print('Invalid Option selected, Try Again')

    else:
        print('Password incorrect, Try Again')
else:
    print('Name Not Found, Please Try again')

database = {3311338867:["Osahon","airhienbuwa", "osahon@rillcod.com", "password", 200]
    }

def init():

    isValidOptionSelected = False
    print("welcome to bank RILLCOD ")
    while isValidOptionSelected =False:

        haveAccount = int(input("Do you have account with us : 1 (yes) 2 (no) \n "))

        if haveAccount == 1:
            isValidOptionSelected =True 
            login()
        elif haveAccount == 2:
            isValidOptionSelected =True 
            print("****REGISTRATION PORTAL")
            register()
        else:
            print("you have selected an invalid Option")

def register():
    firstName = input("Enter your First Name")
    lastName = input("Enter your Last Name")
    email = input("Enter your e-mail Address")
    password = input("Create an eight digit password")

    accountNumber = generateAccount()

    database[accountNumber] = [firstname, lastname, email, password, 0]

    print("Your account have been created ")
    print("Your account number is %d " % accountNumber)

    login()

def login():
    print("Log in to your account")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input ("What is your password \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                bankOperation(userDetails)

    print("Invalid account or password")
    
    login()
    
def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)

def check_funds(accountBalance):
    accountBalance = 0
    if accountBalance<= 0:
        return False
    else:
        return print("the current account balance is", balance)

def withdrawalOperation():
    print("withdrawal")
    # get current balance

    # get amount to withdraw
   amountTo withdraw = withdrawalRequest
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def deposit_operation():
    print("Deposit Operations")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()