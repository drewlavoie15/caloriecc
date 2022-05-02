gender = input("What is your gender (M or F): ")
age = int(input("What is your age (15-80): "))
weight = int(input("What is your weight (lbs): "))
height = int(input("What is your height (inches): "))

# while gender != 'M' and gender != 'F':
while gender not in ["M", "F"]:
    print("Please use either M or F")
    gender = input("What is your gender (M or F): ")

while int(age) < 15 or int(age) > 80:
    print("Please use pick an age between 15 and 80")
    age = input("What is your age (15-80):  ")

while int(weight) < 50 or int(weight) > 300:
    print("Please use pick a weight between 50 and 300 lbs")
    age = input("What is your weight (lbs)):  ")

while int(height) < 40 or int(height) > 84:
    print("Please use pick a height between 40 and 84 inches")
    age = input("What is your height (inch)):  ")


def bmrcalc():

    if gender == "M":
        x = 66
        W = 6.23 * int(weight)
        H = 12.7 * int(height)
        A = 6.8 * int(age)
        # bmrm = 66 + W + H - A
        # print(bmrm)
    elif gender == "F":
        x = 665
        W = 4.35 * int(weight)
        H = 4.7 * int(height)
        A = 4.7 * int(age)
        # bmrw = 665 + W + H - A
        # print(bmrw)
    bmr_result = x + W + H - A
    return bmr_result


bmr = bmrcalc()

print("Your bmr is " + str(bmr))

activity_level = input("What is your activity level (none, light, moderate or heavy): ")
while activity_level not in ["none", "light", "moderate", "heavy"]:
    print("Please pick either none, light, moderate or heavy")
    activity_level = input(
        "What is your activity level (none, light, moderate or heavy): "
    )

# This is to calculate the AMR (amount of calories needed to say at current weight with consderation of activiy lvl)
def activity_calc(bmr_result, activity_level):

    if activity_level == "none":
        activity_level = 1.2 * bmr_result
    elif activity_level == "light":
        activity_level = 1.375 * bmr_result
    elif activity_level == "moderate":
        activity_level = 1.55 * bmr_result
    elif activity_level == "heavy":
        activity_level = 1.725 * bmr_result

    return float(activity_level)


activity = activity_calc(bmr, activity_level)

print(
    "The amount of calories you should consume a day is based on activiy level to maintain your current weight is: "
    + str(activity)
)

goal = input("What is your weight goal (gain, lose or maintain): ")
while goal not in ["gain", "lose", "maintain"]:
    print("Please pick either gain, lose or maintain")
    goal = input("What is your weight goal (gain, lose or maintain): ")


def calorie_calc(activity, goal):
    if goal == "maintain":
        goal = activity
    elif goal == "lose":
        goal = print(
            "Try to up your acitivy level and reduce calories. You should cosume "
            + str(activity - 500)
            + "calories a day"
        )
    elif goal == "gain":
        goal = print(
            "Try to moderate your acitivy level and increase calories. You should cosume around "
            + str(activity * 1.15)
            + "calories a day"
        )
    return goal


cal = calorie_calc(activity, goal)
print(cal)
