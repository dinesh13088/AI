import random

def create_chromosome():
    return [random.choice([0, 1]) for _ in range(11)]


def decode_chromosome(chromosome):
    sign = -1 if chromosome[0] == 1 else 1
    integer_part = int(''.join(map(str, chromosome[1:5])), 2)
    residual_part = int(''.join(map(str, chromosome[5:])), 2) / 64
    return sign * (integer_part + residual_part)


def calculate_fitness(x):
    return abs(2 * x**2 + x - 6)


def crossover(parent1, parent2):
    return [random.choice([gene1, gene2]) for gene1, gene2 in zip(parent1, parent2)]


def mutate(chromosome, mutation_rate=0.1):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in chromosome]


def genetic_algorithm():
    population_size = 10
    generations = 10
    mutation_rate = 0.1

    population = [create_chromosome() for _ in range(population_size)]

    for generation in range(generations):
        print(f"\nGeneration {generation + 1}:")

        decoded = [decode_chromosome(chrom) for chrom in population]
        fitness_scores = [calculate_fitness(x) for x in decoded]


        for i, (chrom, x, fitness) in enumerate(zip(population, decoded, fitness_scores)):
            print(f"Chromosome {i + 1}: {''.join(map(str, chrom))} = {x:.6f}, Fitness: {fitness:.6f}")


        sorted_population = [chrom for _, chrom in sorted(zip(fitness_scores, population))]
        parents = sorted_population[:population_size//2]


        new_population = parents.copy()
        

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            mutated_child = mutate(child, mutation_rate)
            new_population.append(mutated_child)

        population = new_population


    best_chromosome = min(population, key=lambda c: calculate_fitness(decode_chromosome(c)))
    best_solution = decode_chromosome(best_chromosome)
    print(f"\nBest solution found: x = {best_solution:.6f}")
    print(f"Fitness: {calculate_fitness(best_solution):.6f}")

genetic_algorithm()
