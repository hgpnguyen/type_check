import json
import csv

def loadJson(filename):
    with open(filename) as json_file: 
        data = json.load(json_file)
        return data

def variable_search(node):
    if "nodeType" not in node.keys():
        return False
    if node["nodeType"] == "VariableDeclaration" and node["name"] != "":
        return True
    else: 
        return False

def jsonSearch(json_, key_search):
    result = []
    if isinstance(json_, dict):
        if key_search(json_):
                result.append(json_)
        for key, value in json_.items():
            if isinstance(value, dict) or isinstance(value, set) or isinstance(value, list):
                new_result = jsonSearch(value, key_search)
                result += new_result
    elif isinstance(json_, set) or isinstance(json_, list):
        for element in json_:
            if isinstance(element, dict) or isinstance(element, set) or isinstance(element, list):
                new_result = jsonSearch(element, key_search)
                result += new_result
    return result

def get_var_Type(nodes):
    results = []
    for node in nodes:
        id = node["id"]
        name = node["name"]
        type = node["typeDescriptions"]["typeString"]
        results.append([id, name, type])
    return results

def output_csv(results):
    headers = ["id", "name", "type"]
    with open("resources/output/output.csv", 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(headers)
        writer.writerows(results)


def main():
    ast = loadJson("resources/5_0_10/test8.sol_json.ast")
    nodes = jsonSearch(ast, variable_search)
    var_types = get_var_Type(nodes)
    print(var_types)
    output_csv(var_types)

if __name__ == '__main__':
    main()