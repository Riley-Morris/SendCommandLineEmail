import smtplib
#create smtp instance for office 365
conn = smtplib.SMTP('smtp.office365.com', 587)
#start connection to server
conn.ehlo()
#start encryption on connection
conn.starttls()
#while loop to allow user to attempt another login if failed for some reason
while True:
    try:
        username = input('Please type your full email address and click Enter\n> ')
        password = input('Please type your password and click Enter\n> ')
        #try to login with credentials
        status = conn.login(username, password)
        #break out of loop with success
        break
    except:
            print('Login failed, try again...\n\n')
            pass
print('login successful\n\n')
subject = input('What is the Subect line of your email?\n\n> ')
Body = input('What is the main body of the email?\n\n>')
#while loop incase of error
while True:
    try:
        choice = int(input('How many people to send this email to?\n> '))
        #loop over recipients and send email to each
        for i in range(1, choice+1):
            recipient = (input(f'Who is recipient #{i}?\n> '))
            #send the email
            conn.sendmail(username, recipient, f'Subject:{subject}\n\n {Body}')
            break
    except:
        print('Please try again, something went wrong\n')
#quit the connection
conn.quit()
