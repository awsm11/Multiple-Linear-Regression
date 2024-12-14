import numpy as np
import pandas as pd


# A function used to extract data from an Excel file.
excel_set = pd.read_excel(r'\Excel Data\gd_data.xlsx')

x_1 = []
x_2 = []
x_3 = []
x_4 = []
y_1 = []

# The number of data points for each feature
a = len(excel_set["Size"])

x_1_mean = 0
x_2_mean = 0
x_3_mean = 0
x_4_mean = 0

# Calculating the mean values of each dataset
for i in range(a):
    x_1_mean += excel_set["Size"][i]
    x_2_mean += excel_set["Num of Bedroom"][i]
    x_3_mean += excel_set["Num of Floors"][i]
    x_4_mean += excel_set["Age of Home"][i]

x_1_mean = x_1_mean / a
x_2_mean = x_2_mean / a
x_3_mean = x_3_mean / a
x_4_mean = x_4_mean / a

# Mean normalization applied to each feature
for i in range(a):

    x_1.append((excel_set["Size"][i] - x_1_mean) / (excel_set["Max_x_1"][0] - excel_set["Min_x_1"][0]))
    x_2.append((excel_set["Num of Bedroom"][i] - x_2_mean) / (excel_set["Max_x_2"][0] - excel_set["Min_x_2"][0]) )
    x_3.append((excel_set["Num of Floors"][i] - x_3_mean) / (excel_set["Max_x_3"][0] - excel_set["Min_x_3"][0]))
    x_4.append((excel_set["Age of Home"][i] - x_4_mean) / (excel_set["Max_x_4"][0] - excel_set["Min_x_4"][0]))
    y_1.append(excel_set["Price 1000s dollars"][i])


excel_data = np.array([x_1, x_2, x_3, x_4])

excel_data = np.transpose(excel_data)

y_1 = np.array(y_1)

m, n = excel_data.shape
