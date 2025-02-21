class Software_Engineer:
    def __init__(self,exp_level):
        self.exp = exp_level
    
    def cal_salary(self):
        base_salary = 100000
        actual_salary = 100000 * self.exp
        print(actual_salary)


class Intern(Software_Engineer):
    pass


class Junior(Software_Engineer):
    pass
        
class Mid_level(Software_Engineer):
    pass


class Senior(Software_Engineer):
    pass

        
intern_obj = Intern(1)
mid_level_obj = Mid_level(2)
junior_obj = Junior(3)
senior_obj = Senior(4)

intern_obj.cal_salary()
mid_level_obj.cal_salary()
junior_obj.cal_salary()
senior_obj.cal_salary()