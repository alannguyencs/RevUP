#return a list of sentences
def Get_data(filename):
    # data = open("data.txt", "r")
    # data = open("word2vec_data.txt", "r")
    # data = open("Artificial_Intelligent.txt", "r")
    # data = open("neuron_network_data.txt", "r")
    data = open(filename, "r")
    doc_raw = ""
    for line in data:
        line = line.decode('utf-8')
        # delete some [number] in wiki
        ck = True
        for j in range(len(line)-1):
            if(line[j] == '[' and line[j+1].isdigit()):
                ck = False
            if(ck):
                doc_raw += line[j]
            if (line[j] == ']'):
                ck = True
        doc_raw += " "



    doc_complete = []
    for sentence in (doc_raw.split('. ')):
        doc_complete.append(sentence)
        # print sentence

    return doc_complete

# Extract_data()

