
class Person:
      def  set_details(self, name, age):
            self.name = name
            self.age = age

      def display(self):
            print('I am ', self.name)

      def greet(self):
            if self.age < 80:
                  print('Hi, How are you doing ?')
            else:
                  print('Hello, How do you do ?')
            self.display()
      
p1 = Person()
p1.set_details('Bob', 20)
p1.greet()

p2 = Person()
p2.set_details('Ted', 90)
p2.greet()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
