import pandas as pd

# Population data from GapMinder
population = pd.read_csv("pop.csv")


#Wide to Long
long_population = population.melt(id_vars=["country"], var_name="year", value_name="population")
long_population.head

#Long to wide
wide_population = long_population.pivot(index = "country", columns = "year", values = "population")
wide_population = wide_population.reset_index()
wide_population.head
