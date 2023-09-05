which_cities_you_be = input('Enter cities which you visit last 10 years>>>').title().split()
which_cities_you_want_be = input('Enter cities which you want to visit next 10 years>>>').title().split()

cites_be = set(which_cities_you_be)
cites_want_be = set(which_cities_you_want_be)
print(cites_be)
print(cites_want_be)

cites_be_and_want = (cites_be.intersection(cites_want_be))
print(cites_be_and_want)

if not cites_be_and_want:
    print('You are open to something new!')
else:
    print(f"I think you like this cities the most: {', '.join(cites_be_and_want)} ")
