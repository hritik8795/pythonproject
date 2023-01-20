print("welcome in our service")
number=int(input("enter your passsword"))
if number!=1234:
    print("sorry")
else:
    account_balance=100000
    print("hii, solemn")
    print("what do you want")
    print("1.credit money"
          "2.withdraw money"
          "3.check balance"
          "4.exit")
    sep="\n"
    option=int(input("enter from these option "))
    if (option ==1):
     credited_money=int(input("enter money that you want to be credit"))
     print("your account balance is",credited_money+account_balance)
     while True:
      print("enter what u want")
     option == input()
    if (option==exit):
            break
    elif (option ==2):
       withdraw_money=int(input("enter money that you want to withdraw"))
       print("your current balance is ",account_balance-withdraw_money)
    elif(option ==3):
            print("your balance is  ",account_balance)