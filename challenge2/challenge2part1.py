#Chuck Robbins wants to give a raise to everyone whose first name starts the letter c (upper or lower case), how many employees will get a raise?


all_employees = [
        'JOHNSON WILLIAMS','BROWN JONES','GARçIæ MILLER','DAVIS RODRIGUEZ','MARTINEZ HERNANDEZ','LOPEZ GONZALEZ',
        'WILSON ANDERSON','THOMAS TAYLOR','MÖÖRE JACKSON','MARTIN LEE','PEREZ THOMPSON','WHITE HARRIß',
        'SANCHEZ CLARK','RAMIREZ LEWIS','ROBINSON WALKER','YÖUNG ALLEN','KING WRIGHT','SCOTT TORRES',
        'NGUYEN HILL','FLORES GREEN','ADAMS NELSON','BAKER HALL','RIVERA CAMPBELL','MITCHELL CARTER',
        'ROBERTS GOMEZ','PHILLIPẞ EVANS','TURNER DIAZ','PARKER CRUZ','EDWARDS COLLINS','REYES STEWART',
        'MORRIS MORALES','MURPHY COOK','ROGERS GUTIERREZ','ORTIZ MORGAN','COOPER PETERSON',
        'BAILEY REED','HANẞ HOWARD','RAMOS KIM','CÖX WARD','RICHARDSON WATSON','BROOKS CHAVEZ',
        'WOOD JAMES','BENNETT GRAY','MENDOZA RUIZ','HUGHES PRICE','ALVAREZ çASTILLO'
    ]

def get_all_employees_input(message):
    """ Ignore this function you don't need to understand or change it """
    if "testInput" in message:
        testInputString = message.split("testInput")[1].rstrip().lstrip()
        allEmployeesTestingInput = testInputString.split(",")
        return allEmployeesTestingInput
    return all_employees

# Functions that your team will implement
def problem2_1(message):
    all_employees = get_all_employees_input(message)
    beginsWithLetterCCount = 0

    for x in all_employees:
        if x[0] == 'c' or x[0] == 'C':
            beginsWithLetterCCount +=1

    return str(beginsWithLetterCCount)

#There’s been a glitch in the ancient payroll system, and some people can’t get paid. 
#It's been discovered that people with last names which are longer than 8 characters are affected.
#How many people does this include?

def problem2_2(message):
    all_employees = get_all_employees_input(message)
    peopleWithLongerThan8CharacterLastnamesCount = 0

    for name in all_employees:
            if len(name.split()[1]) > 8:
                peopleWithLongerThan8CharacterLastnamesCount += 1
    return str(peopleWithLongerThan8CharacterLastnamesCount)



#Chuck is feeling generous wants to give his German, Danish and Turkish employees a raise. 
#How many employees have any of the following characters in their name: ẞ, ö, æ, or ç

# Assuming 'name' here refers to the full name and not (name, surname) as challenge 1.4 reffered to 'first name'
def problem2_3(message):
    all_employees = get_all_employees_input(message)
    employeesWhoWillGetBonusesCount = 0
    specialChars = ['ẞ', 'ö', 'æ', 'ç'] #we are taking only these specific chars, not upper case 

# s.find('$')
    for name in all_employees:
        statement = (name.find('æ') > 0 or name.find('ẞ') > 0 or name.find('ö') > 0 or name.find('ç') > 0)
        if(statement):
            employeesWhoWillGetBonusesCount += 1

    return str(employeesWhoWillGetBonusesCount)
