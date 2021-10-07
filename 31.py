from uuid import uuid4

class Person:
    """Information about person"""
    __num_person = 0
    def __init__(self,name,surname,passport,y_of_birth,phone):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.y_of_birth = y_of_birth
        self.__phone = phone
    
    def get_info(self):
        """Information about person"""
        info = f"{self.name} {self.surname}. "
        info += f"Passport:{self.passport}, {self.y_of_birth}-yilda tug`ilgan"
        return info
            
    def get_age(self,yil):
        """Age determination method"""
        return yil - self.y_of_birth
    
    @classmethod
    def get_num_person(cls):
        return cls.__num_person
    
class Adress:
    """Class for address"""
    def __init__(self,home,street,district,region):
        """Adress properties"""
        self.home = home
        self.street = street
        self.district = district
        self.region = region
    
    def get_Adress(self):
        """see Adress"""
        Adress = f"{self.region} regioni, {self.district} districti, "
        Adress += f"{self.street} street, {self.home}-home"
        return Adress
    
class Professors(Person):
    def __init__(self,name,surname,passport,y_of_birth,idnumber):
        super().__init__(name, surname, passport, y_of_birth)
        self.idnumber = idnumber
        self.publications = []
        self.publication_numbers = 0
        
    def get_info(self):
        """Information about the person"""
        info = f"{self.name} {self.surname}. "
        info += f"Passport:{self.passport}, {self.y_of_birth}-was born"
        return info
    
class Student(Person):
    """Student class"""
    __num_student = 0
    def __init__(self,name,surname,passport,y_of_birth,idnumber,Adress):
        """Student characteristics"""
        super().__init__(name, surname, passport, y_of_birth)
        self.idnumber = idnumber
        self.bosqich = 1
        self.Adress = Adress
        self.Subjectlar = []
        self.Subjectlar_soni = 0
        self.__id = uuid4()
    
    def get_id(self):
        """student ID number"""
        return self.idnumber
    
    def get_bosqich(self):
        """the student’s learning phase"""
        return self.bosqich
    
    def get_info(self):
        """student information"""
        info = f"{self.name} {self.surname}. "
        info += f"{self.get_bosqich()}-bosqich. ID number: {self.idnumber}."
        return info
    
    def registration(self,Subject):
        self.subjects.append(Subject)
        self.subjects_number += 1
        
    def remove_Subject(self,subject):
        if subject in self.Subjects:
            self.subjects.remove(Subject)
            self.subjects_number -= 1
        else:
            return "You are not subscribed to this Subject"
        
    @classmethod
    def get_num_stodent(cls):
        return cls.__num_student
    
class Subject:
    def __init__(self,subject_name):
        self.subject_name = subject_name
    
subject1 = Subject("Mathematics")
subject2 = Subject("Physics")
subject3 = Subject("Informatics")
student_Adress = Adress(12,'Olmazor',"Bog'bon","Samarqand")
student1 = Student("Valijon","Aliyev","FA112299",2000,"0000012",student_Adress)
student1.registration(subject1)
student1.registration(subject3)
