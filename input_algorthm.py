from matrix import excel_set, x_1_mean, x_2_mean, x_3_mean, x_4_mean


# The function allows user to input values representing the characteristics of the home they are looking for
def input_function(w1, w2, w3, w4, b):

    size = int(input("Please enter the size of the house:"))
    num_bedrooms = int(input("Please enter the num_bedroom:"))
    num_floors = int(input("Please enter the num_floors:"))
    age_home = int(input("Please enter the age_home:"))

    size = (size - x_1_mean) / (excel_set["Max_x_1"][0] - excel_set["Min_x_1"][0])
    num_bedrooms = (num_bedrooms - x_2_mean) / (excel_set["Max_x_2"][0] - excel_set["Min_x_2"][0])
    num_floors = (num_floors - x_3_mean) / (excel_set["Max_x_3"][0] - excel_set["Min_x_3"][0])
    age_home = (age_home - x_4_mean) / (excel_set["Max_x_4"][0] - excel_set["Min_x_4"][0])

    price_prediction = w1 * size + w2 * num_bedrooms + w3 * num_floors + w4 * age_home + b

    print(price_prediction)



