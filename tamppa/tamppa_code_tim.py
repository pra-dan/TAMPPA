# tamppa_code_tim.py
import pandas as pd
import matplotlib.pyplot as plt

# globals
lines = []
again_func_names = []

def toDataframe(txtfile_path):
    """
    Parses stats from the .txt file and converts it to a pandas dataframe.
    """
    f = open(txtfile_path, "r")
    txt = f.read()

    for line in txt.split('\n'):
        #print(line)
        if line.startswith('Wrote'): continue
        if line.startswith('Timer'): continue

        if line.startswith('Total'): continue
        if line.startswith('File'): continue
        if line.startswith('Function'): continue

        if line.startswith('Line'): continue
        if line.startswith('='): continue
        if line == '': continue
        data = [i.strip() for i in line.split()]

        #Fix def lines
        if len(data) <= 1: continue

        if data[1] == '@profile': continue

        if data[1] == 'def':
            data = [data[0],'','','','',' '.join(data[1:4])]
            #print(data)
            temp_str = ''.join(data[5])
            #print(temp_str)
            temp_str = temp_str.split(' ')[1]
            again_func_names.append(temp_str.split('(')[0])

        data = [data[0], data[1], data[2], data[3],data[4], ''.join(data[5:])]
        #print(f"{len(data)}\t{data}")
        lines.append(data)

    df = pd.DataFrame(lines, columns=['Line #', 'Hits','Total Time', 'Time Per Hit', '% Time', 'Line Contents'])
    return df, again_func_names

def writeFuncNamesTXT(again_func_names):
    """
    Generates a text file of all the functions (names)
    """
    with open("again_func_names.txt", "w") as f:
        for item in again_func_names:
            f.write("%s\n" % item)

def toCSV(df):
    """
    Converts the extracted stats from the dataframe to .csv
    """
    split_idx = df[df['Line Contents'].str.startswith('def')].index

    index_collector_list = list()
    for i, idx in enumerate(split_idx):
        index_collector_list.append(idx)

    dataframes = []
    for idx, val in enumerate(index_collector_list):
        try:
            dataframes.append(df.iloc[val:index_collector_list[idx+1]])
        except IndexError:
            dataframes.append(df.iloc[val:])

    fn = iter(again_func_names)

    for i in dataframes:
        #print("===")
        i = i.iloc[1:]
        #print(i)
        i.to_csv(next(fn)+'_tim_.csv')

def decode():
    """
    Demonstrates how to use the results. Optional Plotting
    """
    fun = open("again_func_names.txt",'r')
    df_names = [f.split('\n')[0]+'_tim_.csv' for f in fun]
    dfs = [pd.read_csv(d) for d in df_names]

    # Data to plot
    labels = []
    sizes = []
    colors = []

    color_palette_2 = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    for idx, d in enumerate(dfs):
        clr = color_palette_2[idx%len(color_palette_2)]
        for c in list(d.loc[:,'% Time']):
            sizes.append(c)
        for l in d['Line #']:
            colors.append(clr)
            labels.append(l)
            #sizes.append()

    # Plot
    plt.pie(x=sizes, labels=labels, colors=colors,
        startangle=90,pctdistance=1.125,
        wedgeprops={"edgecolor":"k",'linewidth': 1},
        textprops={'fontsize': 8})
    #plt.legend(labels, bbox_to_anchor=(0,0) loc="best")

    plt.axis('equal')
    plt.rcParams['font.size'] = 10
    fig = plt.gcf()
    fig.set_size_inches(10,10)
    fig.show()

def tim_parse(txtfile_path):
    """
    Driver Function
    """
    df, again_func_names = toDataframe(txtfile_path)
    toCSV(df)
    writeFuncNamesTXT(again_func_names)
    decode()
