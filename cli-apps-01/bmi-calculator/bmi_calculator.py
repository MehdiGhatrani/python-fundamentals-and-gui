# get wieght and height
def user_input():
    height = float(input("enter your height (m): "))
    weight = float(input("enter your weight (kg): "))
    return height, weight


# calculate bmi
def calculate_bmi(height, weight):
    bmi = weight // (height ** 2)
    print(bmi)
    return bmi


# bmi result
def result(bmi):
    if bmi <= 18.5:
        print("Underweight")
    elif 18.5 < bmi <= 23:
        print("Healthy")    
    elif 23 < bmi <= 27:
        print("Overweight")    
    else:
        print("Obese")    


# main function
def main():
    height, weight = user_input()
    bmi = calculate_bmi(height, weight)

    result(bmi)


if __name__ == "__main__":
    main()