import time , os

raw_time = []
get_raw_time = time.asctime()
for t in get_raw_time:
	raw_time.append(t)
	
h = raw_time[11]+raw_time[12]
m = raw_time[14]+raw_time[15]
s = raw_time[17]+raw_time[18]
ap_h = raw_time[11]+raw_time[12]

if h > "12":
	if h == "13":
		h = 1
	elif h == "14":
		h = 2
	elif h == "15":
		h = 3
	elif h == "16":
		h = 4
	elif h == "17":
		h = 5
	elif h == "18":
		h = 6
	elif h == "19":
		h = 7
	elif h == "20":
		h = 8
	elif h == "21":
		h = 9
	elif h == "22":
		h = 10
	elif h == "23":
		h = 11
	elif h == "00":
		h = 12	
else:
	h = h

os.system("clear")
print ("        "+"—"*25)
print ("       |   ⏱️ Simple Clock ⏱️    |")
print ("        "+"—"*25)
print ()
raw_day = raw_time[0]+raw_time[1]+raw_time[2]
month = raw_time[4]+raw_time[5]+raw_time[6]
date = raw_time[8]+raw_time[9]
year = raw_time[20]+raw_time[21]+raw_time[22]+raw_time[23]

day = ""
if raw_day == "Sat":
	day = "Saturday"
elif raw_day == "Sun":
	day = "Sunday"
elif raw_day == "Mon":
	day = "Monday"
elif raw_day == "Thu":
	day = "Thursday"
elif raw_day == "Tue":
	day = "Tuesday"
elif raw_day == "Wed":
	day = "Wednesday"
elif raw_day == "Fri":
	day = "Friday"
	
print ("Today: "+day+", "+date+"-"+month+"-"+year)

hh = int(ap_h)
ap = ""
if hh >= int(12):
	ap = " PM"
else:
	ap = " AM"

def show():
	global s
	global m
	global h
	global ap
	s = str(s)
	m = str (m)
	h = str(h)
	
	if len(h)==1 and len(m)==1 and len(s)==1:
		print ("Time : "+"0"+str(h)+":0"+str(m)+":0"+str(s)+ap,end="\r")
		
	elif len(h)==1 and len(m)==1 and len(s)==2:
			print ("Time : "+"0"+str(h)+":0"+str(m)+":"+str(s)+ap,end="\r")
			
	elif len(h)==1 and len(m)==2 and len(s)==1:
			print ("Time : "+"0"+str(h)+":"+str(m)+":0"+str(s)+ap,end="\r")
			
	elif len(h)==1 and len(m)==2 and len(s)==2:
		print ("Time : "+"0"+str(h)+":"+str(m)+":"+str(s)+ap,end="\r")
		
		##
		
	elif len(h)==2 and len(m)==1 and len(s)==1:
		print ("Time : "+str(h)+":0"+str(m)+":0"+str(s)+ap,end="\r")	
		
	elif len(h)==2 and len(m)==1 and len(s)==2:
		print ("Time : "+str(h)+":0"+str(m)+":"+str(s)+ap,end="\r")
		
	elif len(h)==2 and len(m)==2 and len(s)==1:
		print ("Time : "+str(h)+":"+str(m)+":0"+str(s)+ap,end="\r")
		
	elif len(h)==2 and len(m)==2 and len(s)==2:
		print ("Time : "+str(h)+":"+str(m)+":"+str(s)+ap,end="\r")
	
def add():
	global s
	global m
	global h
	
	s = int(s)
	m = int (m)
	h = int(h)
	s+=1
	if s==60:
		m+=1
		s=0
	if m==60:
		h+=1
		m=0
	if h==24:
		h=0
while True:
	time.sleep(1)
	add()
	show()