import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os

if __name__ == '__main__':
    base_path = "./3_br_encaps"

    df = pd.read_csv(os.path.join(base_path, "2-128-2-3-e.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df128 = pd.read_csv(os.path.join(base_path, "3-128-2-3-250.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df256 = pd.read_csv(os.path.join(base_path, "3-128-2-3-500.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df512 = pd.read_csv(os.path.join(base_path, "3-128-2-3-750.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df1024 = pd.read_csv(os.path.join(base_path, "3-128-2-3-1000.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])

        
    fig = plt.figure(figsize=(8, 8))
    ax1 = fig.add_subplot(221)
    ax1.set_ylim(0,1.1)

    y0 = df['Delivery Rate Mean']
    y1 = df128['Delivery Rate Mean']
    y2 = df256['Delivery Rate Mean']
    y3 = df512['Delivery Rate Mean']
    y4 = df1024['Delivery Rate Mean']

    ax1.plot(df['Output Packet Rate'], y0, 'C0', label='End.B6.Encaps.SFC')
    ax1.plot(df128['Output Packet Rate'], y1, 'C1', label='End.B6.Encaps with 250 rules')
    ax1.plot(df256['Output Packet Rate'], y2, 'C2', label='End.B6.Encaps with 500 rules')
    ax1.plot(df512['Output Packet Rate'], y3, 'C3', label='End.B6.Encaps with 750 rules')
    ax1.plot(df1024['Output Packet Rate'], y4, 'C4', label='End.B6.Encaps with 1000 rules')
 
    h1, l1 = ax1.get_legend_handles_labels()
    ax1.legend(h1, l1, loc='lower right', fontsize=8)

    ax1.set_xlabel('Output Packet Rate (bps)')
    ax1.set_ylabel('Delivery Rate')
    ax1.set_title('128 Bits')
    ax1.grid(True)


    ## graph2 


    df = pd.read_csv(os.path.join(base_path, "2-256-2-3-e.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df2 = pd.read_csv(os.path.join(base_path, "3-256-2-3-250.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df3 = pd.read_csv(os.path.join(base_path, "3-256-2-3-500.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df4 = pd.read_csv(os.path.join(base_path, "3-256-2-3-750.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df5 = pd.read_csv(os.path.join(base_path, "3-256-2-3-1000.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])

        
    ax1 = fig.add_subplot(222)
    ax1.set_ylim(0,1.1)

    y0 = df['Delivery Rate Mean']
    y1 = df2['Delivery Rate Mean']
    y2 = df3['Delivery Rate Mean']
    y3 = df4['Delivery Rate Mean']
    y4 = df5['Delivery Rate Mean']

    ax1.plot(df['Output Packet Rate'], y0, 'C0', label='End.B6.Encaps.SFC')
    ax1.plot(df2['Output Packet Rate'], y1, 'C1', label='End.B6.Encaps with 250 rules')
    ax1.plot(df3['Output Packet Rate'], y2, 'C2', label='End.B6.Encaps with 500 rules')
    ax1.plot(df4['Output Packet Rate'], y3, 'C3', label='End.B6.Encaps with 750 rules')
    ax1.plot(df5['Output Packet Rate'], y4, 'C4', label='End.B6.Encaps with 1000 rules')
 
    h1, l1 = ax1.get_legend_handles_labels()
    ax1.legend(h1, l1, loc='lower right', fontsize=8)

    ax1.set_xlabel('Output Packet Rate (bps)')
    ax1.set_ylabel('Delivery Rate')
    ax1.set_title('256 Bits')
    ax1.grid(True)


 
    df = pd.read_csv(os.path.join(base_path, "2-512-2-3-e.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df2= pd.read_csv(os.path.join(base_path, "3-512-2-3-250.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df3 = pd.read_csv(os.path.join(base_path, "3-512-2-3-500.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df4 = pd.read_csv(os.path.join(base_path, "3-512-2-3-750.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df5 = pd.read_csv(os.path.join(base_path, "3-512-2-3-1000.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])

        
    ax1 = fig.add_subplot(223)
    ax1.set_ylim(0,1.1)

    y0 = df['Delivery Rate Mean']
    y1 = df2['Delivery Rate Mean']
    y2 = df3['Delivery Rate Mean']
    y3 = df4['Delivery Rate Mean']
    y4 = df5['Delivery Rate Mean']

    ax1.plot(df['Output Packet Rate'], y0, 'C0', label='End.B6.Encaps.SFC')
    ax1.plot(df2['Output Packet Rate'], y1, 'C1', label='End.B6.Encaps with 250 rules')
    ax1.plot(df3['Output Packet Rate'], y2, 'C2', label='End.B6.Encaps with 500 rules')
    ax1.plot(df4['Output Packet Rate'], y3, 'C3', label='End.B6.Encaps with 750 rules')
    ax1.plot(df5['Output Packet Rate'], y4, 'C4', label='End.B6.Encaps with 1000 rules')
 
    h1, l1 = ax1.get_legend_handles_labels()
    ax1.legend(h1, l1, loc='lower right', fontsize=8)

    ax1.set_xlabel('Output Packet Rate (bps)')
    ax1.set_ylabel('Delivery Rate')
    ax1.set_title('512 Bits')
    ax1.grid(True)


    df = pd.read_csv(os.path.join(base_path, "2-1024-2-3-e.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df2 = pd.read_csv(os.path.join(base_path, "3-1024-2-3-250.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df3 = pd.read_csv(os.path.join(base_path, "3-1024-2-3-500.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df4 = pd.read_csv(os.path.join(base_path, "3-1024-2-3-750.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])
    df5 = pd.read_csv(os.path.join(base_path, "3-1024-2-3-1000.dr"), names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Delivery Rate Mean', 'Drop Rate Std'])

        
    ax1 = fig.add_subplot(224)
    ax1.set_ylim(0,1.1)

    y0 = df['Delivery Rate Mean']
    y1 = df2['Delivery Rate Mean']
    y2 = df3['Delivery Rate Mean']
    y3 = df4['Delivery Rate Mean']
    y4 = df5['Delivery Rate Mean']

    ax1.plot(df['Output Packet Rate'], y0, 'C0', label='End.B6.Encaps.SFC')
    ax1.plot(df2['Output Packet Rate'], y1, 'C1', label='End.B6.Encaps with 250 rules')
    ax1.plot(df3['Output Packet Rate'], y2, 'C2', label='End.B6.Encaps with 500 rules')
    ax1.plot(df4['Output Packet Rate'], y3, 'C3', label='End.B6.Encaps with 750 rules')
    ax1.plot(df5['Output Packet Rate'], y4, 'C4', label='End.B6.Encaps with 1000 rules')
 
    h1, l1 = ax1.get_legend_handles_labels()
    ax1.legend(h1, l1, loc='lower right', fontsize=8)

    ax1.set_xlabel('Output Packet Rate (bps)')
    ax1.set_ylabel('Delivery Rate')
    ax1.set_title('1024 Bits')
    ax1.grid(True)


 





 












    plt.tight_layout()
    plt.show()



