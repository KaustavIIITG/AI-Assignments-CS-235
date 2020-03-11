import random
random.seed(42)
from random import randint as rand
from statistics import variance, mean


def weights_generator(size, start=40, end=80):
    """Returns list of student weights"""

    return [rand(start, end) for i in range(size)]


def population(number, size):
    """Generates and returns encoded form for each gene"""

    return [[rand(1, 3) for i in range(size)] for j in range(number)]


def crossover(parent_A, parent_B):
    """Crossover at random point"""

    crossover_point = rand(1, len(parent_A) - 1)
    child_A = parent_A[:crossover_point] + parent_B[crossover_point:]
    child_B = parent_B[:crossover_point] + parent_A[crossover_point:]
    return child_A, child_B


def mutation(gene):
    """Random index mutation"""

    mutation_index = rand(0, len(gene) - 1)
    gene[mutation_index] = rand(1, 3)
    return gene


def fitness_function(encoded, weights):
    """Returns average variance as fitness function"""

    group_1, group_2, group_3 = list(), list(), list()
    for i in range(len(encoded)):
        if encoded[i] == 1:
            group_1.append(weights[i])
        elif encoded[i] == 2:
            group_2.append(weights[i])
        else:
            group_3.append(weights[i])

    var1 = variance(group_1) if len(group_1) > 1 else 0
    var2 = variance(group_2) if len(group_2) > 1 else 0
    var3 = variance(group_3) if len(group_3) > 1 else 0

    return 1 / mean([var1, var2, var3])


def genetic_algorithm(genes, weights):
    """Applies genetic algorithm"""

    best_gene = genes[0]
    initial_fitness = fitness_function(best_gene, weights)
    final_fitness = initial_fitness

    for i in range(len(genes)):
        for j in range(i + 1, len(genes)):
            gene_A, gene_B = crossover(genes[i], genes[j])
            prob = rand(0, 1)
            if prob:
                gene_A = mutation(gene_A)
                gene_B = mutation(gene_B)
            if fitness_function(gene_A, weights) > final_fitness:
                final_fitness = fitness_function(gene_A, weights)
                best_gene = gene_A
            if fitness_function(gene_B, weights) > final_fitness:
                final_fitness = fitness_function(gene_B, weights)
                best_gene = gene_B

    return best_gene, final_fitness, initial_fitness


# 'size' refers to number of students i.e, size of each gene
# 'number' refers to the size of population i.e, number of genes
# 'weights' refers to the list of randomly assigned weights of students
# 'genes' refers to population

size = 20
number = 100
weights = weights_generator(size)
genes = population(number, size)

best_gene, final_fitness, initial_fitness = genetic_algorithm(genes, weights)

print("weights = {}\n".format(weights))
print("initial fitness = {}\n".format(initial_fitness))
print("initial gene = {}\n".format(genes[0]))
print("final fitness = {}\n".format(final_fitness))
print("best gene = {}".format(best_gene))

