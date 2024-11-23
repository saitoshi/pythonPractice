# Beginner Practice Problems

<ol>
<li>Write a program that takes in a user input and determines whether it is even or not?</li>

```
# Practice 1 - Create a program that determines whetehr user input is even or not
userInput = input("Enter A Value and Will determine if it is even or not \n")
print("You have inputted: " + userInput)
digitEvaluation = ""
if (int(userInput) % 2 == 0):
    digitEvaluation = "even"
else:
    digitEvaluation = "odd"

print(userInput + " is a " + digitEvaluation + " number.")

```

</ol>
