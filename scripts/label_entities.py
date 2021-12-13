from typing import List

import pandas as pd
import nltk


DATA_FOLDER = '../data/'
DATA_FILE = 'oracle.csv'


def tokenize_text(body: str) -> List[str]:
    return nltk.word_tokenize(body)


def main():
    oracle: pd.DataFrame = pd.read_csv(DATA_FOLDER+DATA_FILE)
    text_and_entities = oracle[['body', 'entity type', 'entity']]
    print(text_and_entities.head(5))

if __name__ == "__main__":
    main()
