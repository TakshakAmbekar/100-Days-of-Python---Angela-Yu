# pip install prettytable

from prettytable import PrettyTable

table = PrettyTable()

# using methods
table.add_column("Pokemon Name",[])
table.add_column("Type",[])
table.add_row(("Pikachu", "Electric"))
table.add_rows([("Bulbasaur", "Grass"), ("Squirtle", "Water"), ("Charmander", "Fire")])

# manipulating attributes
table.align = 'l'

print(table)

