import itertools
import pandas as pd
import warnings


def find_unique_column_combinations(input_df: pd.DataFrame) -> pd.DataFrame:
    table_cardinality = len(input_df)
    columns = list(input_df)

    for i in range(1, len(columns) + 1):
        # Всевозможные сочетания столбцов из n по k, где k = i
        k_combinations_from_set_of_attributes = list(itertools.combinations(columns, i))

        for combination in k_combinations_from_set_of_attributes:
            # Фильтрация таблицы по комбинации столбцов
            slicer = input_df.filter(items=combination)
            slicer_cardinality = len(slicer.drop_duplicates())

            # Если кардинальность комбинации столбцов равна кардинальности всей таблицы, то такая комбинация
            # уникально описывает все записи
            if slicer_cardinality == table_cardinality:
                unique_column_combinations = pd.DataFrame(slicer.columns, columns=["Признаки"])
                return unique_column_combinations

    raise Exception("No unique columns found")


# Приведение dataframe к формату csv
def serialize_df_to_csv(df: pd.DataFrame) -> None:
    df.to_csv("results.csv")


# Выполнение кода
def main(input_: str) -> None:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        df = pd.read_json(input_)

    df = find_unique_column_combinations(df)
    serialize_df_to_csv(df)


if __name__ == "__main__":
    main('[{"a": 1, "b": 2}, {"a": 1, "b": 3}]')
