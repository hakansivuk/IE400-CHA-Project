# Santa's Little Helper

This project aims to solve linear integer problems with respect to a set of problems. //TODO define the problem a little bit more

## How to Run

The program can be run as follows:
> python3 Solver.py dataArg problemIndexArg

* dataArg: name of the data file to run. If you want to use default data initially given, use **def-file** as the argument. If the argument here is not equal to the def-file, it would try to open your custom data file to setup the model.
* problemIndexArg: is problem number you want to solve. It should be between 1 <= x <= 4.
An example usage is given as below:
>python3 Solver.py hello-world 3 
>=> This would run the program with a file named hello-world xlsx f

You do not always have to give arguments to run the program.  
### Default Configuration
> python3 Solver.py

This would run the program with the given data.xlsx on all 4 problems. 

### Custom Data Configuration
>python3 Solver.py data-file-name

This would run the program with the given data-file-name.xlsx on all 4 problems.

### Specific Problem to Solve Configuration
>python3 Solver,py data-file-name 1

This would run the program with the given data-file-name.xlsx on problem 1.

## Adding Your Own Data to Test with Different Input Cases

Enter DataFolder which is located at the root of the project. Create or copy paste your own .xlsx data file inside this folder. The custom data file must be in xlsx format. Other file types are not supported. Finally, run the program with the filename argument. To learn how to run the program with custom data argument, please refer to "How to Run". 

## Developers

* Hakan Sivuk, 21601899
* Cevat Aykan Sevinç, 21703201
* Ahmet Berk Eren, -
