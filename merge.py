import pandas as pd
import sys

def merge_csv(input_frequency_file, input_definition_file):
    # 读取两个CSV文件
    df_word_frequency = pd.read_csv(input_frequency_file)
    df_word_definition = pd.read_csv(input_definition_file)

    # 将Word列中的数据合并到已存在的CSV文件中，并去重
    merged_df = pd.concat([df_word_definition, df_word_frequency[['Word']]]).drop_duplicates(subset=['Word'])

    # 将结果保存回原有的CSV文件中
    merged_df.to_csv(input_definition_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_csv.py <input_frequency_file> <input_definition_file>")
        sys.exit(1)

    input_frequency_file = sys.argv[1]
    input_definition_file = sys.argv[2]

    merge_csv(input_frequency_file, input_definition_file)
