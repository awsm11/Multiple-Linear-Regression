This algorithm allows you to estimate your target data using a gradient descent model, which establishes a statistical relationship 
between the given data tables or arrays read from an Excel file.

The code is representing the Linear Regression for multiple variables.

To recap,
This algorithm provides an approximate price of a house based on features such as size, number of rooms, number of corridors 
and the age of the building in a specific region. These features are available in an Excel file in tabular format
and the algorithm retrieves the relevant data from the Excel table to present the desired information.

Additionally, by modifying the type or quantity of data in the Excel table, the algorithm can be adapted to offer predictions 
for various applications. By following the comments in the Python code files, you can apply this algorithm to your own data 
by making the necessary adjustments.
 
*** If you run the code without any changes ***
!! Essential !! : First, you need to download the Excel file containing the data table in order to run the code correctly. 
The algorithm uses specific data from the Excel file as an example.
!! Essential !! : Secondly, you need to specify the location of the Excel file you downloaded in the pd.read_excel function, 
as shown below:
(this function is in the file "matrix.py")

pd.read_excel(r'\file location\excel file name')
for instance:
excel_set = pd.read_excel(r'\Excel Data\data.xlsx'

The example usage of this algorithm takes a few seconds without changing any iteration counts.
If you increase iteration counts, the prediction will be more close to the its exact solution.
However this approach could take more times depend on number of iterations.
More iteration means more time.

If model function does not make sense in terms of the data defined by you;
- The data may not be suitable for linear regression with multi variables.
- Increasing the number of iterations might be solution of the problem.


