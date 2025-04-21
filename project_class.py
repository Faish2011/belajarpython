class student:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def welcome_massage (self): 
        return f"welcome {self.name}! your address is {self.address} and your phone number is {self.phone_number}"

student_name = input ("enter student's name: ")
student_address = input ("enter student's address: ")
student_phone = input ("enter student's phone number: ")

new_student = student (student_name, student_address, student_phone)

print (new_student.welcome_massage ())




























