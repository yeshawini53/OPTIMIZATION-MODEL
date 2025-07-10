from pulp import LpMaximize, LpProblem, LpVariable, value

# Define the problem
model = LpProblem("Maximize_Profit", LpMaximize)

# Define decision variables
A = LpVariable("Product_A", lowBound=0, cat='Integer')
B = LpVariable("Product_B", lowBound=0, cat='Integer')

# Objective function
model += 40 * A + 50 * B, "Total_Profit"

# Constraints
model += 2 * A + 3 * B <= 100, "Labor_Constraint"
model += 3 * A + 2 * B <= 90, "Material_Constraint"

# Solve the problem
model.solve()

# Results
print("Status:", model.status)
print("Produce Product A:", A.varValue)
print("Produce Product B:", B.varValue)
print("Total Profit:", value(model.objective))
