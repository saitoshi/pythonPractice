'''
@name life_in_weeks()
@desc Caluclates the weeks left based on the age input 
@input age 
@return the remaining weeks we have left based on  the given age 
'''
def life_in_weeks(age):
    max_age = 90
    max_weeks = 90 * 52
    current_weeks = age * 52
    weeks_left = max_weeks - current_weeks
    print("You have " + str(weeks_left) + " weeks left.")

life_in_weeks(20)
