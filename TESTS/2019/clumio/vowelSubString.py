test_string = 'aeiougaeiouoiea'

def vowelSubString(string):
	l = []
	s = []
	for letter in string:
		if letter in ['a','e','i','o','u']:
			s.append(letter)
		else:
			l.append(s)
			s=[]
	l.append(s)
	return l

def validSubStringCount(str):
	#print(str)
	n = len(str)
	if n < 5:
		return 0
	d={'a':0,'e':0,'i':0,'o':0,'u':0}
	for i in str:
		d[i]+=1
	if d['a'] and d['e'] and d['i'] and d['o'] and d['u']:
		pass
	else:
		return 0
	l_ind=0
	r_ind=n-1

	while d[str[r_ind]]>1:
		#print(d,r_ind)
		d[str[r_ind]]-=1
		r_ind-=1
	#print("here",d,r_ind)
	while d[str[l_ind]]>1:
		#print(d,l_ind)
		d[str[l_ind]]-=1
		l_ind+=1
	#print("there",d,l_ind)
	#print(r_ind,l_ind)
	return n-r_ind+l_ind+validSubStringCount(str[:r_ind])+validSubStringCount(str[l_ind+1:])

listOfVowelSubString = vowelSubString(test_string)
ans = 0
for vowelSubString in listOfVowelSubString:
	ans+=validSubStringCount(list(vowelSubString))
print(ans)
