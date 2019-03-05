import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import pgmpy
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
from flask import Flask
from flask import jsonify
from flask import request

def top_results(factor, k = 10):
    from itertools import product
    
    value_index = 0
    factor_table = []

    for prob in product(*[range(cardinality) for cardinality in factor.cardinality]):
        state = ["{state}".format(state=factor.state_names[list(factor.variables)[i]][prob[i]]) for i in range(len(factor.variables))]
        probability = factor.values.ravel()[value_index]
        factor_table.append({'disease': state[0], 'probability': probability})
        value_index += 1

    factor_table.sort(key = lambda x: x['probability'], reverse = True) 
    factor_table = factor_table[:k]

    return factor_table

data = pd.read_csv('hw4_data_long.csv')
root = list(data)[0]
model = BayesianModel(map(lambda x: [root, x], list(data)[1:]))
model.fit(data, estimator = MaximumLikelihoodEstimator)
inference = VariableElimination(model, state_names = model.get_cpds()[0].state_names)

app = Flask(__name__)

@app.route("/query")
def query():
    evidence = {k: int(v) for k, v in request.args.items()}
    query = inference.query([root], evidence = evidence)
    res = query[root]
    res.state_names = inference.state_names
    return jsonify(top_results(res))