# Progress Report

2/12/2022

- Created repository with the appropriate .gitignore and license.


## 1st Progress Report

### Work

#### Blog Authorship Corpus

The initial purpose of this project was to find markers of age group within the Blog Authorship Corpus dataset, and see how markers (punctuation/words) characterize texts written by a particular age group. 

So far, I downloaded the Blog Authorship Corpus in it's original XML form, and also found a version of it which is identical in CSV form. I wan't too sure if they were identical, so I inspected the data and verified it as a sanity check.

The data import and basic EDA is contained in `data.ipynb`

From the feedback given in the proposal, there was a mention of "value-add". So, I thought about it.

#### Reddit Data


### Sharing Plan

For both datasets, there are a few examples of data in `blog_samples/`. I used the notebook `process_blog_data` to sample data from the dataset and provide small examples. `csv_sample.csv` contains the information in it's simplest form, a CSV file.

It isn't readable, so I organized a nested directory holding age group and raw text under the template <ID>.txt. This is more complicated, but it is readable, which is why it is a good idea to share it in this way. 
  
The groups are equally represented.

