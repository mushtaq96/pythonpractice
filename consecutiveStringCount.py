dictionary={}

def find_consecutive(samplestring):    
    i=0
    while i < len(samplestring)-1:
        count=0
        if(samplestring[i] == samplestring[i+1]):
            dictionary[i] = count+1
            
        else:
            dictionary[i] = count
            
        i+=1
    return dictionary

samplestring = 'Iaamgeek?'
final = find_consecutive(samplestring)
print(samplestring)
print(final)

total=0
for key in dictionary:
    if(dictionary[key]==1):
        total+=1
print("number of consecutive characters are:",total)

