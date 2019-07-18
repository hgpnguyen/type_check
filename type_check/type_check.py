import json

FIRST_PUSH_INS_CODE = 96 # PUSH1 (60)
LAST_PUSH_INS_CODE = 127 # PUSH32 (7f)

def loadJson(filename):
    with open(filename) as json_file: 
        data = json.load(json_file)
        return data

def sourceMapReducer(acc, curr):
    fullParts = []
    for i in range(4):
        fullPart = curr[i] if i < len(curr) and curr[i] != '' else acc[i]
        fullParts.append(fullPart)
    newAcc = (int(fullParts[0]), int(fullParts[1]), int(fullParts[2]), fullParts[3], acc[4] + 1)
    return newAcc

def scan(arr, reducer, initialValue):
    accumulator = initialValue;
    result = []
    for currValue in arr:
        curr = reducer(accumulator, currValue)
        accumulator = curr
        result.append(curr)
    return result

def sourceMapPreprocess(srcmap):
    items = srcmap.split(';')
    items = list(map(lambda x: x.split(':'), items))
    srcMapFull = scan(items, sourceMapReducer, (0,0,0,'-',-1))
    return srcMapFull

def binPreprocess(bin):
    bin = bytes.fromhex(bin)
    i = 0
    instructions = []
    while i < len(bin):
        byte = bin[i]
        if byte >= FIRST_PUSH_INS_CODE and byte <= LAST_PUSH_INS_CODE:
            pushDataLend = byte - FIRST_PUSH_INS_CODE + 1;
            pushDataStart = i + 1
            pushData = bin[pushDataStart: pushDataStart + pushDataLend]
            instruction = [byte, pushData, len(instructions)]
            i += pushDataLend + 1
        else:
            instruction = [byte, len(instructions)]
            i += 1
        instructions.append(instruction)
    return instructions

def assign_search(node):
    if "nodeType" not in node.keys():
        return False
    if (node["nodeType"] == "VariableDeclarationStatement" and node["initialValue"] != None):
            return True
    elif (node["nodeType"] == "Assignment"):
        return True
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

def scan_Exp(exp, results=[]):
    if exp == None:
        return
    if exp["nodeType"] == "BinaryOperation":
        scan_Exp(exp["leftExpression"], results)
        scan_Exp(exp["rightExpression"], results)
    elif exp["nodeType"] == "UnaryOperation":
        scan_Exp(exp["subExpression"], results)
    elif exp["nodeType"] == "TupleExpression":
        for com in exp["components"]:
            scan_Exp(com, results)
    else:
        results.append(exp["typeDescriptions"]["typeString"])


def print_result(opps):
    results = []
    for opp in opps:
        leftExp = (([opp["leftHandSide"]] if opp["leftHandSide"]["nodeType"] != "TupleExpression" else opp["leftHandSide"]["components"]) 
                    if opp["nodeType"] == "Assignment" else opp["declarations"])
        right = opp["rightHandSide"] if opp["nodeType"] == "Assignment" else opp["initialValue"]
        rightExp = [right] if right["nodeType"] != "TupleExpression" else right["components"]
        if len(rightExp) != len(leftExp):
            rightExp = len(leftExp) * rightExp
        for l, r in zip(leftExp, rightExp):
            if not l: continue
            result = [opp["src"]]
            result.append(l["typeDescriptions"]["typeString"])
            scan_Exp(r, result)
            results.append(result)
    return results

def main():
    #data = loadJson("resources/combined.json")
    #sourceMap = data["contracts"]["/sources/test1.sol:MyContract"]["srcmap-runtime"]
    #bin = data["contracts"]["/sources/test1.sol:MyContract"]["bin-runtime"]
    ast = loadJson("resources/test6.sol_json.ast")
    #print(bin)
    #srcMapFull = sourceMapPreprocess(sourceMap)
    #instructions = binPreprocess(bin)
    f = open("resources/test1.sol", 'r')
    sourceCode = repr(f.read())
    add_opp = jsonSearch(ast, assign_search)
    print(print_result(add_opp))

if __name__ == '__main__':
    main()