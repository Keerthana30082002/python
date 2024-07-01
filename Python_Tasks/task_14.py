def calculate_area(length, width):
    area = length * width
    return area


def find_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def classify_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Needs Improvement"


def calculate_discount(price, discount_percentage=10):
    discount_percentage = price - (price * discount_percentage / 100)
    return discount_percentage


a = calculate_area(3, 4)
print("Area =", a)
b = find_max(8, 45, 9)
print("Maximum is", b)
c = is_even(56)
print(c)
d = classify_score(95)
print(d)
e = calculate_discount(500, 25)
print("Discount is: ", e)
