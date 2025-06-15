import pickle
import pandas as pd
from nltk import FreqDist

with open('data_pickle_format/synethetic_vacancies_final.pickle', 'rb') as f:
    df = pickle.load(f)    

counts_1_4 = df.loc[df['women_proportion'] < 0.25]

print(counts_1_4)

# positive_freq_dic=FreqDist(word_frequency_counts['pos'])
# negative_freq_dic=FreqDist(word_frequency_counts['neg'])

# display( positive_freq_dic, negative_freq_dic)