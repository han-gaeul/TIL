import h5py, numpy as np

matrix1 = np.random.random(size=(1000, 1000))
matrix2 = np.random.random(size=(10000, 100))

with h5py.File('test3.hdf5', 'w') as hdf:
    hdf.create_dataset('dataset1', data=matrix1)
    hdf.create_dataset('dataset2', data=matrix2)