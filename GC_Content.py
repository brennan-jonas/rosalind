#read data from FASTA File
def readFile(filePath):

    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
#Calculates the percentage of cytosine and guanine
def gc_content(seq):

    return round(
        ((seq.count('C')+ seq.count('G')) / len(seq)*100), 6)

FASTAFile = readFile('test//gc_content')

FASTADict = {}
FASTALabel = ""

print(FASTAFile)
#Converts file data into dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line
print(FASTADict)

ResultDict = {key: gc_content(value) for (key, value) in FASTADict.items()}
print(ResultDict)
#Finds max amount of gc/content
MaxGCKey = max(ResultDict, key=ResultDict.get)

print(f'{MaxGCKey[1:]}\n{ResultDict[MaxGCKey]}')
