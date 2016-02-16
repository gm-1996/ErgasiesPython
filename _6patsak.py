import urllib
import json

date = raw_input("Dose imerominia tis morfis dd-MM-yyyy\n")

url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json"%(date)

response = urllib.urlopen(url)
data = json.loads(response.read())
#arithmos klirosewn gia ta opoia exoume dedomena
length = len(data['draws']['draw'])
#paragogh listas 80 thesewn , osoi kai oi arithmoi sto kino 
#arxika kathe thesi pou antiprosopeuei kathe arithmo exei timh 0
nums =[]
for i in range(80):
    nums.append(0)

#gia kathe seira apotelesmatwn stin antistoixh thesi tou pinaka 
#prostithetai 1
for i in range(length):
    for j in range(20):
        nums[data['draws']['draw'][i]['results'][j]-1]+=1
#ektiposi apotelesmatwn
for i in range(80):
    print i+1 ," : ",nums[i]
print "kliroseis :",length

