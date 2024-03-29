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
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/738e639c-1fbf-4e16-beb0-a223831011e8/download/public_150k_plus_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/a7fa66f4-fd2e-433c-8ef9-59780ef60ae5/download/public_up_to_150k_1_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/7d2308a8-0ac1-48a8-b21b-f9eb373ac417/download/public_up_to_150k_2_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/5158aae1-066d-4d01-a226-e44ecc9bdda7/download/public_up_to_150k_3_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/d888bab1-da5b-46f2-bed2-a052d48af246/download/public_up_to_150k_4_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/ee12d751-2bb4-4343-8330-32311ae4e7c7/download/public_up_to_150k_5_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/27b874d9-a059-4296-bb74-374294c48616/download/public_up_to_150k_6_230930.csv')        
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/434efae0-016a-48da-92dc-c6f113d827c1/download/public_up_to_150k_7_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/4fc8e993-c3b9-4eb2-b9bb-dfbde9b1fb6f/download/public_up_to_150k_8_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/7f9c6867-2b55-472e-a4f3-fd0f5f27f790/download/public_up_to_150k_9_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/a8f2c8b2-facb-4e97-ad5f-7c8736c8b4b6/download/public_up_to_150k_10_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/6f9787a3-afd6-45b2-b78e-ad0dc097c1c3/download/public_up_to_150k_11_230930.csv')
    links.append('8aa276e2-6cab-4f86-aca4-a7dde42adf24/resource/b6528428-fbd9-4ca6-ae08-9e3416f8ee7f/download/public_up_to_150k_12_230930.csv')
    # We make another list by adding the root to each of our links.
    full_links=[]
    for link in links:
        full_links.append(root+link)
    # We return the dataframe obtained by concatenating the dataframes given by these CSV files.
    return merge_csv_from_links(full_links)


