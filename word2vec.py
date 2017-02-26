import gensim
from get_clean_data import Get_clean_data

sentences = Get_clean_data("neuron_network_data.txt")

model = gensim.models.Word2Vec(sentences, size=100, min_count = 1)

A = {}
B = {}

print model.most_similar('neural', topn = 10)

# for s in sentences:
#     for word in s:
#         try:
#             y = model[word]
#             print word
#             if word not in A:
#                 A[word] = 1
#             else:
#                 A[word] += 1
#         except:
#             B[word] = True
#             if word not in B:
#                 B[word] = 1
#             else:
#                 B[word] += 1
# print len(A)
# for key in A:
#     print A[key], key

# print "-"*25
# print len(B)
# for key in B:
#     print key, B[key]

# print model.most_similar("video", topn = 15)
# for s in sentences:
#     # print s
#     ck = True
#     for word in s:
#         if word in A:
#             ck = False
#             print word,
#         else:
#             print "    ",
#
#     print
#     if ck:
#         print "-" * 25

