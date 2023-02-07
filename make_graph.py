import numpy as np
import pandas as pd
import matplotlib

if __name__ == '__main__':
    df = pd.read_csv('./b6_encaps', names=['Output Rate', 'Input Rate', 'Drop Rate Mean', 'Drop Rate Std'])
    print(df)
