#loading data
import json
#data for similar words
from difflib import get_close_matches

data = json.load(open("dat.json"))

#processing word
def translate(word):
    
    #translate to lowercase
    word = word.lower()


#retrieving data for word
    if word in data:
        return data[word]
#finding similar words    
    elif len(get_close_matches(word, data.keys())) > 0:
       yn = input ("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(word, data.keys())[0])
      #nested conditional
       if yn == "Y":
           return data[get_close_matches(word, data.keys())[0]]
        #if word doesnt exist
       elif yn == "N":
            return "The word doesn't exist, Please check, and retype the word!"
        #still cant understand
       else:
           return "We don't understand  your entry."     

#translating given word
word = input("Enter word: ")

output = translate(word)

#making it user friendly
if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)

