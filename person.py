from plan import Plan

class Person:
  def __init__(self, name, boss_name, score):
    self.name = name
    self.score = score
    self.boss_name = boss_name
    self.children = []
    self.attending_plan_cache = None
    self.not_attending_plan_cache = None

  def add_child(self, child):
    self.children.append(child)

  def attending_plan(self):
    if not self.attending_plan_cache:
      self.attending_plan_cache = Plan(self, True)
      for child in self.children:
        self.attending_plan_cache.merge(child.not_attending_plan())
    return self.attending_plan_cache

  def not_attending_plan(self):
    if not self.not_attending_plan_cache:
      self.not_attending_plan_cache = Plan(self, False)
      for child in self.children:
        self.not_attending_plan_cache.merge(child.best_plan())
    return self.not_attending_plan_cache

  def best_plan(self):
    if self.attending_plan().is_better_than(self.not_attending_plan()):
      return self.attending_plan()
    else:
      return self.not_attending_plan()
