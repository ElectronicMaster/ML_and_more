import re
import os

os.system('cls')

replies = ["","",""]

orderNumber = r'#\s?(\d{8})'
pnPattern = r'\d{10}|\(\d{3}\)-?\s?\d{4}-?\s?\d{3}'
emailPattern = r'\w+\@\w+.\w{2,}'
patterns = [orderNumber,pnPattern,emailPattern]

def query(replies):
    querys = ["order no,", "phone no,", "email ID"]
    reqQuery = ""
    reqQueryArr = []
    j=0
    while(j<3):
        if(not replies[j]):
            reqQuery += " " + querys[j]
            reqQueryArr.append(querys[j])
        j+=1
    return [reqQuery,reqQueryArr]

reqFields= []

while(True):
    if(reqFields):
        print("=======================================================")
        for reqField in reqFields:
            if(reqField == "order no,"):
                print("* missing : please enter your order number which will be #(8digits)")
            if(reqField == "phone no,"):
                print("* missing : please enter your 10 digit phone number")
            if(reqField == "email ID"):
                print("* missing : please enter your full email ID (example: xyz@abc.pqr)")
        print("=======================================================")
    reqFields = []
    question = "please enter the following"
    question += query(replies)[0]
    print(question + "?")
    reply = input()
    if re.search(patterns[0],reply):
        replies[0] = (re.search(patterns[0],reply)).group()
    if re.search(patterns[1],reply):
        replies[1] = (re.search(patterns[1],reply)).group()
    if re.search(patterns[2],reply):
        replies[2] = (re.search(patterns[2],reply)).group()
    reqFields = query(replies)[1]
    if(reqFields):
        os.system('cls')
        continue
    else:
        break

os.system('cls')
print("\n========================================")
print("Thank you for providing your information")
fields = ["order no", "phone no", "email ID"]
i=0
for field in fields:
    print(f"Your {field} is : {replies[i]}")
    i+=1
print("========================================")