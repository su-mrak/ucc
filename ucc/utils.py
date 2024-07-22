import itertools
import pandas as pd


def read_dataframe_from_json(path: str) -> pd.DataFrame:
    df = pd.read_json(path)
    return df


def find_unique_column_combinations(input_df: pd.DataFrame) -> pd.DataFrame:
    table_cardinality = len(input_df)
    columns = list(input_df)

    for i in range(1, len(columns) + 1):
        k_combinations_from_set_of_attributes = list(itertools.combinations(columns, i))

        for combination in k_combinations_from_set_of_attributes:
            slicer = df.filter(items=combination)
            slicer_cardinality = len(slicer.drop_duplicates())

            if slicer_cardinality == table_cardinality:
                unique_column_combinations = pd.DataFrame(slicer.columns, columns=['Признаки'])
                return unique_column_combinations


def serialize_df_to_csv(df: pd.DataFrame):
    df.to_csv("results.csv")


