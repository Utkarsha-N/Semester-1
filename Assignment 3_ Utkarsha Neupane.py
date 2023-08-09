# WAP to calculate the final pay of an employee

hrs = int(input("Enter the hours worked"))        # Prompt to input total hours worked and hourly pay rate
payRate = float(input("Enter hourly pay-rate"))

if hrs <= 40:
    Final_pay = payRate * hrs                     # Calculating Final weekly pay in case of work done less than 40 hrs

else:
    OT_hrs = hrs - 40                             # calculating overtime hours
    OT_payRate = payRate * 1.5                    # Calculating Overtime Pay  rate
    normalPay = payRate * 40                      # Calculating pay for 40 hrs
    OT_pay = OT_payRate * OT_hrs                  # Calculating overtime Pay
    Final_pay = normalPay + OT_pay                # Calculating final pay by adding normal hrs pay and overtime pay


print("The final pay is ", Final_pay)             # Print statement to output final pay calculated


