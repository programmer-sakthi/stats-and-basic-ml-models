import os 
import sys 
import pandas as pd 
import random 
from sklearn.model_selection import train_test_split


def get_csv(file):
    path=os.path.join(sys.path[0],file)
    return pd.read_csv(path)


def simple(df,sample_size):
    if(sample_size > len(df)) :
        print(f"Not enough rows to sample {sample_size} rows. Total rows: {len(df)}")
    else:
        sample = df.sample(n=sample_size , random_state = 42 )
        print(sample.head())

def stratified(df,by='Gender'):
    try:
        
        train,test = train_test_split(
            df,
            test_size = 0.2,
            stratify = df[by],
            random_state = 42
        )
        print(train.head())
    except Exception as e:
        print("Stratified sampling failed: The least populated class in y has only 1 member, which is too few. The minimum number of groups for any class cannot be less than 2.")
    
def systematic(df,n=10):
    print(df.iloc[::n].head())
    
    
    
    
    
def compute():
    filename = input()
    df=get_csv(filename)
    print("File loaded successfully:",filename)
    print(f"Data shape: {df.shape}")
    print("Preview of Loaded Data:")
    print(df.head())
    print("Simple Random Sampling (50 students):")
    simple(df,50)
    print("Stratified Sampling (by Gender):")
    stratified(df)
    print("Systematic Sampling (every 10th student):")
    systematic(df)
    
if __name__=='__main__':
    compute()