class student:
    def __init__(self, name, address, phone_number, hobby, years):
        self.name = name 
        self.address = address
        self.phone_number = phone_number
        self.hobby = hobby
        self.years = years

    def welcome_massage (self):
        return f"welcome {self.name}! your address is {self.address} and your phone number is {self.phone_number}. next, your hobby is {self.hobby} and your years is {self.years}"

student_name = input ("enter student's name: ")
student_address = input ("enter student's address: ")
student_phone = input ("enter student's phone number: ")
student_hobby = input ("enter student's hobby: ")
student_years = input ("enter student's years: ")


new_student = student (student_name, student_address, student_phone, student_hobby, student_years)



print (new_student.welcome_massage)




#name, address, aur phone
#hobby, name, aur years

























