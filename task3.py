#take inputs from user.
minimum_time = 100
swim = int(input("Enter the time in minutes for the swim: "))
cycle = int(input("Enter the time in minutes for the cycle: "))
run = int(input("Enter the time in minutes for the run: "))

#use collected inputs to determine which award is received.
total = swim + cycle + run
if total <= minimum_time:
    print("Provincial Colours")
elif total <= minimum_time + 5:
    print("Provincial Half Colours")
elif total <= minimum_time + 10:
    print("Provincial Scroll")
else:
    print("No Award")