def main():
    print('''
=============================================================================
                       ##  SIMPLE CALCULATOR l ##
                 ''')
    num1=int(input("Enter your first no: "))
    num2=int(input('''
Enter your second no:'''))
    
    func=input('''
             ##### What operation would you like to performe ######
             
                            1= Addition
                            2= Subtraction
                            3= Multiplication
                            4= Division
                            5= Modulus Division

                          -> ''')
    #Addition
    if func=="1":
        ans=num1+num2
        print("Your ans is", ans)
        main()

    #Subtraction    
    if func=="2":
        ans=num1-num2
        print("Your ans is",ans)
        main()

    #Multiplication    
    if func=="3":
        ans=num1*num2
        print("Your ans is",ans)
        main()

    #Division    
    if func=="4":
        if num2 ==0:
           print("Second number is Zero Therefore Division no possible")
        else:
           ans=num1/num2
           print("Your ans is",ans)   
        main()

    #Modulus Division
    if func=="5":

        # if Second number Zero
        if num2==0:
            print("Second number is Zero Therefore Division no possible")
        elif num1>num2:
           ans=num1%num2
           print("Your ans is",ans)

        # if first number is smaller
        else:
           print("Operation cannot performed... Because first number is smallar number  ")
        main()

    # If Invalid operation is given    
    else:
        print('''                     !!!!  ERROR  !!!!

          !!! The operation you Entered is invalid. Plz try again !!!''')
        main()

#star main loop
main()
