accountNo=input(" Enter the Account Number :" )
customerName=input("Enter the Customer Name:")
accountType=input("Enter the account type:")
balance=float(input("Enter the balance:"))

def showAccount():
    print("Account # : {} \nCustomerName :{} \naccount type:{} \n Balance Amount:{} ".
          format(accountNo,customerName,accountType,balance))
def withDraw(balance,amount):
    if accountType== "SAVINGS":
        newBalance= balance- amount
        if newBalance<500:
            raise Exception("Insufficient balance ,balance can not be withdrawn")
        else:
            balance=newBalance
            return balance
    elif accountType=="CURRENT":
        balance=balance -amount
        return balance

showAccount()
amount=float(input("Enter the Amount to be withdrawn :"))
balance=withDraw(balance,amount)