


import os
import re
import tempfile
import pandas as pd
import numpy as np

def build_dataset(rootdir="./atelier/RPZ-mariage"):
    # build dataset
    df = None
    with tempfile.NamedTemporaryFile(mode='w') as tmp:
        metaregx = re.compile(r"\[(?P<date>[^\[\]]+)\] (?P<streamer>[^\-]+) -")
        lineregx = re.compile(r"\[(?P<date>[^\[\]]+) UTC\] (?P<commentator>[^\:]+): (?P<comment>[^\n]+)")
        for root, _, files in os.walk('./'):
            if root == rootdir:
                for filename in [f for f in files if f.endswith('.txt')]:
                    # file metadata
                    obj = metaregx.match(filename)
                    if obj is None: continue
                    meta = '{date};{streamer}'.format(**obj.groupdict())
                    # format file content
                    with open(os.path.join(root, filename), mode='r') as txtfile:
                        for line in txtfile.readlines():
                            obj = lineregx.match(line)
                            if obj is None: continue
                            content = "{date};{commentator}".format(**obj.groupdict())
                            tmp.write("%s;%s\n" % (meta, content))
        df = pd.read_csv(tmp.name, sep=';', names=['cdate', 'streamer', 'ctimestamp', 'commentator'])
        df.cdate = df.cdate.astype(np.datetime64)
        df.ctimestamp = df.ctimestamp.astype(np.datetime64)
    return df

dataset = build_dataset()
