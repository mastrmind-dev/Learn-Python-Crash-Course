#Domain name replacer
email = "john@something.com"

def replaceNewDomain(email, oldDomain, newDomain):
	if(oldDomain in email):
		index = email.index(oldDomain)
		email = email[:index] + newDomain
		return email

oldDomain = "something"
newDomain = "someone.com"

rep = replaceNewDomain(email, oldDomain, newDomain)
print("New Email: " + rep)
