#Author: Ethan Lakhan epl5303@psu.edu 
def run():  
  name = input("Enter your course 1 letter grade: ")
  credit1 = input("Enter your course 1 credit: ")
  credit1 = float(credit1)
  print(f"Grade point for course 1: {getGradePoint(name)}")
  name2 = input("Enter your course 2 letter grade: ")
  credit2 = input("Enter your course 2 credit: ")
  credit2 = float(credit2)
  print(f"Grade point for course 2: {getGradePoint(name2)}")
  name3 = input("Enter your course 3 letter grade: ")
  credit3 = input("Enter your course 3 credit: ")
  credit3 = float(credit3)
  print(f"Grade point for course 3: {getGradePoint(name3)}")
  print("Your GPA is: " + str((getGradePoint(name)*credit1 + getGradePoint(name2)*credit2 + getGradePoint(name3)*credit3)/(credit1+credit2+credit3)))
  

def getGradePoint(name):
  if name  == "A":
    return 4.0
    name = float(name)

  elif name == "A-":
    return 3.67
    name = float(name)
    
  elif name == "B+":
    return 3.33
    name = float(name)
  elif name == "B":
    return 3.0
    name = float(name)
  elif name == "B-":
    return 2.67
    name = float(name)
  elif name == "C+":
    return 2.33
    name = float(name)
  elif name == "C":
    return 2.0
    name = float(name)
  elif name == "D":
    return 1.0
    name = float(name)
  else:
    return 0.0
    name = float(name)

def getGradePoint(name2):
  if name2  == "A":
    return 4.0
    name2 = float(name2)
  elif name2 == "A-":
    return 3.67
    name2 = float(name2)
  elif name2 == "B+":
    return 3.33
    name2 = float(name2)
  elif name2 == "B":
    return 3.0
    name2 = float(name2)
  elif name2 == "B-":
    return 2.67
    name2 = float(name2)
  elif name2 == "C+":
    return 2.33
    name2 = float(name2)
  elif name2 == "C":
    return 2.0
    name2 = float(name2)
  elif name2 == "D":
    return 1.0
    name2 = float(name2)
  else:
    return 0.0
    name2 = float(name2)

def getGradePoint(name3):
  if name3  == "A":
    return 4.0
    name3 = float(name3)
  elif name3 == "A-":
    return 3.67
    name3 = float(name3)
  elif name3 == "B+":
    return 3.33
    name3 = float(name3)
  elif name3 == "B":
    return 3.0
    name3 = float(name3)
  elif name3 == "B-":
    return 2.67
    name3 = float(name3)
  elif name3 == "C+":
    return 2.33
    name3 = float(name3)
  elif name3 == "C":
    return 2.0
    name3 = float(name3)
  elif name3 == "D":
    return 1.0
    name3 = float(name3)
  else:
    return 0.0
    name3 = float(name3)

if __name__ == "__main__":
  run()