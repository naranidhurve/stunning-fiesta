
import json,os
def my():
    user=(input("enter login or signup :  "))
    if user=="signup":
        u_name=input("enter the user_name :  ")
        password=input("enter the password :  ")
        p=len(password)
        numbers = "0123456789"
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_chr = "!@#$%^&*()-+"
        n,l,u,s=0,0,0,0
        i=0
        while i<len(password):
            if password[i] in numbers:
                n=n+1
            if password[i] in lower_case:
                l=l+1
            if password[i] in upper_case:
                u=u+1
            if password[i] in special_chr:
                s=s+1
            i=i+1
        if p>=6:
            if n>=1 and l>=1 and u>=1 and s>=1 :
                print("your  password")

        else:
            print("no")
        password1=((input("repassword1 the password :  ")))
        if password==password1 :
                print("your password is match")
                if(os.path.isfile('Signup.json')):
                    op=open("Signup.json","r")
                    a=json.load(op)
                    for i in a["user"]:
                        if i["username"]==u_name:
                            print("Already Exists")
                            dic={}
                            d={}
                            dic["username"]=u_name
                            dic["password"]=password1
                            d["Description"]=input("enter description : ")
                            d["D.O.B"]=input("enter D.O.B : ")
                            d["Gender"]=input("enter your gender : ")
                            d["Hobbies"]=input("enter your hobbies : ")
                            dic["Profile"]=d
                            v=a["user"]
                            v.append(dic)
                            f=open("Signup.json","w+")
                            json.dump(a,f,indent=4)  
                            f.close()
                            print("Signup Succesfully")
                            break  
                        else:

                                dic={}
                                l=[]
                                d={}
                                d1={}
                                dic["username"]=u_name
                                dic["password"]=password1
                                d["description"]=input("enter the description : ")
                                d["D.O.B"]=input("enter your D.O.B : ")
                                d["Gender"]=input("enter your gender : ")
                                d["Hobbies"]=input("enter your hobbies : ")
                                dic["Profile"]=d
                                l.append(dic)
                                d1["user"]=l
                                file=open("Signup.json","w+")
                                json.dump(d1,file ,indent=4)
                                file.close()
                                print("Signup Succesfully")
                else:

                    a={}
                    b=[]
                    c={}
                    d={}
                    a["username"]=u_name
                    a["password"]=password1
                    c["description"]=input("enter the description : ")
                    c["D.O.B"]=input("enter your D.O.B : ")
                    c["Gender"]=input("enter your gender : ")
                    c["Hobbies"]=input("enter your hobbies : ")
                    a["Profile"]=c
                    b.append(a)
                    d["user"]=b
                    file=open("Signup.json","w+")
                    json.dump(d,file ,indent=4)
                    file.close()
my()