import ducks_07_raise_error as ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
ducks3 = ducks.Duck()
ducks4 = ducks.Duck()
ducks5 = ducks.Duck()
ducks6 = ducks.Duck()
ducks7 = ducks.Duck()
percy = ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(ducks3)
flock.add_duck(ducks4)
flock.add_duck(ducks5)
flock.add_duck(ducks6)
flock.add_duck(ducks7)
flock.add_duck(percy)

flock.migrate()
