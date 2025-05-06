from mlrose_hiive as mlrose
import aero

fitness = mlrose.CustomFitness(aero.fitness_function)
rpoblema = mlrose.DiscreteOpt(
    length = 12,
    fitness_fn = fitness,
    maximaze = false,
    max_val = 10
)

# hill climb
solucao, custo, _ = mlrose.hill_climb(problema, random_state=1)
aero.listar_voos(solucao)

# simulating annealing
solucao, custo, _ = mlrose.simulated_annealing(
    problema, 
    schedule=mlrose.GeomDecay(init_temp=10000), 
    random_state=1
)
aero.listar_voos(solucao)

# alg. gebético
solucao, custo, _ = mlrose.hill_climb(
    problema, 
    pop_size=500,
    mutation_prob=0.2,
    random_state=1
)
aero.listar_voos(solucao)
