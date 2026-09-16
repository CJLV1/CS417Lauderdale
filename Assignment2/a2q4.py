import random
BASES = "ACGT"

def frequencyTable(dnaList):
    n = max([len(dna)for dna in dnaList])
    frequency_matrix = {
        'A': [0]*n,
        'C': [0]*n,
        'T': [0]*n,
        'G': [0]*n
        }
    for dna in dnaList:
        for index, base in enumerate(dna):
            frequency_matrix[base][index]+=1

    return frequency_matrix

def generateDna(length):
    return "".join(random.choice(BASES) for _ in range(length))

def mutate(dna, numOfMutation):
    bases = list(dna)
    for _ in range(numOfMutation):
        position = random.randint(0, len(bases)-1)
        bases[position] = random.choice(BASES)
    return "".join(bases)

def print_frequency_table(freq_table, chunk_size=100):
    """Print the frequency table in readable chunks, plus totals per
    base across the whole sequence."""
    n = len(freq_table['A'])
    for start in range(0, n, chunk_size):
        end = min(start + chunk_size, n)
        print(f"positions {start}-{end - 1}:")
        for base in BASES:
            print(f"  {base}: {freq_table[base][start:end]}")
        print()
 
    print("Totals per base:")
    for base in BASES:
        print(f"  {base}: {sum(freq_table[base])}")

def main():
    length = 1000
    mutations = 100
    dna = generateDna(length)

    unmutatedTable = frequencyTable([dna])
    mutatedDNA = mutate(dna, mutations)
    mutatedTable = frequencyTable([mutatedDNA])


    print("Un-mutated DNA: \n")
    print_frequency_table(unmutatedTable)

    print("Mutated DNA \n")
    print_frequency_table(mutatedTable)

if __name__ == "__main__":
    main()