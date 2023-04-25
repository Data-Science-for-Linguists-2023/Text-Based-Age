# Linguistic Features for Age Detection in Text

Name: Varun Venkatesh

Email: vav30@pitt.edu

Date: 04/25/2023

## Description

This project aims to find markers of age within blog posts using The Blog Authorship Corpus and within comments from a gathered age-grouped Reddit Dataset.

## Dataset

The "found" dataset used for this project is the [Blog Authorship Corpus](https://u.cs.biu.ac.il/~koppel/BlogCorpus.htm), which contains over 600,000 posts written on a wide range of topics. The dataset is available on Kaggle and was originally compiled by Dr. Jichan Zeng at the University of Illinois at Urbana-Champaign. 

The project also involves the collection, processing, and usage of a custom reddit dataset that is divided into age groups. More info can be found [here](https://github.com/Data-Science-for-Linguists-2023/Text-Based-Age-Recognition/blob/main/progress_report.md#3rd-progress-report), as well as the [`reddit_data/`](reddit_data/) folder.


## Important Files and Folders

- [**`final_report.md`**](final_report.md) : A report detailing the final results of the project
- [`progress_report.md`](progress_report.md): A report detailing the progress made, with steps, process, timeline, etc.
- [`data_samples/`](data_samples/): Contains the raw data files as well as processed data samples
- [`scripts/`](scripts/): Contains Python scripts for various tasks (preprocessing, feature extraction, model training, and model evaluation)
- [`notebooks/`](notebooks/): Contains iPython Notebooks (Jupyter) for the main work like discovery, processing, EDA, analysis, etc.

Feedback and comments on the project are in the [Guestbook](https://github.com/Data-Science-for-Linguists-2023/Class-Lounge/blob/main/guestbooks/varun.md)


## Most Important Jupyter Notebooks

- [`blog_final.ipynb`](notebooks/data_analysis/final/blog_final.ipynb): A Jupyter notebook detailing the analysis of the blog authorship corpus
- [`reddit_final.ipynb`](notebooks/data_analysis/final/reddit_final.ipynb): A Jupyter notebook detailing the analysis of the reddit dataset
- [`process_blog_data.ipynb`](notebooks/data_extraction/process_blog_data.ipynb): A Jupyter notebook detailing the extraction of the blog authorship corpus
- [`process_reddit_data.ipynb`](notebooks/data_extraction/process_reddit_data.ipynb): A Jupyter notebook detailing the extraction of the raw reddit data obtained using [this script](scripts/reddit_comment_fetch.py)

**Note:** If the Jupyter notebooks fail to load on GitHub, use the [nbviewer](https://nbviewer.jupyter.org/) links provided in the top of the corresponding files.


To replicate any work, run the following:

```
# create virtual environment
python3 -m venv /path/to/new/virtual/environment
# activate virtual environment
source /path/to/new/virtual/environment/bin/activate
# install requirements
pip3 install -r requirements.txt
```