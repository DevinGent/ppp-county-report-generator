# This script gathers data from the U.S. Small Business Administration for analysis.

import pandas as pd

def merge_csv_from_links(url_list):
    """Takes a list of urls linking to CSV files and constructs a dataframe by
    concatenating them. Please ensure that each CSV has the same set of columns first."""
    # We will create a list of dataframes representing individual CSVs and then concatenate them all at once.
    df_list=[]
    # For each url we will load the CSV as a dataframe and add it to our df_list.
    for link in url_list:
        df_list.append(pd.read_csv(link,
                                   encoding='ISO-8859-1',
                                   engine='python',
                                   on_bad_lines='warn'))
    # If only one CSV/link (as a list) was given as the input of this function, then we return
    # that dataframe with duplicate rows removed and the index reset.
    if len(df_list)==1:
        return df_list[0].drop_duplicates().reset_index(drop=True)
    # In all other cases we concatenate the CVs in the list, drop duplicates, reset the index, and return the combined dataframe.
    else:
        full_df=pd.concat(df_list,axis=0,ignore_index=True)    
        full_df.drop_duplicates(inplace=True)
        full_df.reset_index(drop=True,inplace=True)
        return full_df

def sba_7a_2020_to_present():
    root='https://data.sba.gov/dataset/'
    link='0ff8e8e9-b967-4f4e-987c-6ac78c575087/resource/3e4231a6-fd69-409f-ac4a-62b7b7592d84/download/foia-7afy2020-present-asof-231231.csv'
    return merge_csv_from_links([root+link])



def sba_7a_2010_to_present():
    root='https://data.sba.gov/dataset/'
    link_2010='0ff8e8e9-b967-4f4e-987c-6ac78c575087/resource/40e6d1ef-5853-4bf6-866d-79d91722e2e1/download/foia-7afy2010-fy2019-asof-231231.csv'
    link_2020='0ff8e8e9-b967-4f4e-987c-6ac78c575087/resource/3e4231a6-fd69-409f-ac4a-62b7b7592d84/download/foia-7afy2020-present-asof-231231.csv'
    links=[root+link_2010,root+link_2020]
    return merge_csv_from_links(links)

def ppp():
    """Loads U.S. PPP loan data from https://data.sba.gov/dataset/ppp-foia consisting of over 10 million recorded loans."""
    # We store the common root of the various links as a variable, then store the individual links in a list.
    root='https://data.sba.gov/dataset/'
    links=[]
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/c1275a03-c25c-488a-bd95-403c4b2fa036/download/public_150k_plus_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/cff06664-1f75-4969-ab3d-6fa7d6b4c41e/download/public_up_to_150k_1_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/1e6b6629-a5aa-46e6-a442-6e67366d2362/download/public_up_to_150k_2_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/644c304a-f5ad-4cfa-b128-fe2cbcb7b26e/download/public_up_to_150k_3_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/98af633d-eb1b-4d4b-995d-330962e6c38d/download/public_up_to_150k_4_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/3b407e04-f269-47a0-a5fe-661d1a08a76c/download/public_up_to_150k_5_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/7b7b5b58-9645-4b88-a675-a8a825e77076/download/public_up_to_150k_6_240930.csv')        
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/dabdddb5-1807-44f6-97c6-d624a5372525/download/public_up_to_150k_7_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/1fc6ddc4-ccb0-49d4-b632-0749e3292e57/download/public_up_to_150k_8_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/e9f2c718-b95e-47da-8f3e-17154aab1c86/download/public_up_to_150k_9_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/d9972f0d-c377-46ac-8637-a5c1265377c8/download/public_up_to_150k_10_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/8db19ddc-f036-40df-89f9-d0d309aa58b5/download/public_up_to_150k_11_240930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/7e4f672f-d163-4735-a5ec-f23afa2835db/download/public_up_to_150k_12_240930.csv')
    # We make another list by adding the root to each of our links.
    full_links=[]
    for link in links:
        full_links.append(root+link)
    # We return the dataframe obtained by concatenating the dataframes given by these CSV files.
    return merge_csv_from_links(full_links)




