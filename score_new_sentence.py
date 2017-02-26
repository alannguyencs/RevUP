import gensim
from gensim import corpora
from get_data import Get_data
from get_clean_data import Get_clean_data
from get_ldamodel import Get_ldamodel



doc_clean = Get_clean_data()
doc_complete = Get_data()


# Creating the term dictionary of our corpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)
#print (dictionary.token2id)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

ldamodel = Get_ldamodel()

def get_score_doc(lda, bow):
    gamma, _ = lda.inference([bow])
    topic_dist = gamma[0] / sum(gamma[0])  # normalize distribution
    top_topic_value = []
    for _, topicvalue in enumerate(topic_dist):
        # print topicvalue,
        top_topic_value.append(topicvalue)
    top_topic_value = sorted(top_topic_value, reverse = True)
    # for i in top_topic_value:
    #     print i,
    # print
    score = 0.0
    if len(top_topic_value) < 3:
        for i in top_topic_value:
            score += i
    else:
        for i in range(1):
            score += top_topic_value[i]
    return score


print ("Number of topic: 100")
id_score = {}
doc_score = []
for i in range(len(doc_clean)):
    # print doc_complete[i]
    score = get_score_doc(ldamodel, doc_term_matrix[i])
    id_score[score] = i
    doc_score.append(score)
    # print doc_clean[i]
    # print get_score_doc(ldamodel, doc_term_matrix[i])
    # print

doc_score = sorted(doc_score, reverse = True)
for i in doc_score:
    print i, doc_complete[id_score[i]]
