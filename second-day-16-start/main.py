# import turtle as t

# tony = t.Turtle()


# tony.shape("turtle")
# tony.color("red")
# tony.forward(100)


# my_screen = tony.Screen()
# my_screen.exitonclick()
# ------------------------------#
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
