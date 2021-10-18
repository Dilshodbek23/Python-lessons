class Person:
    """Information about person"""
    def __init__(self,name,surname,passport,y_of_birth):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.y_of_birth = y_of_birth
    
    def get_info(self):
        """Information about person"""
        info = f"{self.name} {self.surname}. "
        info += f"Passport:{self.passport}, {self.y_of_birth}-yilda tug`ilgan"
        return info
            
    def get_age(self,yil):
        """Personning age-reversing method"""
        return yil - self.y_of_birth
    
class Adress:
    """Adress saqlash uchun klass"""
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
        """Person haqida ma'lumot"""
        info = f"{self.name} {self.surname}. "
        info += f"Passport:{self.passport}, {self.y_of_birth}-was born"
        return info
    
class Student(Person):
    """student klassi"""
    def __init__(self,name,surname,passport,y_of_birth,idnumber,Adress):
        """studentning xususiyatlari"""
        super().__init__(name, surname, passport, y_of_birth)
        self.idnumber = idnumber
        self.bosqich = 1
        self.Adress = Adress
        self.Subjectlar = []
        self.Subjectlar_soni = 0
    
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

        
    def remove_Subject(self,subject):
        if subject in self.Subjects:
            self.subjects.remove(Subject)
            self.subjects_number -= 1
        else:
            return "You are not subscribed to this Subject"
    
class Subject:
    def __init__(self,subject_name):
        self.subject_name = subject_name
    
subject1 = Subject("Mathematics")
subject2 = Subject("Physics")
subject3 = Subject("Informatics")
student_Adress = Adress(12,'Olmazor',"Bog'bon","Samarqand")
student1 = Student("Valijon","Aliyev","FA112299",2000,"0000012",student_Adress)
