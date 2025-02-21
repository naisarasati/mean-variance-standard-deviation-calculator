import numpy as np

def calculate(list):

    #1. Set Function to Containing List in 9 Digits
    if len(list) != 9:
        raise ValueError("Your list must consist of nine numbers.")

    #2. Set Numpy Output
    npMatrix = np.array(list).reshape(3, 3)

    #3. Set Dictionary
    calculations = {
        'mean': [npMatrix.mean(axis=0).tolist(), npMatrix.mean(axis=1).tolist(), npMatrix.mean().tolist()],
        'variance': [npMatrix.var(axis=0).tolist(), npMatrix.var(axis=1).tolist(), npMatrix.var().tolist()],
        'standard deviation': [npMatrix.std(axis=0).tolist(), npMatrix.std(axis=1).tolist(), npMatrix.std().tolist()],
        'max': [npMatrix.max(axis=0).tolist(), npMatrix.max(axis=1).tolist(), npMatrix.max().tolist()],
        'min': [npMatrix.min(axis=0).tolist(), npMatrix.min(axis=1).tolist(), npMatrix.min().tolist()],
        'sum': [npMatrix.sum(axis=0).tolist(), npMatrix.sum(axis=1).tolist(), npMatrix.sum().tolist()]
    }

    return calculations