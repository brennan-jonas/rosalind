def readFile(filePath):
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]


def format_fasta(lines):
    sequences = {}
    current_header = None
    current_sequence = []

    for line in lines:
        if line.startswith('>'):
            if current_header:
                sequences[current_header] = ''.join(current_sequence)
            current_header = line[1:]  # Remove the '>'
            current_sequence = []
        else:
            current_sequence.append(line)

    if current_header:
        sequences[current_header] = ''.join(current_sequence)

    return sequences


filePath = 'test.fasta'  # edit this with your filepath
lines = readFile(filePath)
sequences = format_fasta(lines)

for seqID, fasta in sequences.items():
    print(f'SeqID: {seqID}')
    print(f'FASTA Content: {fasta}')
