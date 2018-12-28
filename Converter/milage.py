print('How many kilometers have you ran today?')
userinput = input()
kilometers_ran = int(userinput)
miles_ran = kilometers_ran / 1.609
miles_ran= int(miles_ran)
print(f"wow {kilometers_ran} kilometers is about {miles_ran} miles. That's a lot of miles!")
