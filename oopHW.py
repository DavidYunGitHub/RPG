# Assignment 1
class Person: 

    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        friends_list = []

    def greet(self, other_person): 

        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print(self.name, self.email, self.phone)
        



sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.name, sonny.email, sonny.phone)
print(jordan.name, jordan.email, jordan.phone)

sonny.print_contact_info()
jordan.print_contact_info()

jordan.Person.friends_list.append(sonny) 
len(jordan.Person.friends)




# Assignment 2
# class vehicle:

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         print(self.make, self.model, self.year)

# car = vehicle("toyota", "tacoma", "1900")
print(car.make, car.model, car.year)
# car.print_info()





