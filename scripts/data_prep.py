from itertools import chain
import nltk
import sklearn
import scipy.stats
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
import pandas as pd
import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics
import eli5
from typing import List
import nltk
from nltk import pos_tag
import emoji
import re
import random
from pathlib import Path
from string import punctuation
from process_urls import process_url
import pickle

def iob_tag(pos_tagged_tokens, entity_tuples):

    iob_tagged_tokens = []
    entity_tuples_dict = dict(entity_tuples)

    for token in pos_tagged_tokens:
        if token[0] in entity_tuples_dict.keys():
            entity_type = entity_tuples_dict[token[0]]
            iob_tagged_tokens.append((token[0], token[1], entity_type))
        else:
            iob_tagged_tokens.append((token[0], token[1], 'O'))

    return iob_tagged_tokens


def prepare_text(text, entity_tuples):
    tokens = [token.strip(punctuation) for token in text.split()]
    pos_tags = pos_tag(tokens)
    return iob_tag(pos_tags, entity_tuples)


def keep_sents_with_entities(txt_body: str, entity: str) -> str:
    """
    This function takes a body of text, splits it into sentences, and then searches for the sentences that include the
    entity to keep them.
    :return: a string of the sentences (1 or more) that include the entity.
    """
    all_sentences: List[str] = nltk.sent_tokenize(txt_body)
    sentences_with_entities: List[str] = [sent for sent in all_sentences if entity in sent]

    return ''.join(sentences_with_entities)


def clean_body(df_row) -> str:
    return keep_sents_with_entities(df_row.body, df_row.entity)


def clean_entity(entity) -> str:
    """
    removes leading and trailing punctuation and empty whitespaces from entities
    """
    return entity.strip(punctuation).strip()


def check_for_entity(df_row) -> str:
    for entity_tuple in df_row.entity_tuples:

        entity = entity_tuple[0]
        tokens = [token.strip(punctuation) for token in df_row.body.split()]


        if entity in tokens:
            pass
        elif entity in '\t'.join(tokens):
            print(f'looking for *{entity}* in {tokens}')
            print('Partial match\n')
        else:
            print(f'looking for *{entity}* in {tokens}')
            print('No match!\n')
            # print()

    return

def main():
    data_dir = '../data/'
    labelled_entities_filename = 'oracle.csv'
    oracle_data_file = Path(data_dir, labelled_entities_filename)

    oracle: pd.DataFrame = pd.read_csv(oracle_data_file)

    # clean the body
    oracle.body = oracle.apply(lambda row: clean_body(row), axis=1)

    # clean the entity
    oracle.entity = oracle.entity.apply(clean_entity)

    # rename entity types:
    oracle['entity type'].replace({'branch_name': 'B-BRANCH', 'file_name': 'B-FILE', 'issue_number': 'B-ISSUE'},
                                  inplace=True)

    # combine entity and entity type as a tuple
    oracle['entity_tuples'] = oracle[["entity", "entity type"]].apply(tuple, axis=1)

    # group entities within the same body as a list
    oracle = oracle['entity_tuples'].groupby([oracle.body]).apply(list).reset_index()

    data = []
    for index, row in oracle.iterrows():
        data.append(prepare_text(row.body, row.entity_tuples))

    tagged_data_file = Path(data_dir, 'data.pickle')
    with open(tagged_data_file, 'wb') as f:
        pickle.dump(data, f)

if __name__ == "__main__":
    main()
