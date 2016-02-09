# CheckPing
Script performs ping to a device and send an email if the device does not respond.
To send email use external SMTP.

file: checkping.py, sendmail.py

>Instruction:

Install mail server Postfix

>Ubuntu 15.10:

    sudo apt-get update
    sudo apt-get insall postfix

>Fedora 23:

    sudo dnf install postfix

>Configuration postfix to use a external SMTP:

    sudo vim /etc/postfix/main.cf

    insert in main.cf:
    myhostname = name.example.com
 
>Configuring username and password:

  Open or create the /etc/postfix/sasl_passwd 

     add your destination in sasl_passwd: 
      [mail.isp.example] username:password
   
       if you want to specify a non default port, insert: [mail.isp.example]:587 username:password

Create the hash db file for Postfix
   sudo postmap /etc/postfix/sasl_passwd
   
You should have a new file named sasl_passwd.db in the /etc/postfix/

>Configuring the Relay Server:

    sudo vim /etc/postfix/main.cf
    
    # specify SMTP relay host 
    relayhost = [mail.isp.example]:587
    
At the end of the file, add the following parameters to enable authentication:

    sudo vim /etc/postfix/main.cf
    
    # enable SASL authentication 
    smtp_sasl_auth_enable = yes
    # disallow methods that allow anonymous authentication. 
    smtp_sasl_security_options = noanonymous
    # where to find sasl_passwd
    smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
    # Enable STARTTLS encryption 
    smtp_use_tls = yes
    # where to find CA certificates Debian or RedHat based
    smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt  # this in Debian based
    smtp_tls_CAfile = /etc/pki/tls/certs/ca-bundle.crt # this in RadHat based
    
>Restart Postfix:

    sudo service postfix restart
    
>Configuration for provider example:

For google apps:

    sudo vim /etc/postfix/sasl_passwd
    
    insert:
    
    [smtp.gmail.com]:587 <USERNAME@gmail.com>:PASSWORD
    
For your domain:
  
    sudo vim /etc/postfix/sasl_passwd
    
    insert:
    
    [smtp.gmail.com]:587 <USERNAME@yourdomain.com>:PASSWORD
    
Use Relay host:
    
    sudo vim /etc/postfix/main.cf
    
    relayhost = [smtp.gmail.com]:587

