# import json
# print("wel come login  and signup page")
# usr=input("what u want to do login or sign up :-")
# if usr=="signup":
#     usr_name=input("enter the usr_name:-")
#     password=input("enter usr password:-")
#     password1=input("comform password")
#     if password==password1:
#         description=input("enter your qualification:-")
#         dob=input("enter ur dob:-")
#         hobbies=input("enter ur hobbies:-")
#         gender=input("enter ur gender f/m:-")
#         usr_details={"description":description,"DOB":dob,"hobbies":hobbies,"gender":gender}
#         with open("p.json","w")as f:
#             data=json.dump(usr_details,f,indent=4)

#     else:
#         print("not strong password")
# else:
#     if usr=="login":
#         usr_name=input("enter the usr_name:-")
#         password=input("enter usr password:-")
#         password1=input("conform password")
#         with open("p.json","r")as file:
#             d=json.load(file)
#             if password==d["password1"]:
#                 print("login successfully")
#                 print(d)
#             else:
#                 ("wrong details")




import json
print(("welcome to login signup"))
user=input("you wants to login or signup:")
if user=="signup":
    user1=input("enter user name")
    pass1=input("enter password")
    pass2=input("enter your confirm password")
    if pass1==pass2:
        print("your password is confirmed")
        birth=input("enter birthdate")
        gender=input("enter the gender")
        hobbies=input("enter your hobbies")
        dict={"user":user,"pass2":pass2,"birth":birth,"gender":gender,"hobbies":hobbies}
        with open("text.json","w")as f:
            b=json.dump(dict,f,indent=4)
    else:
        print("wrong password")
else:
    if user=="login":
        user1=input("enter user name")
        pass1=input("enter password")
        with open("text.json","r")as f:
            b=json.load(f)
            if pass1==b["pass2"]:
                print("login succesfully")
                print(b)
    else:
        print("wrong details")
