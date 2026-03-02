medical_cause = input("do you have a medical cause?")
if medical_cause == "yes":
    print("you are allowed to write exam.")
else:
     atten = int(input("give attendance"))
     if atten >= 75:
            print("you are allowed")
     else:
          print("you are not allowed")  