


import math



def norm(vec):
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x] 
    
    return math.sqrt(sum_of_squares)

#subpart a 
def cosine_similarity(vec1, vec2): 
    numerator = 0
    for key1, val1 in vec1.items():
        numerator += val1 * (vec2.get(key1, 0))
        
    return numerator/((norm(vec1)*norm(vec2)))

                               
# subpart b 
def build_semantic_descriptors(sentences):
    dictionary_count = {}  
    for sentence in sentences:  # looking at one sentence/list
        checked_word2 = []
        for word in sentence:  #looking at each word in the sentence/list
            #if not there return empty list 
            if word not in checked_word2 :
                checked_word = []
                if word not in dictionary_count:
                    dictionary_count[word] = {}
                checked_word2.append(word)
                #checking the sentence for each word  
                for each_word in sentence:
                    if (each_word != word) and each_word not in checked_word and each_word not in dictionary_count[word]:
                        dictionary_count[word][each_word] = 1
                        checked_word.append(each_word)
                    elif (each_word != word) and each_word not in checked_word and each_word in dictionary_count[word]:
                        dictionary_count[word][each_word] +=1  
                        checked_word.append(each_word)
    return dictionary_count  

# subpart c 
def build_semantic_descriptors_from_files(filenames):
    listed_sentences = []
    for files in filenames:
        text = open(files, "r", encoding="latin1").read().lower() 

        text = text.replace("!",".")
        text = text.replace("?",".")
        text = text.replace(",","")
        text = text.replace("-"," ")
        text = text.replace("--"," ")
        text = text.replace(":","")
        text = text.replace(";","") 

        text = text.split(".")  

        for j in text: 
            sentences = j.split()
            listed_sentences.append(sentences) 


    return build_semantic_descriptors(listed_sentences)


# part d
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    highest_similarity = -1 
    most_sim_word_choice = None
    for i in choices:
        if i in semantic_descriptors:
            if word in semantic_descriptors.keys():
                similar_word = similarity_fn(semantic_descriptors[word], semantic_descriptors[i])
                if similar_word > highest_similarity:
                    highest_similarity = similar_word
                    most_sim_word_choice = i 
    return most_sim_word_choice


# part e
def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct = 0
    f = open(filename, "r", encoding = "latin1") 
    line = f.readlines()
    ques = len(line)
    for i in line:
        words = i.split()
        if words[1] == most_similar_word(words[0], words[2:], semantic_descriptors, similarity_fn):
            correct += 1
    return (correct/ques)*100
  




if __name__ == "__main__":  

    sem = build_semantic_descriptors_from_files(["book1.txt", "book2.txt"])
    res = run_similarity_test("text.txt", sem, cosine_similarity)
    print(res)

