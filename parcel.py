def calculate_postage(weight):
    cost = 1.00
    if weight > 1:
        cost += (weight - 1) * 0.50
    return cost

weight = float(input("Enter the weight of the parcel (in pounds): "))

postage = calculate_postage(weight)
print(f"The postage for a {weight} pound parcel is ${postage:.2f}")
