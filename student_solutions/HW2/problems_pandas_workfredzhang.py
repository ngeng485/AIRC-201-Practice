import pandas as pd
from typing import List, Tuple, Any

def get_dataset_shape(df: pd.DataFrame) -> Tuple[int, int]:
    """
    Returns the shape of the dataframe as a tuple of (number of rows, number of columns).
    """
    return df.shape

def get_column_names(df: pd.DataFrame) -> List[str]:
    """
    Returns a list of all column names in the given dataframe.
    """
    return list(df.columns)

def get_summary_statistics(df: pd.DataFrame, column_name: str) -> pd.Series:
    """
    Returns the summary statistics (using .describe()) for the specified column in the dataframe.
    """
    return df[column_name].describe()

def get_nth_row(df: pd.DataFrame, n: int) -> pd.Series:
    """
    Returns the n-th row of the dataframe, using standard integer-based indexing.
    """
    return df.iloc[n]

def filter_by_drink_category(df: pd.DataFrame, category: str) -> pd.DataFrame:
    """
    Returns a dataframe containing only the rows where the "drink_category" matches the given category string.
    """
    return df[df['drink_category'] == category]

def get_high_spenders(df: pd.DataFrame, min_spend: float) -> pd.DataFrame:
    """
    Returns a dataframe containing only the rows where the "total_spend" is STRICTLY GREATER THAN min_spend.
    """
    return df[df['total_spend'] > min_spend]

def get_mobile_rewards_members(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a dataframe containing only the rows where the "order_channel" is 'Mobile App' 
    AND they are a rewards member ('is_rewards_member' is True).
    """
    return df[(df['order_channel'] == 'Mobile App') & (df['is_rewards_member'] == True)]

def get_specific_regions(df: pd.DataFrame, regions: List[str]) -> pd.DataFrame:
    """
    Returns a dataframe containing only the rows where the "region" is one of the strings in the given list of regions.
    """
    return df[df['region'].isin(regions)]

