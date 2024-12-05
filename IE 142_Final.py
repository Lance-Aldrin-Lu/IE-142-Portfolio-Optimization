import cvxpy as cp
import numpy as np
import pandas as pd

file_path = "C:\\Users\\Lance Aldrin Lu\\Documents\\Python Programming\\CS 11 Crazy\\IE 142 Stock Data Sheet - Lance_Copy.csv"
df = pd.read_csv(file_path)
returns = df.to_numpy()

expected_returns = np.mean(returns, axis=0)     # Mean return value i for each stock 1
cov_matrix = np.cov(returns, rowvar=False)      # Covariance matrix

i = len(expected_returns)                       # Number of stocks to analyze
p = cp.Variable(i)                              # proportion i for each stock i



portfolio_return = p @ expected_returns          # Summation of (p_i * r_i) for all i
portfolio_var = cp.quad_form(p, cov_matrix)      # [theta Transpose][phi][theta]


# For the whole Portfolio constraint
max_volatility_annual = 0.1
max_volatility_daily = max_volatility_annual / np.sqrt(252)
max_port_var = max_volatility_daily**2


# For the Stock i constraints
var_s11 = cov_matrix[11, 11]
max_volatility_s11_annual = 0.01
max_volatility_s11_daily = max_volatility_s11_annual / np.sqrt(252)
max_var_s11 = max_volatility_s11_daily**2

var_s14 = cov_matrix[14, 14]
max_volatility_s14_annual = 0.02
max_volatility_s14_daily = max_volatility_s14_annual / np.sqrt(252)
max_var_s14 = max_volatility_s14_daily**2


constraints = [
                cp.sum(p) == 1,                   # Total Probability Rule (and Max Budget)
                portfolio_var <= max_port_var,    # Max Volatality of the Whole Portfolio
                
                p >= 0                            # Non-negativity
]

"""
Contraints Pool:
p[11]**2 * var_s11 <= max_var_s11,   # Max Volatility for stock i (currently set to limit stock 11)
p[14]**2 * var_s14 <= max_var_s14,   # Max Volatility for stock i (currently set to limit stock 14)
p[0] >= 0.12,                        # Lower limit for a stock i

p[0] <= 0,                       # Upper limit for a stock i
p[3] <= 0,                       # Upper limit for a stock i
p[8] <= 0,                       # Upper limit for a stock i
p[9] <= 0,                       # Upper limit for a stock i
p[12] <= 0,                      # Upper limit for a stock i
p[16] <= 0,                      # Upper limit for a stock i
p[18] <= 0,                      # Upper limit for a stock i


"""


objective_function = cp.Maximize(portfolio_return)      # Objective function

problem = cp.Problem(objective_function, 
                     constraints)                       


problem.solve(solver="ECOS")
# 

print("Optimal Proportions:")

for stock in range(0, i):
    print("Stock " + str(stock) + ": " + str(p[stock].value * 100))
    

#  + "   " + str(expected_returns[stock])

print("")

print("Optimal Portfolio Return:", portfolio_return.value)
print("Optimal Portfolio Variance:", portfolio_var.value)

print("")

for cons in range(0, len(constraints)):
    print("Dual Constraint " + str(cons) + ": " + str(problem.constraints[cons].dual_value))
