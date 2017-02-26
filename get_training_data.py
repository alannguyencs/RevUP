#return a list of sentences
def Get_Training_data():
    data = open("Artificial_Intelligent.txt", "r")
    doc_raw = ""
    for line in data:
        line = line.decode('utf-8')
        doc_raw += line[:len(line)-1]
        doc_raw += " "

    # print doc_raw
    doc_clean_dot = ""
    #delete '.' which do not end a sentence
    for i in range(len(doc_raw)):
        if doc_raw[i] == '.' or doc_raw[i] == '?':
            end_sentence = True
            for j in range(i + 1, len(doc_raw)):
                if(doc_raw[j].isalpha()):
                    end_sentence = doc_raw[j].isupper()
                    break
            if not end_sentence:
                continue
        if doc_raw[i] == '?':
            doc_clean_dot += '.'
            continue
        doc_clean_dot += doc_raw[i]

    # print doc_clean_dot
    doc_complete = []
    for sentence in (doc_clean_dot.split('.')):
        doc_complete.append(sentence)
        # print sentence

    print ("Number of sentences in training data:",len(doc_complete))
    return doc_complete

# Get_AI_data()

