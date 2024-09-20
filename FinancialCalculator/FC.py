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
putils
pgroceries
ptransport