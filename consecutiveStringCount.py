def find_consecutive(samplestring):
    dictionary={}
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
