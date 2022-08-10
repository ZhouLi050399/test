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
    files = tf.data.Dataset.list_files(f"{hdfs_path}/*.*")
    path_list = [item.decode() for item in list(files.as_numpy_iterator())]
    mark_1 = []
    mark_2 = []
    mark_3 = []
    mark_4 = []
    mark_5 = []
    cpi = []
    unemployment = []
    for file in path_list:
        with tf.io.gfile.GFile(file) as f:
            while True:
                line = f.readline()
                if not line: break
                features = line.split('|')
                print(features)
                #mark_1.append(float(features[4].strip()))
                #mark_2.append(float(features[5].strip()))
                #mark_3.append(float(features[6].strip()))
                #mark_4.append(float(features[7].strip()))
                #mark_5.append(float(features[8].strip()))
                #cpi.append(float(features[9].strip()))
                #unemployment.append(float(features[10].strip()))
    #X = np.stack((mark_1, mark_2, mark_3, mark_4, mark_5, cpi, unemployment), axis=1)
    #print(X.shape)
    #print(np.mean(np.array(mark_1)))
    #print(np.mean(np.array(mark_2)))
    #print(np.mean(np.array(mark_3)))
    #print(np.mean(np.array(mark_4)))
    #print(np.mean(np.array(mark_5)))
    #print(np.mean(np.array(cpi)))
    #print(np.mean(np.array(unemployment)))
if "__main__" == main():
    main()