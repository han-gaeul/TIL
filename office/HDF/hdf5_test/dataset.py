import h5py

# file = h5py.File('test2.hdf5', 'w')

# float_list = ['0.4', '0.3', '1.4', '5.8', '3.2']
# int_list = ['2', '4', '8', '7', '1']

# a = file.create_group('a')

# a.create_dataset('INT_DATA', data=int_list)
# a.create_dataset('FLOAT_DATA', data=float_list)


with h5py.File('test2.hdf5', 'r') as file:
    a_group = file['a']
    int_dataset = a_group['INT_DATA']
    int_list = list(int_dataset)
    print(int_list)
    float_dataset = a_group['FLOAT_DATA']
    float_list = list(float_dataset)
    print(float_list)

# [b'2', b'4', b'8', b'7', b'1']
# [b'0.4', b'0.3', b'1.4', b'5.8', b'3.2']