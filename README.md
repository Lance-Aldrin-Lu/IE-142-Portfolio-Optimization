# IE-142-Portfolio-Optimization

1. Install the needed package dependencies for the code to work. Copy one line at the time to the command prompt to install.
```
pip install "cvxpy[CBC,CVXOPT,GLOP,GLPK,GUROBI,MOSEK,PDLP,SCIP,XPRESS]"
```
```
pip install numpy
```
```
pip install pandas
```
2. Download the CSV data sheet.

3. Copy the Python code file in your preferred code development environment (e.g. VS Code).

4. Going back to the CSV file, locate it and fully copy its File Path as it is needed as an argument in the code.

5. In the code, locate the variable named “file_path”, replace the copied file path in Step 5 into the code. Make sure it is correct and that the slash should be replaced into double slashes for the string to work.

6. Make, manipulate, and adjust the arguments for the variable named “constraints” and as well as specified parameters (e.g. allowable max portfolio volatility) as seen in the Sensitivity Analysis. Note that the 1st stock is Stock 0 (0 index).
