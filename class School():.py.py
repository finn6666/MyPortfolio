class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  def getname(self):
    return self.name

  def getlevel(self):
    return self.level

  def getnumberOfStudents(self):
    return self.numberOfStudents

  def setnumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
      return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."

class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
      super().__init__(name, "primary", numberOfStudents)
      self.pickupPolicy = pickupPolicy


    def getPickupPolicy(self):
      return self.pickupPolicy

    def __repr__(self):
      parentRepr = super().__repr__()
      return parentRepr + f" The pickup policy is: {self.pickupPolicy}"

class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
      super().__init__(name, "high", numberOfStudents)
      self.sportsTeams = sportsTeams

    def getsportsTeams(self):
      return self.sportsTeams
      parentRepr = super().__repr__()

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + f" The sports teams are: {', '.join(self.sportsTeams)}."

# Example usage:
primary = PrimarySchool("Greenwood", 300, "No pickup after 5 PM")
print(primary)

high_school = HighSchool("Riverdale", 500, ["Football", "Basketball", "Baseball"])
print(high_school)
