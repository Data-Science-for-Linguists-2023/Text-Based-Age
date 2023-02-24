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

