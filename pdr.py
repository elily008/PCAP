import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

if __name__ == '__main__':
    df128 = pd.read_csv('./b6_encaps_sfc/b6_encaps_sfc-128', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])
    df256 = pd.read_csv('./b6_encaps_sfc/b6_encaps_sfc-256', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])
    df512 = pd.read_csv('./b6_encaps_sfc/b6_encaps_sfc-512', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])
    df1024 = pd.read_csv('./b6_encaps_sfc/b6_encaps_sfc-1024', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])

    ndf128 = pd.read_csv('./b6_encaps/b6_encaps-128', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])
    ndf256 = pd.read_csv('./b6_encaps/b6_encaps-256', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])
    ndf512 = pd.read_csv('./b6_encaps/b6_encaps-512', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])

    ndf1024 = pd.read_csv('./b6_encaps/b6_encaps-1024', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])
        
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_ylim(0,100000000)

    y5 = ndf128['Input Bytes Rate']
    y6 = df128['Input Bytes Rate']
    y7 = ndf256['Input Bytes Rate']
    y8 = df256['Input Bytes Rate']
    y9 = ndf512['Input Bytes Rate']
    y10 = df512['Input Bytes Rate']
    y11 = ndf1024['Input Bytes Rate']
    y12 = df1024['Input Bytes Rate']


    ln5=ax1.plot(ndf128['Drop Rate Mean'], y5,'C4',label='End.B6.Encaps DR Mean(PS 128 Bit)')
    ln5=ax1.plot(df128['Drop Rate Mean'], y6,'C10',label='End.B6.Encaps.SFC DR Mean(PS 128 Bit)')
    ln5=ax1.plot(ndf256['Drop Rate Mean'], y7,'C4',label='End.B6.Encaps DR Mean(PS 128 Bit)')
    ln5=ax1.plot(df256['Drop Rate Mean'], y8,'C10',label='End.B6.Encaps.SFC DR Mean(PS 128 Bit)')
    ln5=ax1.plot(df512['Drop Rate Mean'], y9,'C10',label='End.B6.Encaps.SFC DR Mean(PS 128 Bit)')
    ln5=ax1.plot(ndf512['Drop Rate Mean'], y10,'C4',label='End.B6.Encaps DR Mean(PS 128 Bit)')
    ln6=ax1.plot(ndf1024['Drop Rate Mean'], y11, 'C9', label='End.B6.Encaps DR Mean(PS 1024 Bit)')
    ln6=ax1.plot(df1024['Drop Rate Mean'], y12, 'C11', label='End.B6.Encaps.SFC DR Mean(PS 1024 Bit)')
 
    h1, l1 = ax1.get_legend_handles_labels()
    ax1.legend(h1, l1, loc='lower right', fontsize=8)

    ax1.set_xlabel('Output Byte Rate (bps)')
    ax1.set_ylabel('Output packet Rate (pps)')
    ax1.grid(True)

    plt.show()



