# tamppa_code_mem.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lines = []
func_names = []
only_functions_lines = []


def toDataframe(txtfile_path):
    """
    Parses stats from the .txt file and converts it to a pandas dataframe.
    """
    f = open(txtfile_path, "r")
    txt = f.read()

    for line in txt.split("\n"):
        # print(line)
        if line.startswith("Filename"):
            continue
        if line.startswith("Line"):
            continue
        if line.startswith("="):
            continue
        if line == "":
            continue
        data = [i.strip() for i in line.split()]

        # Fix def lines
        if len(data) <= 1:
            continue
        try:
            if data[5] == "@profile":
                temp_str = "".join(data[7:])
                fun_name = temp_str.split("(")[0]
                only_functions_data = [
                    data[0],
                    " ".join(data[1:3]),
                    " ".join(data[3:5]),
                    fun_name,
                ]
                only_functions_lines.append(only_functions_data)
                continue
        except IndexError:
            pass

        if data[1] == "def":
            # print(data[1:4])
            temp_str = "".join(data[2:4])
            func_names.append(temp_str.split("(")[0])
            data = [data[0], "", "", "", "", " ".join(data[1:3])]

        data = [data[0], " ".join(data[1:3]), " ".join(data[3:5]), data[-1]]
        lines.append(data)

    df = pd.DataFrame(
        lines, columns=["Line #", "Mem usage", "Increment", "Line Contents"]
    )

    only_functions_df = pd.DataFrame(
        only_functions_lines, columns=["Line #", "Mem usage", "Increment", "Function"]
    )
    only_functions_df["Function"] = func_names

    total_lines = len(df["Line #"])
    return only_functions_df, df

def writeFuncNamesTXT(only_functions_df):
    """
    Generates a text file of all the functions (names)
    """
    with open("func_names.txt", "w") as f:
        for item in func_names:
            f.write("%s\n" % item)

    only_functions_df.to_csv("function_wise_time_results.csv")

def toCSV(df):
    """
    Converts the extracted stats from the dataframe to .csv
    """
    split_idx = df[df["Line Contents"].str.startswith("def")].index

    index_collector_list = list()
    for i, idx in enumerate(split_idx):
        index_collector_list.append(idx)

    dataframes = []
    for idx, val in enumerate(index_collector_list):
        try:
            dataframes.append(df.iloc[val : index_collector_list[idx + 1]])
        except IndexError:
            dataframes.append(df.iloc[val:])

    df_names = []
    fn = iter(func_names)

    for i in dataframes:
        #print("===")
        i = i.iloc[2:]
        #print(i)
        i.to_csv(next(fn) + "_mem_.csv")


def decode():
    """
    Demonstrates how to use the results. Optional Plotting
    """
    fun = open("func_names.txt", "r")
    df_names = [f.split("\n")[0] + "_mem_.csv" for f in fun]
    # print(df_names)
    dfs = [pd.read_csv(d) for d in df_names]

    color_palette = ["b", "g", "r", "c", "m", "y", "k"]

    # fig_dim_x = int(total_lines/4)

    plt.figure(figsize=(15, 5), dpi=100)
    plt.grid()
    plt.title("Memory Profiling Results")
    plt.xlabel("Line #")
    plt.ylabel("Memory Usage (in MiB)")

    for idx, df in enumerate(dfs):
        # split 116 MiB to separate columns: 116 and MiB
        mbs_float = df["Mem usage"].str.split(' ',expand=True)[0].astype(np.float)
        plt.scatter(
            df["Line #"], mbs_float,
             color=color_palette[idx % len(color_palette)])
        plt.plot(
            df["Line #"], mbs_float, color_palette[idx % len(color_palette)])
        for i, label in enumerate(df["Line #"]):
            plt.annotate(label, (df["Line #"][i], mbs_float[i]))

    plt.show()


def mem_parse(txtfile_path):
    """
    Driver Function
    """
    only_functions_df, df = toDataframe(txtfile_path)
    toCSV(df)
    writeFuncNamesTXT(only_functions_df)
    decode()
