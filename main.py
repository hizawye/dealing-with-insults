"""
=> Taking "text" as input
and filtering insults/bad words and the output
will be more respectful 
-like the F word >>f***-
Author : safou abderrahim
"""

from re import sub
from resourses.deliver import insults

insults = insults()

user_text = input("Enter the text:").lower()
def analys(text):
	count = 0
	for insult in insults :
		if insult in text :
			count += 1
			yield insult
	yield count
analys_ = list(analys(user_text))

def replace(text ,pattern):
	for patt in pattern :
		patt_rep = list(patt[0:1]) + ((len(patt) - 1) * '*')
		text = sub(patt ,patt_rep ,text)
		yield text
if analys_[-1] >= 1 :
	print(f"[!]there is {analys_[-1]} insult(s)")
else :
	print("[✓] Your text is clean asf")

#print(replace(user_text , analys_[0:-1]))
print(list(replace(user_text,analys_[:-1])))
