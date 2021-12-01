import json
import tree
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/v1/b-trees/height', methods=['POST'])
def questionOne(api):  # API es un diccionario
    record = json.loads(request.data)
    listTree = record["toTree"]
    head = tree.makeTree(listTree)
    res = jsonify({"height": head.getHeight()})
    return res


@app.route('/v1/b-trees/neighbors', methods=['POST'])
def questionTwo():
    record = json.loads(request.data)
    listTree = record["toTree"]
    node = record["node"]
    head = tree.makeTree(listTree)
    bfs = tree.bfsWithIndexes(head)
    nodes = bfs[0]
    indexes = bfs[1]
    idx = nodes.index(node)
    neighborsIndexes = [it for it in range(len(indexes)) if indexes[it] == indexes[idx] and it != idx]
    neighbors = [nodes[it] for it in neighborsIndexes]
    res = jsonify({"neighbors": neighbors})
    return res


@app.route('/v1/b-trees/bfs', methods=['POST'])
def questionThree():
    record = json.loads(request.data)
    listTree = record["toTree"]
    head = tree.makeTree(listTree)
    resNum = tree.bfs(head)
    res = jsonify({"toTree": resNum})
    return res


def prueba():
    api = {"toTree": [3, 2, 1, 4, 5]}
    res = questionThree(api)
    for num in res:
        print(num)


prueba()



def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)



def heightApi():
    record = json.loads(request.data)
    questionOne(record)



def BFSApi():
    record = json.loads(request.data)
    questionThree(record)
