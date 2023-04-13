# TASK 3 : mini project : 
# KALYAN JWELLERS : 

# M 
# >  65
# purchase > 2lk - 3lk    20% 
# purchase > 3lk - 5lk 	30% 
# purchase > 5lk  	35% 


# <65
# purchase > 2lk - 3lk    10% 
# purchase > 3lk - 5lk 	20% 
# purchase > 5lk  	25% 



# F
# >  65
# purchase > 2lk - 3lk    25% 
# purchase > 3lk - 5lk 	35% 
# purchase > 5lk  	40% 


# <65
# purchase > 2lk - 3lk    15% 
# purchase > 3lk - 5lk 	25% 
# purchase > 5lk  	30% 


# ------------------------------------------------------------
# Enter your name : 
# Enter gender : 
# Enter age : 

# Enter product : Ring 
# Enter product gram : 20  
# current gold price (1 grm) : 5752

# -------------------------------------
# TOTAL GOLD RATE :  XXXXX 


# Making charges (1 gram)  : 845
# Total Making CHarges :    TOTAL GOLD  X  MAKING CHARGES 

# ---------------------------------------
# TOTAL AMOUNT : GOLD PRICE + TOTAL MAKING CHARGES



# DISCOUNT :   25 (AUTOMATIC) 
# DIS- AMOUNT : except (making charges) 
# -----------------------------------------
# total net amount : 

# --------------------------------------------
# HINT : variables , input , conditional statements 





GOLD_PRICE_PER_GRAM = 5752
MAKING_CHARGES_PER_GRAM = 845

def calculate_gold_rate(gram):
    return GOLD_PRICE_PER_GRAM * gram

def calculate_making_charges(gold_rate):
    return MAKING_CHARGES_PER_GRAM * gold_rate

def calculate_discount(age, gender, purchase_amount):
    discount = 0
    if gender == 'M':
        if age >= 65:
            if purchase_amount > 500000:
                discount = 0.35
            elif purchase_amount > 300000:
                discount = 0.3
            elif purchase_amount > 200000:
                discount = 0.2
        else:
            if purchase_amount > 500000:
                discount = 0.25
            elif purchase_amount > 300000:
                discount = 0.2
            elif purchase_amount > 200000:
                discount = 0.1
    elif gender == 'F':
        if age >= 65:
            if purchase_amount > 500000:
                discount = 0.4
            elif purchase_amount > 300000:
                discount = 0.35
            elif purchase_amount > 200000:
                discount = 0.25
        else:
            if purchase_amount > 500000:
                discount = 0.3
            elif purchase_amount > 300000:
                discount = 0.25
            elif purchase_amount > 200000:
                discount = 0.15
    return discount


name = input("Enter your name: ")
gender = input("Enter your gender (M/F): ")
age = int(input("Enter your age: "))
product = input("Enter product: ")
gram = float(input("Enter product gram: "))
gold_rate = calculate_gold_rate(gram)
print("-------------------------------------------")
print("TOTAL GOLD RATE : ", gold_rate)
making_charges = calculate_making_charges(gold_rate)
print("Making charges (1 gram)  : ", MAKING_CHARGES_PER_GRAM)
print("Total Making Charges :   ", making_charges)
total_amount = gold_rate + making_charges
print("-------------------------------------------")
print("TOTAL AMOUNT : ", total_amount)
discount = calculate_discount(age, gender, total_amount)
discount_amount = total_amount * discount
print("DISCOUNT : ", discount * 100, "%")
print("DIS- AMOUNT : ", discount_amount)
net_amount = total_amount - discount_amount
print("--------------------------------------------")
print("total net amount : ", net_amount)
print("--------------------------------------------")

#--------------------------------------------------------------------------------------------------------------------------
#ipl task:

import random
teams = ['CSK', 'KXIP', 'KKR', 'RR', 'RCB']
opponent_team = random.choice([teams])
toss_choice = input("Toss time! What's your call? (H/T): ")
toss_result = random.choice(['H', 'T'])

if toss_choice == toss_result:
    print("Congratulations! You won the toss.")
    batting_choice = input("What do you want to do? (1 - Bat / 2 - Ball): ")
    
    if batting_choice == '1':
        print("You chose to bat first!")
        score = 0
        wickets = 0
       
        for i in range(6):
            ball_score = random.choice([1, 2, 3, 4, 6, 'WICKET', 'NO BALL', 'WIDE'])
            
            if ball_score == 'WICKET':
                wickets += 1
                print(f"Wicket down! Total wickets lost: {wickets}")
                if wickets == 10:
                    print("All out!")
                    break
            elif ball_score == 'NO BALL':
                score += 1
                print("No ball! Free hit coming up!")
            elif ball_score == 'WIDE':
                score += 1
                print("Wide ball! Extra run added!")
            else:
                score += ball_score
            
            print(f"Ball {i+1}: {ball_score}")
            
        print(f"Your score: {score} for {wickets} wickets.")
        
    elif batting_choice == '2':
        print("You chose to ball first!")
     
        pass
    
    else:
        print("Invalid choice. Please try again.")
        
else:
    print("Oops! You lost the toss. Better luck next time.")
 
    pass
