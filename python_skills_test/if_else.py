
good_credit = True
salary = 40_000
age = 22


# loan approval logic
if good_credit:
    if salary > 30_000:
        if age > 30:
            approval = 10_000
        else:
            approval = 5_000
    else:
       approval = 1_000 
else:
    approval = 0


# as an if-elif-else stack
if good_credit and salary > 30_000 and age > 30:
    approval = 10_000
elif good_credit and salary > 30_000:
    approval = 5_000
elif good_credit:
    approval = 1_000
else:
    approval = 0


3variable = 4