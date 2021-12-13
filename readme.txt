README for G12
--------------

Our project relies mainly on sklearn, pandas, numpy, scipy, sklearn-crfsuite.
Our code submission contains the following files:

./requirements.txt       <-- pip environment for our project
./script/data_prep.py    <-- script to preprocess (prepare) our data
./script/model.ipynb     <-- notebook where we train and test the model + provide our report
./script/plot_helper.py  <-- script used to plot the performance figure in the pdf report
./data/oracle.csv        <-- our raw manually labelled dataset
./data/data.pickle       <-- our processed dataset that results from running `data_prep.py`


* While the preprocessed data is shared in the `./data/data.pickle` file, we can also run the whole experiment starting
  from the raw data:
  - run ./script/data_prep.py
  - run ./script/model.ipynb

* GPU is not required.
* Training takes ~10 minutes.
* The ./script/data_prep.py script creates a `data.pickle` file in the `data` dir.


For training the CRF we relied heavily on the tutorial found at https://sklearn-crfsuite.readthedocs.io/en/latest/tutorial.html