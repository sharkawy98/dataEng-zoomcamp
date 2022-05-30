import pandas as pd
import sys


dic = {
    'first_name' : sys.argv[1].capitalize(),
    'last_name' : sys.argv[2].capitalize(),
    'age' : sys.argv[3]
}

df = pd.DataFrame.from_dict([dic])

print(df)
