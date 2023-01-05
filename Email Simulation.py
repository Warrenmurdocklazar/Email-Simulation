#lists needed for code to work
inbox = []

#class email with 4 vairables
class Email:
    def __init__(self, has_been_read, email_contents, is_spam, from_address):
        self.has_been_read = has_been_read
        self.email_contents = email_contents
        self.is_spam = is_spam
        self.from_address = from_address

    def __str__(self):
     return f"{self.has_been_read, self.email_contents, self.is_spam, self.from_address}"

    # mark as read function
    def mark_as_read(self):
        self.has_been_read = True
        return

    # mark as spam function
    def mark_as_spam(self):
        self.is_spam = True
        return



Email_1 = Email(False,"Potato", False, "123@gmail.com")
inbox.append(Email_1)

Email_2 = Email(False,"ketchup", True, "123@gmail.com")
inbox.append(Email_2)

Email_3 = Email(False,"milk", False, "123@gmail.com")
inbox.append(Email_3)

Email_4 = Email(False,"car", False, "123@gmail.com")
inbox.append(Email_4)

Email_5 = Email(False,"Potato", False, "123@gmail.com")
inbox.append(Email_5)


# add email function using Email class
def add_email(email_contents, from_address):
    new_email = Email(False, email_contents, False, from_address)
    inbox.append(new_email)

    return new_email


#get count function
def get_count():
    print(len(inbox))
    return


#get email function
def get_email():
    x = len(inbox)
    option = int(input(f"There are {x} in total, which one do you want to read?"))
    option1 = option - 1
    print(inbox[option1].email_contents)
    print(f"Email is from,{inbox[option1].from_address}")
    inbox[option1].mark_as_read()
    print("Email has now been read")
    return


#get_unread_emails function
def get_unread_emails():
    x = -1
    for i in inbox:
        x += 1
        if inbox[x].has_been_read == False:
            print(f"Email {x} {inbox[x]}")
    read = int(input("Type which number email you want to mark as read"))
    inbox[read].mark_as_read()
    print(f"Email {read} has now been marked as read")
    return


#get_spam emails function using classes
def get_spam_emails():
    x = -1
    for i in inbox:
        x +=1
        if inbox[x].is_spam == True:
            print(f"Email {x} {inbox[x].email_contents}")
    return

#delte email function
def delete():
    x = len(inbox)
    for i in range(x):
        print(f"Email {i} reads {inbox[i]}")
    option = int(input("Which email would you like to delete enter a number?"))
    inbox.pop(option)
    print("Email deleted")


user_choice = ""
user_choice_1 = ""


while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/delete/quit?")

#using class function to read emails and mark them as read
    if user_choice == "read":
      user_choice_1= input("Enter 'specific' to read a specific email or 'unread' to view unread emails: ")
      if user_choice_1 == "unread":
        get_unread_emails()
      if user_choice_1 == "specific":
        get_email()

#using class function to read emails and mark them as spam
    elif user_choice == "mark spam":
        x = len(inbox)
        for i in range(x):
            print(f"Email {i} reads {inbox[i]}")
        spam_choice = int(input("Type which number email you want to mark as spam"))
        inbox[spam_choice].mark_as_spam()
        print("Here are all emails marked as spam")
        get_spam_emails()

#logic to allow user to send emails(add emails)
    elif user_choice == "send":
        email_address = input("Enter email address: ")
        email_content = input("Write your content: ")
        add_email(email_content,email_address)


#logic to allow user to delete emails in inbox
    elif user_choice == "delete":
        delete()

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")


