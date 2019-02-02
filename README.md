# Social network creation 

This is the basic code for social network generation for a list of characters, and given (word embedding, or other) models.
It's evaluated against a gold standard created with crowdsourcing.
This is a reduced version of the code used eg in this publication: [http://www.aclweb.org/anthology/W16-4004](http://www.aclweb.org/anthology/W16-4004)


## Prelimaries
Make sure that you have the word embedding models.
You can make the `models` directory point to the models in `https://github.com/gwohlgen/digitalhumanities_dataset_and_eval/models`.
(I didn't want to upload the same models to github twice).


## Running

First, change in `src` directory directory.

Run both these scripts:
`python generate_relations.py (asoif|hp)`
`python eval_relations.py (asoif|hp)`

The first script iterates of all word embedding models defined in config.py and creates the closest relations for the input characters. 
The second script evaluates the results of the first script against the gold standard data from the `datasets/` directory.

## More details

The `datasets` directory contains the starting point, which is a list of characters used in social network construction, and 
it contains variants of the gold standard datasets created with crowdsourcing (CrowdFlower).

The `models` directory contains the models. Best replace with a symlink to the models from 
the `https://github.com/gwohlgen/digitalhumanities_dataset_and_eval/models` repo, see above.

## To cite our work, use eg:

```
@InProceedings{wohlgenannt2016lt4dh,
  author    = {Wohlgenannt, Gerhard  and  Chernyak, Ekaterina  and  Ilvovsky, Dmitry},
  title     = {Extracting Social Networks from Literary Text with Word Embedding Tools},
  booktitle = {Proceedings of the Workshop on Language Technology Resources and Tools for Digital Humanities (LT4DH)},
  month     = {December},
  year      = {2016},
  address   = {Osaka, Japan},
  publisher = {The COLING 2016 Organizing Committee},
  pages     = {18--25},
  abstract  = {In this paper a social network is extracted from a literary text. The social
    network shows, how frequent the characters interact and how similar their
    social behavior is. Two types of similarity measures are used: the first
    applies co-occurrence statistics, while the second exploits cosine similarity
    on different types of word embedding vectors.
    The results are evaluated by a paid micro-task crowdsourcing survey. The
    experiments suggest that specific types of word embeddings like word2vec are
    well-suited for the task at hand and the specific circumstances of literary
    fiction text.},
```
