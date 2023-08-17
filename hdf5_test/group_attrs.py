import h5py

file = h5py.File('test.hdf5', 'w')

# file.create_group('a')
# file['a'].create_group('d')

# file.create_group('b')
# file['b'].create_group('c')

n = file.create_group('n')
nn = n.create_group('nn')
print(file.keys())
print(n.keys())
print(nn.keys())

nn.attrs['message'] = 'test'
nn.attrs['date'] = '230801'
print(nn.attrs['message'])
print(nn.attrs.keys())

nnn = n.create_group('nnn')

nnn.attrs['message'] = 'second_test'
print(nnn.attrs['message'])