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
        
    ndf1024 = pd.read_csv('./b6_encaps/b6_encaps-1024', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])
    ndf512 = pd.read_csv('./b6_encaps/b6_encaps-512', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])
    ndf256 = pd.read_csv('./b6_encaps/b6_encaps-256', names=['Output Bytes Rate', 'Input Bytes Rate', 'Output Packet Rate', 'Input Packet Rate', 'Drop Rate Mean', 'Drop Rate Std'])

    fig = plt.figure(figsize=(8, 4))

    ax2 = fig.add_subplot(121)
    ax2.set_ylim(0,1.1)
    t = ndf128['Output Packet Rate']/1000
    y5 = ndf128['Drop Rate Mean']
    y6 = ndf256['Drop Rate Mean']
    y7 = ndf512['Drop Rate Mean']
    y8 = ndf1024['Drop Rate Mean']
    ln5=ax2.plot(t,y5,'C4',label='End.B6.Encaps DR Mean(128 Bytes)',marker='o', markersize=3)
    ln6=ax2.plot(t, y6, 'C5', label='End.B6.Encaps DR Mean(256 Bytes)', marker='o', markersize=3)
    ln6=ax2.plot(t, y7, 'C6', label='End.B6.Encaps DR Mean(512 Bytes)', marker='o', markersize=3)
    ln6=ax2.plot(t, y8, 'C9', label='End.B6.Encaps DR Mean(1024 Bytes)', marker='o', markersize=3)
    h2, l2 = ax2.get_legend_handles_labels()
    ax2.legend(h2, l2, loc='lower right', fontsize=8)
    ax2.set_xlabel('Send Packet Rate (kpps)')
    ax2.set_ylabel('Delivery Rate')
    ax2.grid(True)


    ax3 = fig.add_subplot(122)
    ax3.set_ylim(0,100000)
    ax3.set_ylim(0,1.1)
    t = df128['Output Packet Rate']/1000
    y5 = df128['Drop Rate Mean']
    y6 = df256['Drop Rate Mean']
    y7 = df512['Drop Rate Mean']
    y8 = df1024['Drop Rate Mean']
    ln5=ax3.plot(t,y5,'C4',label='End.B6.Encaps.SFC DR Mean(128 Bytes)',marker='o')
    ln6=ax3.plot(t, y6, 'C5', label='End.B6.Encaps.SFC DR Mean(256 Bytes)', marker='o')
    ln6=ax3.plot(t, y7, 'C6', label='End.B6.Encaps.SFC DR Mean(512 Bytes)', marker='o')
    ln6=ax3.plot(t, y8, 'C9', label='End.B6.Encaps.SFC DR Mean(1024 Bytes)', marker='o')
 
    h2, l2 = ax3.get_legend_handles_labels()
    ax3.legend(h2, l2, loc='lower right', fontsize=8)

    ax3.set_xlabel('Send Packet Rate(kpps)')
    ax3.set_ylabel('Delivery Rate')
    ax3.grid(True)

    #ax4 = fig.add_subplot(2,2,3)
    #ax4.set_title("End.B6.Encaps vs End.B6.Encaps.SFC")
   # ax4.set_ylim(0,1.1)
    #t = df128['Output Packet Rate']/1000
    #y5 = df128['Drop Rate Mean']
    #y6 = df1024['Drop Rate Mean']
    #y7 = ndf128['Drop Rate Mean']
    #y8 = ndf1024['Drop Rate Mean']
    #ln5=ax4.plot(t,y5,'C4',label='End.B6.Encaps.SFC DR Mean(128 Bytes)',marker='o')
    #ln6=ax4.plot(t, y6, 'C5', label='End.B6.Encaps.SFC DR Mean(1024 Bytes)', marker='o')
    #n6=ax4.plot(t, y7, 'C6', label='End.B6.Encaps DR Mean(128 Bytes)', marker='o')
    #ln6=ax4.plot(t, y8, 'C9', label='End.B6.Encaps DR Mean(1024 Bytes)', marker='o')
 
    #h2, l2 = ax4.get_legend_handles_labels()
    #ax4.legend(h2, l2, loc='lower right', fontsize=8)

    #ax4.set_xlabel('Input Packet Rate (kpps)')
    #ax4.set_ylabel('Drop Rate')
    #ax4.grid(True)




    plt.tight_layout()
    plt.show()



