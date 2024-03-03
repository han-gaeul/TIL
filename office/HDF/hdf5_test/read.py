import h5py, numpy as np

# with h5py.File('test2.hdf5', 'r') as hdf:
#     base_items = list(hdf.items())
#     print(base_items)
#     group_a = hdf.get('a')
#     group_a_items = list(group_a.items())
#     print(group_a_items)


# with h5py.File('test2.hdf5', 'r') as hdf:
#     ls = list(hdf.keys())
#     print(ls)
#     data = hdf.get('a')
#     a = np.array(data)
#     print(a.shape)


f = h5py.File('test2.hdf5', 'r')
keys_ls = list(f.keys())
values_ls = list(f.values())
items_ls = list(f.items())
print(keys_ls)
print(values_ls)
print(items_ls)