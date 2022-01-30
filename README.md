# Santa's Little Helper

  

This project aims to solve linear integer problems with respect to a set of problems. Problems are different variations of well-known travelling salesman problem. Details can be found from [HW File](https://github.com/hakansivuk/IE400-CHA-Project/blob/main/IE400-Project-Fall2020-2021.pdf) 

  

## How to Setup (Python dependencies)

  

You need to install Python3 on your computer. You can refer to the Internet or contact us if your computer does not have Python (we highly doubt it that you would not have Python)

  

For our solver model, we use the google's linear integer programming solver. If the command below does not make the trick for you, follow the instructions here: https://developers.google.com/optimization/install.

  

> python3 -m pip install --upgrade --user ortools

  

We are also using pandas to access xlsx file. Below command should do the trick if you do not have pandas module.

  

> pip install pandas

> pip install xlrd (optional dependency, but if you do not have it, project wont work)

> pip install openpyxl (this is because given file extension is xlsx and this is not supported by pandas at the moment, we need to change engine of pandas)

  

## How to Run

  

The program can be run as follows:

  

> python3 Solver.py dataArg problemIndexArg

  

* dataArg: name of the data file to run. If you want to use default data initially given, use **def-file** as the argument. If the argument here is not equal to the def-file, it would try to open your custom data file to setup the model.

* problemIndexArg: is problem number you want to solve. It should be between 1 <= x <= 4.

An example usage is given as below:

> python3 Solver.py hello-world 3
> => This would run the program with a file named hello-world.xlsx on the problem 3.

> python3 Solver.py def-file 1
> => This would run the program with the default data file data.xlsx on the problem 1.

  

You do not always have to give arguments to run the program.

  

### Default Configuration

  

> python3 Solver.py

  

This would run the program with the given data.xlsx on all 4 problems.

  

### Custom Data Configuration

  

> python3 Solver.py data-file-name

  

This would run the program with the given data-file-name.xlsx on all 4 problems.

  

### Specific Problem to Solve Configuration

  

> python3 Solver,py data-file-name 1

  

This would run the program with the given data-file-name.xlsx on problem 1.

  

## Adding Your Own Data to Test with Different Input Cases

  

Enter DataFolder which is located at the root of the project. Create or copy paste your own .xlsx data file inside this folder. The custom data file must be in xlsx format. Other file types are not supported. Finally, run the program with the filename argument. To learn how to run the program with custom data argument, please refer to "How to Run".

  

## Developers

  

- Hakan Sivuk, 21601899

- Cevat Aykan Sevinç, 21703201

- Ahmet Berk Eren, 21602055
