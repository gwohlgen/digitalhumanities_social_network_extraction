import sys

## use the input parameter to select the book series
if len(sys.argv) < 2:
    raise Exception("We need two command line arguments!")
if sys.argv[1].lower() == 'asoif':
    BOOK_SERIES="asoif"
elif sys.argv[1].lower() == 'hp':
    BOOK_SERIES="hp" 
else:
    raise Exception("the book series must be either *ASOIF* or *HP*")

NUM_CONNS = 2 # important: number of related characters to compute for any character
MODEL_PATH="../models/"
DUMPFILE = BOOK_SERIES + '_person_data.pickle'


if BOOK_SERIES == "asoif":

    # models to be used
    MODELS = [ 
        ('asoif_w2v-default-bash','bin'),
        ('asoif_w2v-w12-cbow-bash','bin'),
        ('asoif_w2v-w12-i15-bash','bin'),
        ('asoif_w2v-w12-i15-ns-bash','bin'),
        ('asoif_fasttext-12-e25-bash', 'vec'),
    ]

    # pathes to crowdflower gold data
    AGGR_EVAL_DATA_FN   = "../datasets/asoif_final_aggr_15_votes_units.csv.pickle"
    DETAILED_EVAL_DATA_FN   = "../datasets/asoif_final_detailed_15_votes_units.csv.pickle"
    DETAILED_EVAL_DATA_4_PLUS_VOTES_FN = "../datasets/asoif_final_detailed_15_votes_4_plus_votes_units.csv.pickle"


elif BOOK_SERIES == "hp":

    # models to be used
    MODELS = [
        ('hp_w2v-default-bash','bin'),
        ('hp_w2v-w12-cbow-bash','bin'),
        ('hp_w2v-w12-i15-bash','bin'),
        ('hp_w2v-w12-i15-ns-bash','bin'),
        ('hp_fasttext-12-e25-bash','vec'),
    ]

    # pathes to crowdflower gold data
    AGGR_EVAL_DATA_FN               = "../datasets/hp_final_aggr_15_votes_units.csv.pickle"
    DETAILED_EVAL_DATA_FN           = "../datasets/hp_final_detailed_15_votes_units.csv.pickle"
    DETAILED_EVAL_DATA_4_PLUS_VOTES_FN = "../datasets/hp_final_detailed_15_votes_4_plus_votes_units.csv.pickle"
