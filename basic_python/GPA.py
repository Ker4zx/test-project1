def point_gpa(name):
    point_midterm = int(input("Enter Point : "))
    pointfinal = int(input("Enter point : "))
    if point_midterm >= 20:
       print("exllent!!")
    elif point_midterm < 20:
       print("Fiall to Grad F")
    if pointfinal < 30:
       print('Fiall to grad A')
    elif pointfinal:
       print('Dreem to grad A')
    else:
       print("End to program !!")
    return name 
print(point_gpa('Kaiwit Thummee'))