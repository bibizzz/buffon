# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import smtplib
fromMy = 'ecolebuffon@yahoo.com' # fun-fact: from is a keyword in python, you can't use it as variable, did abyone check if this code even works?
#to  = 'maingaul@yahoo.fr'
to =  ['sympa@framalistes.org',  'maingaul@yahoo.fr']
#to =  ['maingaul@yahoo.fr',  'bibizzzmaing@gmail.com']


#to  = 'bibizzzmaing@gmail.com'
subj='INVITE parents-buffon bibizzzmaing@gmail.com'
message_text= ''

msg = "From: %s\nTo: %s\nSubject: %s\n \n%s" % ( fromMy, to, subj, message_text )

username = str('ecolebuffon@yahoo.com')  
password = str('fcpe@ab89')  
host = str("smtp.mail.yahoo.com")

try :
    server = smtplib.SMTP("smtp.mail.yahoo.com",587)
    server.set_debuglevel(False)
    server.starttls()
    server.login(username,password)
    server.sendmail(fromMy, to, msg)
    server.quit()    
    print 'ok the email has sent '
except :
    print 'can\'t send the Email'