import pickle,sys
import w2v_helpers
from config import MODELS, BOOK_SERIES, DUMPFILE

"""
    Create a "social network" for a list of input characters by finding close relations in vector space.

    INPUT:  a list of character names, and the list of (word embedding models to be used)
    RESULT: the config.NUM_CONNS closest related characters for any input character -- per model
"""


# 1) read the list of characters
freq_persons = pickle.load(open('../datasets/'+ BOOK_SERIES + '_freq_persons.pickle', 'rb'))
person_list = [x for x,y in freq_persons] # persons without frequency information
print('\n\nCharacters loaded:',    person_list)
print('Number of Characters:', len(person_list))

model_suggested_data = {}

# 2) iterate over models, get related characters
for (model,emb_type) in MODELS:
    print("\n\n\nNext model:", model, "\n")

    model_suggested_data[model] = w2v_helpers.get_similiar_persons(person_list, mode=model, emb_type=emb_type)

# 3) dump for later usage -- Done
print("\n\nwriting to", DUMPFILE)
pickle.dump(model_suggested_data, open(DUMPFILE, 'wb'))

