import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os

if __name__ == '__main__':
    base_path = "./3_br_encaps"

    df = pd.read_csv(os.path.join(base_path, "2-1024-2-3-e.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df250 = pd.read_csv(os.path.join(base_path, "3-1024-2-3-250.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df500 = pd.read_csv(os.path.join(base_path, "3-1024-2-3-500.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df750 = pd.read_csv(os.path.join(base_path, "3-1024-2-3-750.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df1000 = pd.read_csv(os.path.join(base_path, "3-1024-2-3-1000.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])

        
    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(121)
    ax1.set_ylim(0,1.1)

    y1 = df['Delivery Rate Mean']
    y2 = df250['Delivery Rate Mean']
    y3 = df500['Delivery Rate Mean']
    y4 = df750['Delivery Rate Mean']
    y5 = df1000['Delivery Rate Mean']

    ax1.plot(df['Output Packet Rate'], y1, 'C1', label='End.B6.Encaps.SFC')
    ax1.plot(df['Output Packet Rate'], y2, 'C2', label='End.B6.Encaps with 250 rules')
    ax1.plot(df['Output Packet Rate'], y3, 'C3', label='End.B6.Encaps with 500 rules')
    ax1.plot(df['Output Packet Rate'], y4, 'C4', label='End.B6.Encaps with 750 rules')
    ax1.plot(df['Output Packet Rate'], y5, 'C5', label='End.B6.Encaps with 1000 rules')
 
    h1, l1 = ax1.get_legend_handles_labels()
    ax1.legend(h1, l1, loc='lower right', fontsize=8)

    ax1.set_xlabel('Output Packet Rate (bps)')
    ax1.set_ylabel('Delivery Rate')
    ax1.set_title('Packet Size 1024 Bits')
    ax1.grid(True)


    ## graph2 

    plt.show()



