#!/Users/ten/local/venv3/bin/python
import requests
import random
import re
from functools import reduce

s = requests.Session()

male_names_url = 'https://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/nlp/corpora/names/male.txt'
female_names_url = 'https://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/nlp/corpora/names/female.txt'

male_names_text = s.get(male_names_url)
female_names_text = s.get(female_names_url)

def F(names_list, N):
    random_names=[]
    for i in range(1,N + 1):
        num = random.randint(0, N)
        #print(num)
        random_names.append(names_list[num])
    return random_names

def commonName(Names):
        count =dict()
        for word in Names:
            count[word] = count.get(word,0) + 1
            max = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return max[0]

mn=str(male_names_text.text)
fn=str(female_names_text.text)

m = re.sub(r'#.*\n', '', mn)
f = re.sub(r'#.*\n', '', fn)
m= re.sub('^\n', '', m)
f= re.sub('^\n', '', f)

male_names_list = m.split()
female_names_list = f.split()

names = male_names_list + female_names_list

print(F(names, 100))
print(len(F(names,100)))
print(commonName(F(names,100)))

