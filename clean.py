import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


proj_dir = "/content/drive/Shared drives/2020 Python Project/"
proj_data_dir = proj_dir + "data/"
#proj_data_dir = proj_dir + "new_data/yelp-dataset/"

# load raw data
yelp_biz_attr = pd.read_csv(proj_data_dir + 'yelp_business_attributes.csv')
yelp_biz = pd.read_csv(proj_data_dir + 'yelp_business.csv')
yelp_biz_hour = pd.read_csv(proj_data_dir + 'yelp_business_hours.csv')
yelp_checkin = pd.read_csv(proj_data_dir + 'yelp_checkin.csv')
yelp_tip = pd.read_csv(proj_data_dir + 'yelp_tip.csv')
yelp_user = pd.read_csv(proj_data_dir + 'yelp_user.csv')
pd.merge
# a template of yelp review data
sk_review = random.sample(range(1, 5261669), 5261668 - 1000000)
# provide review's dtype schema for fast read
review_dtype = dict(
    review_id=np.str,
    user_id=np.str,
    business_id=np.str,
    stars=np.float16,
    text=np.str,
    useful=np.int16,
    funny=np.int16,
    cool=np.int16
)
date_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
yelp_review = pd.read_csv(proj_data_dir + 'yelp_review.csv',
                          skiprows=sk_review,
                          dtype=review_dtype,
                          parse_dates=[4,],
                          date_parser=date_parser)


#yelp_biz = pd.read_json(proj_data_dir + 'yelp_academic_dataset_business.json', orient=str)
import re
with open(proj_data_dir + 'yelp_academic_dataset_business.json') as f:
    a = f.read()


pd.DataFrame.from_dict(a)


#create a pivot table of review_count and state
review_by_state = pd.pivot_table(yelp_biz, "review_count", "state", "stars", np.sum, dropna=True, fill_value=0, margins=True)
# review_by_state = yelp_biz.groupby(["city", "stars"]).agg({"review_count": np.sum})
review_by_state.drop('All', inplace=True)
review_by_state.sort_values("All", inplace=True, ascending=False)
review_by_state.reset_index(inplace=True)
review_by_state.head(10).plot(kind='bar', x="state", y='All')

# trim all dataframes to only Nevada
NV_biz = yelp_biz[yelp_biz['state']=='NV']

all_category = yelp_biz.categories.str.split(';').explode()
unique_category = np.unique(all_category)
len(unique_category)

with open(proj_dir + 'categories.txt', 'r', encoding='utf-8') as f:
    c_lst = f.read()

c_lst = c_lst.replace('\n\xa0', '').replace('\xa0', ' ')
restaurant_category = eval(c_lst)
restaurant_category[:5]

yelp_biz = yelp_biz[yelp_biz['state'].notna()]
yelp_biz = yelp_biz[yelp_biz['latitude'].notna()]
yelp_biz = yelp_biz[yelp_biz['longitude'].notna()]
yelp_biz.isnull().sum()