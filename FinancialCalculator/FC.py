income = float(input("Hello, and welcome to your financial calculator! \n How much do you make a month? \n"));
rent = float(input("What is your monthly rent: \n"));
utils = float(input("What is your monthly utilities: \n"))
groceries = float(input("What is your monthly groceries: \n"))
transport = float(input("What is your monthly transportation costs: \n"))

spent = rent + utils + groceries + transport; 
savings = income * .2; 
budget = income - spent - savings; 
print(budget); 

print("In percent that is. \n"); 
prent = int(rent /income *100); 
putils = int(utils/income *100); 
pgroceries = int(groceries /income *100); 
ptransport = int(transport /income*100); 

print(prent, "%\n"); 
print(putils, "% \n"); 
print(pgroceries, "% \n"); 
print(ptransport, "% \n"); 

print("In total you spend \n"); 
pspent = int(spent /income *100); 
print(pspent, "% \n"); 

print("You save 20% \n"); 

print("Your budget is: "); 
pbudget = int(budget /income *100);
print(pbudget, "% \n"); 