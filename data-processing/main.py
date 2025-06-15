import pandas as pd
import numpy as np
import google.generativeai as genai
import re
import json

path = '/Users/songqinyue/Hack4Her/'

def load_csv():
    df = pd.read_csv(f'{path}data_csv_format/merged_file_unlabelled.csv')

    return df

def save_json(response):
    match = re.search(r'{.*}', response, re.DOTALL)
    if match:
        extracted_text = match.group().strip()
        print(extracted_text)
    response_json = json.loads(extracted_text)
    with open(f'{path}result/unlabelled_result.jsonl', 'a') as f:
        json.dump(response_json, f)
        f.write('\n')
    

def get_prompt(df, i):
    with open(f'{path}result/result.jsonl', 'r') as file:
        data = [json.loads(line) for line in file]

    input_desc = df['description'][i]
    input_2 = df['company_name'][i]
    input_3 = df['position_name'][i]
    input_4 = df['language'][i]
    input_5 = df['education'][i]
    input_6 = df['experience'][i]
    input_7 = df['responsibility'][i]
    input_8 = df['personality'][i]

    prompt = f'''You are a professional recruiter with 10 years of experience in analyzing job descriptions.
                 Here is an example {data}, you shoulf analyze the given data and learn from it and predict the women proportion based on data:
                 {input_2}, {input_3}, {input_4}, {input_5}, {input_6}, {input_7}, {input_8}
                 Please only return the women proportion.
            '''
    return prompt

genai.configure(api_key="AIzaSyClbkzV6WdLsoBz7UDvDSYiQJJSlERUqaY")
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

response = chat.send_message(get_prompt(load_csv(), 1))
print(response.text)