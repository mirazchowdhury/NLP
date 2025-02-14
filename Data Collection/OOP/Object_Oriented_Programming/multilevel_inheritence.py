# Base class
class SoftwareDeveloper:
    def __init__(self, name, emp_id, experience_level):
        self.name = name
        self.emp_id = emp_id
        self.experience_level = experience_level

    def display_info(self):
        print(f"Developer Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Experience Level: {self.experience_level}")

    def calculate_salary(self):
        if self.experience_level == "Intern":
            return 20000  # Base salary for interns
        elif self.experience_level == "Junior Developer":
            return 50000  # Base salary for junior developers
        elif self.experience_level == "Senior Developer":
            return 80000  # Base salary for senior developers
        elif self.experience_level == "Team Leader":
            return 120000  # Base salary for team leaders
        else:
            return 0  # Default salary if experience level is unknown or invalid

# Subclass inheriting from SoftwareDeveloper
class Intern(SoftwareDeveloper):
    pass  # Inherits all attributes and methods from SoftwareDeveloper

# Subclass inheriting from SoftwareDeveloper
class JuniorDeveloper(SoftwareDeveloper):
    pass  # Inherits all attributes and methods from SoftwareDeveloper

# Subclass inheriting from JuniorDeveloper
class SeniorDeveloper(JuniorDeveloper):
    pass  # Inherits all attributes and methods from JuniorDeveloper

# Subclass inheriting from SeniorDeveloper
class TeamLeader(SeniorDeveloper):
    pass  # Inherits all attributes and methods from SeniorDeveloper
