import cvxpy as cp
import numpy as np
import pandas as pd

file_path = "C:\\Users\\Lance Aldrin Lu\\Documents\\Python Programming\\CS 11 Crazy\\IE142test.csv"
df = pd.read_csv(file_path)
returns = df.to_numpy()

expected_returns = np.mean(returns, axis=0)     # Mean return value i for each stock 1
cov_matrix = np.cov(returns, rowvar=False)      # Covariance matrix

i = len(expected_returns)                       # Number of stocks to analyze
p = cp.Variable(i)                              # proportion i for each stock i


# Stock proportion naming
p1 = p[0]
p2 = p[1]
p3 = p[2]
p4 = p[3]


portfolio_return = p @ expected_returns          # Summation of (p_i * r_i) for all i
portfolio_var = cp.quad_form(p, cov_matrix)      # [theta Transpose][phi][theta]


# For the whole Portfolio constraint
max_volatility = 0.015
max_port_var = max_volatility**2


# For the Stock i constraint
var_s1 = cov_matrix[0, 0]
max_var_s1 = 0.005


constraints = [
                cp.sum(p) == 1,                   # Total Probability Rule (and Max Budget)
                portfolio_var <= max_port_var,    # Max Volatality of the Whole Portfolio
                p1**2 * var_s1 <= max_var_s1,     # Max Volatility for stock i (currently set to limit stock 1)
                p2 >= 0.2,                        # Lower limit for a stock i (currently set to limit stock 2)
                p2 <= 0.3,                        # Upper limit for a stock i (currently set to limit stock 2)
                p >= 0                            # Non-negativity
]

objective_function = cp.Maximize(portfolio_return)      # Objective function

problem = cp.Problem(objective_function, 
                     constraints)                       


problem.solve(solver="ECOS")
print("Solver: ECOS")
print("Optimal Weights:", p.value)
print("Optimal Portfolio Return:", portfolio_return.value)
print("Optimal Portfolio Variance:", portfolio_var.value)
print()