import sys
import pandas as pd

def sort_and_remove_duplicates(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 按第一列数据排序
    df.sort_values(by=df.columns[0], inplace=True)

    # 去除重复行
    df.drop_duplicates(inplace=True)

    # 将排序后的DataFrame写回原文件
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("请提供正确的文件路径作为参数")
        sys.exit(1)

    file_path = sys.argv[1]
    sort_and_remove_duplicates(file_path)
