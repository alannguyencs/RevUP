import gensim
from gensim import corpora
from get_clean_training_data import Get_clean_training_data

def Generate_ldamodel():

    doc_clean = Get_clean_training_data()


    # Creating the term dictionary of our corpus, where every unique term is assigned an index.
    dictionary = corpora.Dictionary(doc_clean)
    # print (dictionary.token2id)

    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

    # Creating the object for LDA model using gensim library
    Lda = gensim.models.ldamodel.LdaModel

    # Running and Training LDA model on the document term matrix.
    ldamodel = Lda(doc_term_matrix, num_topics = 100, id2word = dictionary, passes=500)   #passes = number of loops

    ldamodel.save("AI_ldamodel.model")
def Get_ldamodel():
    ldamodel = gensim.models.ldamodel.LdaModel.load("AI_ldamodel.model")
    return ldamodel

# Generate_ldamodel()