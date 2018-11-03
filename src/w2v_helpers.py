import os, operator
from config import *
import gensim.models

def load_models(mode=None, emb_type=None):
    """ simply load the models from the file system as gensim models """

    if emb_type == "vec":   binary = False
    elif emb_type == "bin": binary = True
    else: raise Exception()

    print("\n\n**** Model:", mode, " binary:", binary)

    word_model = gensim.models.KeyedVectors.load_word2vec_format(MODEL_PATH + mode + ".model", binary=binary)
    word_model.init_sims(replace=True) # clean up RAM

    print("**** Model:", mode, " LOADED\n\n")

    return word_model


def get_similiar_persons(person_list, mode=None, emb_type=None):
    """ 
        1) load models
        2) iterate over persons
            2a) get related persons
        3) store and return
    """ 

    word_model = load_models(mode, emb_type)

    print("\n\nin get_soiaf_similiar_persons, mode:", str(mode))

    sims = {}
    for person in person_list:
        sims[person] = {}

        for other_person in person_list:
            if person == other_person: continue # don't compute relation to oneself

            # compute simi and save
            if mode=="w2vf" or mode.find('preprocessed')>=0 or mode.find('lower')>=0:
                sim = word_model.similarity(person.lower(), other_person.lower())
            else:
                sim = word_model.similarity(person, other_person)
            sims[person][other_person] = sim


        # sort the sims per person
        sorted_sim = sorted(sims[person].items(), key=operator.itemgetter(1))
        sorted_sim.reverse()

        sims[person] = sorted_sim[:NUM_CONNS]
        print(person, sims[person])

    return sims
