#[{id:1, "name":"rajesh"}, {id:2 , "name":"rahul"} , {id:3 , "name":"Sruthi"}]
#Write a program to accept a number and print the name of the student with that id
student_withid = [{"id":1, "name":"rajesh"}, {"id":2 , "name":"rahul"} , {"id":3 , "name":"Sruthi"}]

user_id = int(input("enter an id "))
for s in student_withid:
    if user_id == s["id"]:
        print("student id:" ,s["id"] ,"student name:",s["name"])
        break
else:
        print("No student with that id")