import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os

if __name__ == '__main__':
    base_path = "./3_br_encaps"

    df128 = pd.read_csv(os.path.join(base_path, "2-128-2-3.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df256 = pd.read_csv(os.path.join(base_path, "2-256-2-3.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df512 = pd.read_csv(os.path.join(base_path, "2-512-2-3.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df1024 = pd.read_csv(os.path.join(base_path, "2-1024-2-3.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])

        
    fig = plt.figure(figsize=(8, 4))
    ax1 = fig.add_subplot(121)
    ax1.set_ylim(0,1.1)

    y1 = df128['Delivery Rate Mean']
    y2 = df256['Delivery Rate Mean']
    y3 = df512['Delivery Rate Mean']
    y4 = df1024['Delivery Rate Mean']

    ax1.fill_between(df128['Output Packet Rate'], y1 + df128['Drop Rate Std'],  y1 - df128['Drop Rate Std'], alpha=0.2, color='C1')
    ax1.plot(df128['Output Packet Rate'], y1, 'C1', label='End.B6.Encaps DR Mean 128')
    ax1.fill_between(df256['Output Packet Rate'], y2 + df256['Drop Rate Std'],  y2 - df256['Drop Rate Std'], alpha=0.2, color='C2')
    ax1.plot(df256['Output Packet Rate'], y2, 'C2', label='End.B6.Encaps DR Mean 256')
    ax1.fill_between(df512['Output Packet Rate'], y3 + df512['Drop Rate Std'],  y3 - df512['Drop Rate Std'], alpha=0.2, color='C3')
    ax1.plot(df512['Output Packet Rate'], y3, 'C3', label='End.B6.Encaps DR Mean 512')
    ax1.fill_between(df1024['Output Packet Rate'], y4 + df1024['Drop Rate Std'],  y4 - df1024['Drop Rate Std'], alpha=0.2, color='C4')
    ax1.plot(df1024['Output Packet Rate'], y4, 'C4', label='End.B6.Encaps DR Mean 1024')
 
    h1, l1 = ax1.get_legend_handles_labels()
    ax1.legend(h1, l1, loc='lower right', fontsize=8)

    ax1.set_xlabel('Output Packet Rate (bps)')
    ax1.set_ylabel('Delivery Rate')
    ax1.set_title('End.B6.Encaps')
    ax1.grid(True)


    ## graph2 

    ax2 = fig.add_subplot(122)
    ax2.set_ylim(0,1.1)
    ndf128 = pd.read_csv(os.path.join(base_path, "2-128-2-3-e.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    ndf256 = pd.read_csv(os.path.join(base_path, "2-256-2-3-e.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    ndf512 = pd.read_csv(os.path.join(base_path, "2-512-2-3-e.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    ndf1024 = pd.read_csv(os.path.join(base_path, "2-1024-2-3-e.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])

        

    y1 = ndf128['Delivery Rate Mean']
    y2 = ndf256['Delivery Rate Mean']
    y3 = ndf512['Delivery Rate Mean']
    y4 = ndf1024['Delivery Rate Mean']

    ax2.plot(ndf128['Output Packet Rate'], y1, 'C5', label='End.B6.Encaps.SFC DR Mean 128')
    ax2.plot(ndf256['Output Packet Rate'], y2, 'C6', label='End.B6.Encaps.SFC DR Mean 256')
    ax2.plot(ndf512['Output Packet Rate'], y3, 'C7', label='End.B6.Encaps.SFC DR Mean 512')
    ax2.plot(ndf1024['Output Packet Rate'], y4, 'C8', label='End.B6.Encaps.SFC DR Mean 1024')
 
    h1, l1 = ax2.get_legend_handles_labels()
    ax2.legend(h1, l1, loc='lower right', fontsize=8)

    ax2.set_xlabel('Output Packet Rate (bps)')
    ax2.set_ylabel('Delivery Rate')
    ax2.set_title('End.B6.Encaps.SFC')
    ax2.grid(True)









    plt.show()



