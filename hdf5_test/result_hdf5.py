import h5py

# with h5py.File('result_replay_post_rms.hdf5', 'r') as rms:
#     keys_ls = list(rms.keys())
#     values_ls = list(rms.values())
#     items_ls = list(rms.items())
#     print(keys_ls)
#     print(values_ls)
#     print(items_ls)


# with h5py.File('result_replay_post_coil.hdf5', 'r') as coil:
#     keys_ls = list(coil.keys())
#     values_ls = list(coil.values())
#     items_ls = list(coil.items())
#     print(keys_ls)
#     print(values_ls)
#     print(items_ls)


with h5py.File('result_replay_post_efit.hdf5', 'r') as efit:
    keys_ls = list(efit.keys())
    values_ls = list(efit.values())
    items_ls = list(efit.items())
    print(keys_ls)
    print(values_ls)
    print(items_ls)