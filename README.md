# machine-learning-carpentry
files for workshop on text classification with machine learning
 
## Machine Learning for Text Classification
This repository contains teaching materials for a workshop on using machine learning algorithms to categorize text data. Although the files here are intended to supplement an in-person classroom environment, they may be useful as an online tutorial as well.

The code samples and tutorials focus on using Python to preparing data, calling the machine learning (scikit-learn) api, and writing and interpreting results. We will review the various machine learning algorithms at a very high level, but we won't get into the details or mathematics of these algorithms. Note that these examples will use Python 3 and Jupyter Notebooks for most of the tutorials.

As an example case, we'll train a machine learning algorithm to distingish between positive and a negative movie reviews, using sentiment data from:
http://www.cs.cornell.edu/home/llee/papers/sentiment.home.html

### Installation Note
This repository is designed to be run through Jupyter Notebook.  Workshop participants can check this repo out and run `jupyter notebook` at the top level of the directory to access and run this code. 

Participants will need to install scikit-learn to run the code in the workbooks.  

### [Introduction](Overview.ipynb)
A quick introduction, text classification and machine in a data carpentry context. 

### [Bag Of Words](BagOfWords.ipynb)
A jupyter notebook demonstrating how to use python and scikit-learn to convert document text into "word vectors" that can be used to train a machine learning model. Specifically, we'll show how to decompose a movie review into a "word vector", a data structure that holds the term frequencies for a particular record.

### [Machine Learning - Overview](supervised_learning_visuals)
A jupyter notebook containing slides, a set of graphical representations of Naive Bayes, Logistic Regression, Support Vector Machine, Neural Network, and Random Forest. These slides are not intended as a deep dive into machine learning - instead, they provide a visual representation of each algorithm for a high level overview.

### [Machine Learning - Code](MachineLearning.ipynb)
"Machine Learning", a jupyter notebook that demonstrates how to use python and scikit-learn to train, run, and interpret results from a machine learning model. The programming approach will be illustrated through Random Forest, with an emphasis on preparing data and using the API. The notebook will also show how to swap in a different machine learning model with minimal programming changes. Specifically, we'll show how to use a trained machine learning model to classify movie reviews based on the term frequencies from that review.

### [Further Reading](recommended-reading.ipynb)
Links to further learning material, blogs, code samples, tutorials, and documentation.

### [Classifier.py](Classifier.py)
A python script that provides a more compact and succinct program to build, train, run, and read output from a machine learning model.

### Data Preparation Files (createfile.py and shufflefile.py)
The sentiment data from cornell is stored as a collection of files in a directory tree, with one file per review. I find that it is easier to work with tab delimited files with each record stored in a row (ID, classification, text). The data preparation files, `createfile.py` and `shufflefile.py`, are used to prepare a tab delimited file that can be read into a pandas dataframe. There isn't much to these files, and the data was already well ordered, but it's worth pointing out that even in the best case, you still usually have to do some piping and processing to get the data into a format where you can use it in a machine learning model.

### Teaching Notes
I want to emphasize that this material is intended to be part of a course, with an instructor who can explain the concepts. The tutorials don't contain long explanations - instead, they contain material that can be used, along with instructor-led discussion and explanation, to teach workshop participants how to classify text through machine learning with Python 3.

I also want to emphasize that this workshop focuses heavily on python, programming, data preparation, and using the scikit-learn library. It doesn't cover the algorithms beyond a quick, visual overview. The emphasis here is on learning how to prepare data, call an API, and read the results.
