import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
	w=w.lower()
	if w in data:
		return	data[w]
	elif len(get_close_matches(w,data.keys()))>0:
		for x in range(len(get_close_matches(w,data.keys()))):
			yn=input("Do you mean %s press y or n:" %get_close_matches(w,data.keys())[x])
			if yn.lower()=='y':
				return data[get_close_matches(w,data.keys())[x]]
			else:
				continue
	else:
		return "The word doesnt exist"
		
word=input("Enter the word: ")
output=translate(word)
if type(output)==list:
	i=1
	for item in output:
		print(i,":"+item)
		i+=1
else:
	print(output)