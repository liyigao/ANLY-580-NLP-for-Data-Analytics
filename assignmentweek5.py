from gensim.models import KeyedVectors

import gensim

vecfile = 'GoogleNews-vectors-negative300.bin'
vecs = KeyedVectors.load_word2vec_format(vecfile, binary=True)

# vecs.vector_size      	result: 300
# len(vecs.index2word)  	result: 3000000

# vecs.most_similar(positive = ["picnic"], topn = 5)
# [('picnics', 0.7400875091552734), ('picnic_lunch', 0.7213739156723022),
# ('Picnic', 0.7005339860916138), ('potluck_picnic', 0.6683273911476135),
# ('picnic_supper', 0.6518912315368652)]


# vecs.doesnt_match(['tissue', 'papyrus', 'manila', 'newsprint', 'parchment', 'gazette'])

# 'tissue'

# vecs.most_similar(positive = ["throw", "leg"], negative = ["jump"], topn = 1)

# [('legs', 0.45747825503349304)]



