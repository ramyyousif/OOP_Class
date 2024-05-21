### --- OOP Email Simulator training --- ###

# --- Email Class --- #
class email:
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    inbox.append(email('person1@hotmail.com', 'Subject 1', 'Content of email 1'))
    inbox.append(email('person2@hotmail.com', 'Subject 2', 'Content of email 2'))
    inbox.append(email('person3@hotmail.com', 'Subject 3', 'Content of email 3'))
    
def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for index, email in enumerate(inbox):
        print(f'{index+1} = {email.subject_line}')

def read_email(index):
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    email = inbox[index]
    print(f'\nEmail from {email.email_address}')
    print(f'Subject: {email.subject_line}')
    print(f'Content: {email.email_content}')
    email.mark_as_read()
    print(f'Email has been marked as read.')

# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Defining menu function.
def options():
    print('\nWould you like to:')
    print('\n1. Read an email.')
    print('2. View unread emails.')
    print('3. Quit application.')

# Fill in the logic for the various menu operations.
menu = True
print('\nWelcome user!')
options()
while True:
    try:
        user_choice = int(input('\nEnter selection: '))
        
        if user_choice == 1:
            # add logic here to read an email.
            while True:
                try:
                    list_emails()
                    index = int(input('\nEnter the number of the email you want to read: ')) - 1
                    if 0 <= index < len(inbox):
                        read_email(index)
                        options()
                        break
                    else:
                        print('\nInvalid email number. Please enter a valid email number.\n')
                except ValueError:
                    print('\nInvalid email number. Please enter a valid email number.\n')
                    
        elif user_choice == 2:
            # add logic here to view unread emails.
            unread_emails = [email for email in inbox if not email.has_been_read]
            if unread_emails:
                print('\nUnread Emails:')
                for email in unread_emails:
                    print(f'- {email.subject_line}')
                options()
            else:
                print('\nNo unread emails.')
                options()
                
        elif user_choice == 3:
            # add logic here to quit application.
            print('\nLeaving e-mail application. Thank you and have a great day!\n')
            break
        
        else:
            print('\nOops - incorrect input, please input a correct option. (1, 2 or 3).')
            options()
    except ValueError:
        print('\nOops - incorrect input, please input a correct option. (1, 2 or 3).')
        options()
