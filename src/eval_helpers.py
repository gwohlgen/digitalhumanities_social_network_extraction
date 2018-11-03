
def get_precent_nums(eval_data, model_data, model=None):

    tot_num = 0.0
    nu_one = 0
    in_two = 0

    for person, conn_person in eval_data.items():
        
        conn_persons = [p for p,v in model_data[person]]

        if conn_person == conn_persons[0]:
            #print "NUMBER ONE", person, conn_person, conn_persons  
            nu_one+=1
        if conn_person in conn_persons: 
            #print "IN THREE", person, conn_person, conn_persons  
            in_two+=1

        tot_num+=1

    # calculate percentages
    perc_one   = nu_one   / tot_num
    perc_two = in_two / tot_num

    print("AGGREGATED RESULTS: Model", model, ": CF-favorite is number one choice:", perc_one*100, ", CF-favorite is in top2:", perc_two*100)


def my_simple_average_aggreement(eval_data, model_data, model=None, gs=True, print_errors=False, gs_mode=None):
    """
        basically, starting with the gold standard (which is CF), we 
        do "average of CF AND METHOD / CF"

        @param eval_data: the gold standard data
        @param model_data: the data from the model to be evaluated 

        @param model .. name of the model, eg. "word2vec"
        @print_errors .. for a detailed analysis, print the agreement and differences to the gold standard
        @gs_mode      .. selection mode for the gold standard data .. default: take the best 2 characters
                      .. gs_mode "plus_n_votes": use all characters as correct that got plus_n_votes
    """
    #print eval_data, "\n\n", model_data; sys.exit()
    res_vals, gs_len = [], []

    for name, raw_conns in eval_data.items(): 
        gs_persons = set([x for x,y in raw_conns])
        gs_len.append(len(gs_persons)) 
        model_persons = set([x for x,y in model_data[name]]) 

        if print_errors:
            print(model, "\nCharacter", name, "overlap:",  gs_persons & model_persons)
            print(model, "Character", name, "difference:", model_persons - gs_persons)

        res_vals.append( len(gs_persons & model_persons) / float(len(model_persons)) )


    avg = sum(res_vals) / float(len(res_vals))
    if gs:
        if gs_mode == "plus_n_votes":
            if model == "coo_chapters":
                print("avg(len(gs_persons)): %s " % (sum(gs_len)/float(len(gs_len))))
                print("len(gs_persons): %s " % (gs_len,))

 
            print("DETAILED RESULTS (PLUS_N):  Model", model, ": simple aggreement betw CF (gold standard) and model:", avg*100)

        else:
            print("DETAILED RESULTS (DEFAULT): Model", model, ": simple aggreement betw CF (gold standard) and model:", avg*100)


    else:
        print("DETAILED RESULTS: Model", model, ": simple aggreement:", avg*100)

    return ""

if __name__=="__main__":

    a = {'Stannis': [('Renly', 15), ('Robert', 14), ('Davos', 14)],   'Balon': [('Theon', 15), ('Euron', 14), ('Robert', 8)]}
    b = {'Stannis': [('Robert', 61), ('Cersei', 55), ('Davos', 54)],  'Balon': [('Cersei', 33), ('Robert', 32), ('Tywin', 8)]}
    my_simple_average_aggreement(a,b) 
   
