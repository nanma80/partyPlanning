import json
from person import Person

class Roster:
  def __init__(self, filename):
    self.filename = filename
    self.ceo = None
    self.populate_dictionary()
    self.populate_children()

  def import_from_json(self):
    with open(self.filename, 'r') as f:
      data = json.load(f)
    return data

  def populate_dictionary(self):
    self.dictionary = {}
    for person_hash in self.import_from_json():
      self.dictionary[person_hash['name']] = \
        Person(person_hash['name'], person_hash['boss'], person_hash['party-animal-score'])

  def populate_children(self):
    for person in self.dictionary.values():
      if person.boss_name:
        boss = self.dictionary[person.boss_name]
        boss.add_child(person)
      else:
        self.ceo = person