# import the necessary random modules 
import random 
# Challenge Name - Who Will Pay First r
def whoWillPayFirst(teamUser):
    return random.choice(teamUser)

team = ['Amanda', 'Bob', 'Aisha']
payee = whoWillPayFirst(team)
print(payee)