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


def main():
    data = loadJson("resources/combined.json")
    sourceMap = data["contracts"]["/sources/test1.sol:MyContract"]["srcmap-runtime"]
    bin = data["contracts"]["/sources/test1.sol:MyContract"]["bin-runtime"]
    print(bin)
    srcMapFull = sourceMapPreprocess(sourceMap)
    instructions = binPreprocess(bin)
    print(srcMapFull)
    print(instructions)
    print(len(instructions))
    f = open("resources/test1.sol", 'r')
    sourceCode = repr(f.read())
    print(sourceCode)
    print(sourceCode[156:162])

main()