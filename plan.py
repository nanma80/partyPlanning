class Plan:
  def __init__(self, person, is_attending):
    self.person = person
    self.subplans = []
    self.score = 0
    self.is_attending = is_attending
    if is_attending:
      self.score += person.score

  def merge(self, plan):
    self.subplans.append(plan)
    self.score += plan.score

  def is_better_than(self, plan):
    return self.score > plan.score

  def list_names(self, list_so_far = None):
    if list_so_far == None:
      list_so_far = []
    
    if self.is_attending:
      list_so_far.append(self.person.name)

    for subplan in self.subplans:
      subplan.list_names(list_so_far)
    return list_so_far
    