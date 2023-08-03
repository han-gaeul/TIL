import h5py

# with h5py.File('20221025RMS.hdf5', 'r') as rms:
#     ls = list(rms.keys())
#     print(ls)
#     data = rms.get('32769')
#     dataset1 = np.array(data)
#     print(dataset1.shape)
#     print(dataset1)
#     print(dataset1[0:10])

with h5py.File('20221025RMS.hdf5', 'r') as rms:
    rms_group = rms['32769']
    rms_group2 = rms_group['11H43M18S.846247']
    print(rms_group2)
    rms_dataset = rms_group2['HDS_HCS_R_P21L']
    print(rms_dataset)
    rms_ls = rms_dataset[()]
    print(rms_ls)
    # 1.9505000114440918


# file_path = input('HDF5 파일 경로를 입력하세요. : ')
# with h5py.File(file_path, 'r') as rms:
#     group_idx = int(input('상위 그룹 인덱스를 입력하세요. (0부터 시작) : '))
#     subgroup_idx = int(input('하위 그룹 인덱스를 입력하세요. (0부터 시작) : '))
#     dataset_idx = int(input('데이터셋 인덱스를 입력하세요. (0부터 시작) : '))

#     group_names = list(rms.keys())
#     target_group_name = group_names[group_idx]
#     group = rms[target_group_name]

#     subgroup_names = list(group.keys())
#     target_subgroup_name = subgroup_names[subgroup_idx]
#     subgroup = group[target_subgroup_name]

#     dataset_names = list(subgroup.keys())
#     target_dataset_name = dataset_names[dataset_idx]
#     dataset = subgroup[target_dataset_name]

#     print(target_group_name)
#     print(target_subgroup_name)
#     print(target_dataset_name)
#     print(dataset[()])


# HDF5 파일 열기
file_path = input("HDF5 파일 경로를 입력하세요: ")
with h5py.File(file_path, 'r') as hdf:
    num_groups = len(hdf.keys())
    target_group_index = int(input(f"상위 그룹 인덱스를 입력하세요 (0부터 {num_groups-1}까지): "))
    group = list(hdf.values())[target_group_index]

    num_subgroups_per_group = len(group.keys())
    target_subgroup_index = int(input(f"하위 그룹 인덱스를 입력하세요 (0부터 {num_subgroups_per_group-1}까지): "))
    subgroup = list(group.values())[target_subgroup_index]

    if isinstance(subgroup, h5py.Group):
        num_datasets_per_subgroup = len(subgroup.keys())
        target_dataset_index = int(input(f"데이터셋 인덱스를 입력하세요 (0부터 {num_datasets_per_subgroup-1}까지): "))
        
        target_dataset_name = list(subgroup.keys())[target_dataset_index]
        dataset = subgroup[target_dataset_name]

        print("Top Group Name:", group.name)
        print("Subgroup Name:", subgroup.name)
        print("Dataset Name:", target_dataset_name)
        print("Dataset Contents:", dataset[()])
    else:
        print("Top Group Name:", group.name)
        print("Dataset Name:", subgroup.name)
        print("Dataset Contents:", subgroup[()])