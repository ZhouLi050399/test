import argparse
import tensorflow as tf
import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_hdfs1', type=str)
    args = parser.parse_args()
    hdfs_path = args.input_hdfs1
    print(hdfs_path)
    files = tf.data.Dataset.list_files(f"{hdfs_path}/*")
    path_list = [item.decode() for item in list(files.as_numpy_iterator())]
    print(path_list)
    id = []
    sl = []
    pl = []
    for file in path_list:
        with tf.io.gfile.GFile(file) as f:
            while True:
                line = f.readline()
                if not line: break
                features = line.split('|')
                print(features)
                id.append(float(features[0].strip()))
                sl.append(float(features[1].strip()))
                pl.append(float(features[3].strip()))
    X = np.stack((id, sl, pl), axis=1)
    print(X.shape)
    print(sl)
    print(pl)
    print(X)
if "__main__" == main():
    main()