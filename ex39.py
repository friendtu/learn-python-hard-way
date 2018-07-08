states={
    'Oregon':'OR',
    'Florida':'FL',
    'Galifornia':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

cities={
    'CA':"San Francisco",
    'MI':"Detroit",
    'FL':"Jacksonville"
}

cities['NY']="New York"
cities['OR']='Portland'

print "Michigan has ", cities[states['Michigan']]

print "items():",states.items()

for state,abbrev in states.items():
    print "%s is abbreviated %s" % (state,abbrev)

state=states.get('Texax',None)
if not state:
    print "Sorry, no Texax."

city=cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is: %s" % city

