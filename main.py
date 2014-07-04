from roster import Roster

roster = Roster('partyco.json')
# roster = Roster('linkedlist.json')

print 'Best'
b = roster.ceo.best_plan()
print b.score
print b.list_names()

print 'If CEO attending'
b_attending = roster.ceo.attending_plan()
print b_attending.score
print b_attending.list_names()