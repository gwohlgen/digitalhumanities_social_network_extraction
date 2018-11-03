import pickle
import eval_helpers 
from config import DUMPFILE, AGGR_EVAL_DATA_FN, DETAILED_EVAL_DATA_4_PLUS_VOTES_FN, DETAILED_EVAL_DATA_FN, MODELS
from pprint import pprint

"""
    given the related characters per character stored in DUMPFILE
    1) compare to the gold standard data from crowdsourcing 
        1a) aggregated stats -- overlap on top suggestions
        1b) detailed stats -- overlap on top two suggestions
        1c) overlap characters with at least 4 votes
    
"""

# load person data from all our models
model_suggested_data            = pickle.load(open(DUMPFILE, 'rb'))
aggr_eval_data                  = pickle.load(open(AGGR_EVAL_DATA_FN, 'rb'))
detailed_eval_data              = pickle.load(open(DETAILED_EVAL_DATA_FN, 'rb'))
detailed_eval_data_4_plus_votes = pickle.load(open(DETAILED_EVAL_DATA_4_PLUS_VOTES_FN, 'rb'))


# get stats for aggregated data
print("\n\n")
for (model,emb_type) in MODELS:
    eval_helpers.get_precent_nums(aggr_eval_data, model_suggested_data[model], model=model)

print("\n\n")

# get stats for detailed data -- top two suggestions
for (model, emb_type) in MODELS:
    eval_helpers.my_simple_average_aggreement(detailed_eval_data, model_suggested_data[model], model=model, print_errors=False)

print("\n\n")

# get stats for detailed data -- suggestions with at least 4 votes
for (model, emb_type) in MODELS:
    eval_helpers.my_simple_average_aggreement(detailed_eval_data_4_plus_votes, model_suggested_data[model], model=model, print_errors=False, gs_mode="plus_n_votes")

print("\n\n")

# if BOOK_SERIES == "asoif":
#     # glove vs w2v
#     print("w2v_default vs glove",         eval_helpers.my_simple_average_aggreement(model_suggested_data['w2v_default'], model_suggested_data['glove'], model="w2v_default vs glove", gs=False))
#     print("w2v_default vs w2v_SG12_300_hs", eval_helpers.my_simple_average_aggreement(model_suggested_data['w2v_default'], model_suggested_data['w2v_SG12_300_hs'], model="w2v_default vs w2v_SG12_300_hs", gs=False))
#     print("w2v_CBOW0_300_hs_disamb vs w2v_SG12_300_hs", eval_helpers.my_simple_average_aggreement(model_suggested_data['w2v_CBOW0_300_hs_disamb'], model_suggested_data['w2v_SG12_300_hs'], model="w2v_CBOW0_300_hs_disamb vs w2v_SG12_300_hs", gs=False))
# 
#     cf_all_res = pickle.load(open(CF_ALL_RES_DATA))
#     print("\nglove missing terms",           eval_helpers.glove_missing_terms(cf_all_res, model_suggested_data['glove']))
#     print("\nw2v_SG12_300_hs missing terms", eval_helpers.glove_missing_terms(cf_all_res, model_suggested_data['w2v_SG12_300_hs']))
#     print("\nw2v_CBOW0_300_hs_disamb missing terms", eval_helpers.glove_missing_terms(cf_all_res, model_suggested_data['w2v_CBOW0_300_hs_disamb']))
# 
# if BOOK_SERIES == "hp":
# 
#     print("\nglove missing terms",           eval_helpers.glove_missing_terms(cf_all_res, model_suggested_data['glove']))
#     print("\nw2v_SG12_300_hs missing terms", eval_helpers.glove_missing_terms(cf_all_res, model_suggested_data['w2v_SG12_300_hs']))
#     print("\nw2v_CBOW0_300_hs_disamb missing terms", eval_helpers.glove_missing_terms(cf_all_res, model_suggested_data['w2v_CBOW0_300_hs_disamb']))
# 
# 
# 
#     # glove vs w2v
#     print("w2v.skipgram.w12.hs1.300dim vs glove_hp",  eval_helpers.my_simple_average_aggreement(model_suggested_data['w2v.skipgram.w12.hs1.300dim'], model_suggested_data['glove_hp'], model="w2v.skipgram.w12.hs1.300dim vs glove_hp", gs=False))
#     print("w2v.skipgram.w12.hs1.300dim vs fasttext_hp_25epoch", eval_helpers.my_simple_average_aggreement(model_suggested_data['w2v.skipgram.w12.hs1.300dim'], model_suggested_data['fasttext_hp_25epoch'], model="w2v.skipgram.w12.hs1.300dim vs fasttext_hp_25epoch", gs=False))
#     print("w2v.skipgram.w12.hs1.300dim vs lexvec_hp", eval_helpers.my_simple_average_aggreement(model_suggested_data['w2v.skipgram.w12.hs1.300dim'], model_suggested_data['lexvec_hp'], model="w2v.skipgram.w12.hs1.300dim vs lexvec_hp", gs=False))
#     print("glove_hp vs lexvec_hp", eval_helpers.my_simple_average_aggreement(model_suggested_data['glove_hp'], model_suggested_data['lexvec_hp'], model="glove_hp vs lexvec_hp", gs=False))
#     print("fasttext_hp_25epoch vs fasttext_hp", eval_helpers.my_simple_average_aggreement(model_suggested_data['fasttext_hp'], model_suggested_data['fasttext_hp_25epoch'], model="fasttext_hp_25epoch vs fasttext_hp", gs=False))
# 
#     cf_all_res = pickle.load(open(CF_ALL_RES_DATA))
#     print("glove_hp missing terms",           eval_helpers.glove_missing_terms(cf_all_res, model_suggested_data['glove_hp']))
#     print("w2v.skipgram.w12.hs1.300dim missing terms", eval_helpers.glove_missing_terms(cf_all_res, model_suggested_data['w2v.skipgram.w12.hs1.300dim']))
#     print("fasttext_hp_25epoch missing terms", eval_helpers.glove_missing_terms(cf_all_res, model_suggested_data['fasttext_hp_25epoch']))
# 
