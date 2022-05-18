class Candidate:
    def __init__(self, id, name, picture, position, gender, age, skills):
        self.id = id
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills

    def get_skills_list(self):
        return self.skills.lower().split(', ')
