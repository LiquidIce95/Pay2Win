import  os
#USE .bashrc
#export VAR="whatever"
#USE COMMAND : source .bashrc
#in /home/Dave/

EmailAddress = os.environ.get("GMAIL")
Pass = os.environ.get('GmailPass')

print(os.environ)
print(os.environ.get('GMAIL'))
print(Pass)

