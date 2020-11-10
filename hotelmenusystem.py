from tabulate import tabulate
print("Welcome to JACKHotel")
print("Please give your choice number:")
a=int(input("1. Vegfood 2.Non-Vegfood\n"))
if a==1:
   print(tabulate([[1,'PaneerMasala'],[2,'Paneer Tikka'],[3,'DaalPakwaan'], [4,'PuriBhaji'],[5,'Veg Thali']],headers=['Srno.','Name'],tablefmt='orgtbl'))
   b=int(input("Please Place your order number from menu\n"))
   if b==1:
        print(" **PaneerMasala**",'\n',"*You have to pay Rs.120*")
   elif(b==2):
        print(" **PaneerTikka**",'\n',"*You have to pay Rs.140*")
   elif(b==3):
        print(" **DaalPakwaan**",'\n',"*You have to pay Rs.110*")
   elif(b==4):
        print(" **PuriBhaji**",'\n',"*You have to pay Rs.160*")
   elif(b==5):
        print(" **VegThali**",'\n',"*You have to pay Rs.220*")
   print("Thank you for ordering, we hope you enjoy the meal:)")
elif a==2:
   print(tabulate([[1,'ChikenMasala'],[2,'Chiken Tandoori'],[3,'ChikenTikka'], [4,'DumBiryani'],[5,'Mughlai Chiken']],headers=['Srno.','Name'],tablefmt='orgtbl'))
   b=int(input("Please Place your order number from menu\n"))
   if b==1:
       print("**ChikenMasala**",'\n',"*You have to pay Rs.180*")
   elif(b==2):
       print("**chikenTandoori**",'\n',"*You have to pay Rs.220*")
   elif(b==3):
       print("**chikenTikka**",'\n',"*You have to pay Rs.190*")
   elif(b==4):
       print("**DumBiryani**",'\n',"*You have to pay Rs.245*")
   elif(b==5):
       print("**MughlaiChiken**",'\n',"*You have to pay Rs.220*")
   print("Thank you for ordering, we hope you enjoy the meal:)")