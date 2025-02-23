class Korean:
    def speak(self):
        print("speak in korean")

class Bangladesh:
    def speak(self):
        print("speak in bangali")

def translation(people):
    people.speak()

k = Korean()
b = Bangladesh()

translation(k)
translation(b)