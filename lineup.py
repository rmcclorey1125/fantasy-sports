import pandas as pd
import cvxpy as cp

salaries = pd.read_csv("/Users/ronan/Downloads/FanDuel-NFL-2020-11-15-51566-players-list.csv")

pos = salaries["Position"].values
sal = salaries["Salary"].values
nam = salaries["Nickname"].values
pts = salaries["FPPG"].values

isQB = (pos == 'QB').astype(float)
isRB = (pos == 'RB').astype(float)
isTE = (pos == 'TE').astype(float)
isWR = (pos == 'WR').astype(float)
isD = (pos == 'D').astype(float)

number_of_players = len(pos)
x = cp.Variable(number_of_players, boolean=True)

constraints = [
    sum(x) == 9,
    x @ sal <= 60000.0,
    x @ isQB == 1,
    x @ isTE >= 1,
    x @ isRB >= 2,
    x @ isWR >= 3,
    x @ isD == 1]

objective = cp.Maximize(pts @ x)

prob = cp.Problem(objective, constraints)

prob.solve()