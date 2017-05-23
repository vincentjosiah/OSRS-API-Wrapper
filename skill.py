import const

class Skill(object):
	def __init__(self, name, rank = 0, level = 0, xp = 0):
		if name not in const.SKILLS_SET:
			raise Exception("%s is not a valid skill." % name)

		self.name = name
		self.rank = rank
		self.level = level
		self.xp = xp

	def __str__(self):
		return "%s-%s-%s-%s" % (str(self.name), str(self.rank), str(self.level), str(self.xp))