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

Age-labelled text datasets are hard to find. This is likely due to privacy and the traditional use of age as part of a UUID for most systems, which is why it wouldn't be a good idea on the entity's part to normally share.

I decided to see if I could find reddit forums (subreddits) that contain a majority age group, so that would serve as an additional dataset. Challenges here were finding text-heavy forums, and also a fairly long author caption (since comments tend to be shorter in most cases)

So far, here are the following age-marked reddit forums I have collected or looked at data from:
- Teens - `r/askteenboys`, `r/askteengirls`
- Twenties - `r/college`, `r/Adulting`, `r/LifeAfterSchool`
- Thirties+ - `r/Over30`, `r/Fitness30Plus`, `r/AskMenOver30`, `r/AskWomenOver30`

Data Pipeline for getting this data is in `scripts/`.

Data collection takes a while (API rate limits users), so final dataset size is TBD.

### Data Organization

Removed irrelevant symbols and white spaces. All existing punctuation is a factor in analysis, so I won't be removing that or changing the text. Data stays as is, in (Text, Age Category) pairs.

### Sharing Plan

For the blog dataset, there are a few examples of data in `blog_samples/`. I used the notebook `process_blog_data.ipynb` to sample data from the dataset and provide small examples. `csv_sample.csv` contains the information in it's simplest form that is going to be used, a CSV file.

It isn't readable, so I organized a nested directory holding age group and raw text under the template <ID>.txt. This is more complicated, but it is readable, which is why it is a good idea to share it in this way. 
  
A similar format has been followed for the reddit dataset that I am creating, located in `reddit_samples/`.

The groups are equally represented.


## 2nd Progress Report

### Analysis

Added scripts in `scripts` for syntactic and lexical analysis of features that I thought would be useful for my analysis, as well as feature engineering for a classification model. There is a file, `analyze_text.ipynb` that uses these modules to analyze a piece of sample text as proof of concept -- these features will be applied to the dataframe as a whole.

There is further data that I have gathered using scripts in `scripts/` and have csv files in a folder that is in my `.gitignore`. I have not preprocessed it or decided how to use it. (haven't had enough time).

And the license --

I have decided to use the MIT license for my repository because I think the project should be open-source, and I want to indirectly collaborate with others and get improvements to my code (there is definitely a ton of room for improvement). The MIT license is a permissive license that allows people to do pretty much whatever they want with my code, as long as they include a copy of the license.

## 3rd Progress Report

### Data

During the last progress report, there were 2 aspects to the data --

- The Blog Authorship Corpus 
    - This is a ready-to-use dataset, so apart from conversion and standard preprocessing to the use case, there is no need for further work.
- The Reddit dataset
    - This had some initial exploration, but was largely "in-the-works", meaning the scripts to fetch the data were there, but there was little planning around the actual structure which it was going to take.

Since the last progress report, there has been a ton of work on the data acquisition part of this. I made a couple of decisions that form the data's key aspects, as follows:

- The subreddits being used are `r/AskTeenBoys`and `r/AskTeenGirls` for teens, `r/LifeAfterSchool` and `r/College` for twenties, and `r/AskMenOver30` and `r/AskWomenOver30` for thirty plus.
- I couldn't form more accurate data for age groups, due to lack of widely available data for specific ages like twenties and thirties only, hence I found data groups that tends to be used by people who are closer to their 20s (as in `r/College`) and 30+ year olds (as in `r/AskMenOver30` and `r/AskWomenOver30`). There might be 18 year olds who use `r/College`, but I do think that it should be a seperate category anyway, since they more closely resemble 20-something year olds rather than early teenagers.
- I am using comments, not post text. This is because in a "ask an X year old", the main text might not be someone that age. Plus, links, news headlines, meme text etc. tend to be used as main text, which makes comments more distinctive of the category anyway.

I ran the data pipeline on all of the data and attempted to get over 10k data points for each subreddit -- so 20k per category. I anticipate noise and very short comments so I gathered 15k-20k within each category anyway to get a worst-case scenario fault tolerance of 50%. This took 60+ hours to run on my machine with 16GB DDR4 RAM, a large part of which was API rate limits. (I am very happy that I have a spare computer lying around)

I left the raw data in `reddit_data/`. Since this is new data that isn't technically mine, I looked into licensing and couldn't find much. Reddit doesn't specify licensing on data obtained through it's API, especially comments. I looked through forums and everyone else also seems to be confused. There also isn't a UUID linking comments to users in my data, so I went ahead and added it under the repo's MIT license.

### Analysis

Since the data is raw, I made sure to do some EDA, as I preprocessed the dataset, which can be found in `notebooks/dataset_extraction/process_reddit_dataset.ipynb`. I also saved the mostly final data in a pickled format in `data_samples/reddit_samples/all.pkl`.

There is more EDA in `notebooks/dataset_analysis`.

I also did update the analysis functions left in the feedback to use SpaCy instead of NLTK. I also am shifting to N-grams based on the feedback anyway, but I just wanted to close the loop on it. Plus, I might need it at some point later.