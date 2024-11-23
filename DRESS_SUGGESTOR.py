# creating the algorithm
# getting the temperature from the user.
temp = int(input("Enter the temperature: "))

if (temp < 0):
    print("Its too cold,go to your house close all doors and windows wear a sweter and thick clothes to keep you warm and watch tv.")
elif (temp < 21):
    print("Its cold prefer wearing the sweater and drink hot water.")
elif (temp < 31):
    print("The temperature is moderate you can wear a shirt or a t-shirt and do your works as usual.")
elif (temp < 41):
    print("The temperature is too warm try wear thin clothes to let the air circulate.")
elif (temp > 40):
    print("The temperature is too hot wear very thin clothes and get into your house and turn on the ac and chill if you don't have an ac then buy and ac.")