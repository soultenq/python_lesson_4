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

def F(Names, N):
    random_names = []
    lenght=len(Names)
    for i in range(1,N + 1):
        num = random.randint(0, lenght - 1)
        #print(num)
        random_names.append(Names[num])
        #print(names_list[num])
    return random_names

def commonName(Names):
        count = dict()
        for word in Names:
            count[word] = count.get(word,0) + 1
            common = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return common[0]

def rareLetter(Names):
    letters = dict()
    count= dict()
    for word in Names:
        letters[word] = str(word[0])
        letter = letters.get(word)
        count[letter] = count.get(letter,0) + 1
        max_letter = sorted(count.items(), key=lambda x: x[1], reverse=False)
    #print(letters)
    return max_letter[0]

mn=str(male_names_text.text)
fn=str(female_names_text.text)

m = re.sub(r'#.*\n', '', mn)
f = re.sub(r'#.*\n', '', fn)
m= re.sub('^\n', '', m)
f= re.sub('^\n', '', f)

male_names_list = m.split()
female_names_list = f.split()

names = male_names_list + female_names_list

#names = ['Yanja', 'Vasily', 'Basili', 'Vera', 'Sara', 'Janna', 'Valya', 'Michael', 'Mila', 'Liuda', 'Daria', 'Denis', 'John', 'Josepth', 'Xander', 'Nikolay', 'Roza']

print(F(names, 100))
print(len(F(names,100)))
print(commonName(F(names,100)))
print(rareLetter(F(names,100)))
