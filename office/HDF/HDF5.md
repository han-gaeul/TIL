## 🗃HDF5

## 개요

---

- 계층적으로 구조화된 다차원 배열 데이터를 저장하기 위해 HDF Group에 의해 만들어진 파일 형식
- 다양한 데이터 타입을 제공하고 효율적인 파일 입출, 대용량의 복잡한 데이터를 저장하고 관리하기 위해 설계
- 모든 object는 각자의 name이 있고, 계층적인 구조로 관리

![img.jpg](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\img.jpg)

- 각 폴더는 Group, 파일의 역할을 하는 것은 Dataset
  - Dataset은 HDF5 파일에 담겨있는 데이터

## 특징

---

- 복잡한 데이터 객체 및 매우 다양한 메타데이터를 표현할 수 있음
- 데이터의 사이즈 및 개수에 제한이 없는 파일 형식
- 다양한 언어로 된 라이브러리 지원(C/C++/Java/Python)

## 용어 정리

---

- **Group** : object(객체) 모음
- **Dataset** : 속성 및 기타 메타데이터를 가진 데이터 요소의 다차원 배열
- Dataspace : 다차원 배열의 차수에 대한 설명
- Datatype : 저장 레이아웃을 비트 패턴으로 포함하는 데이터 요소의 특정 클래스에 대한 설명
- Attribute : 그룹, 데이터 집합 또는 명명된 데이터 유형과 관련된 명명된 데이터 값
- Property List : 라이브러리의 매개변수 제어 옵션 모음
- Link : 객체가 연결 되는 방식

# 📃사용 방법

## Install

---

```bash
pip install h5py
```

## Import / Create

---

```python
import h5py

hdf5_file = h5py.File('test.hdf5', 'w')
```

- mode
  - `r` : 읽기 전용. 파일이 있어야 함
  - `r+` : 읽고 쓰기. 파일이 있어야 함
  - `w` : 파일 쓰기. 파일이 있는 경우 덮어쓰기
  - `w-`, `x` : 파일 쓰기. 파일이 있는 경우 실패
  - `a` : 파일이 있는 경우 읽기/쓰기. 파일이 없다면 만들기(기본값)

## 데이터 모델

---

### Group

- 컨테이너 역할. 파일 시스템 디렉터리와 유사
- 그룹에는 0개 이상의 개체가 포함되며 모든 개체는 적어도 하나의 그룹의 구성원
- 항상 루트 그룹(`/`)이 존재하며, 파일 객체는 루트 그룹으로 취급할 수 있음

![group1.png](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\group1.png)

- 예시
  
  ```python
  top_group_a = hdf5_file.create_group('top_group_A')
  
  # 여러 개의 그룹을 동시 생성
  hdf5_file.create_group('top_group_B'/'top_group_C')
  
  # 하위 group 생성
  subgroup_a = top_group_A.create_group('subgroup_a')
  hdf5_file['top_group_B'].create_group('subgroup_c')
  subgroup_d = top_group_C.create_group('subgroup_d/subgroup_f')
  ```

![Screenshot 2023-08-03 at 14.33.01.JPG](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\Screenshot%202023-08-03%20at%2014.33.01.JPG.jpg)

![Screenshot 2023-08-03 at 14.33.52.JPG](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\Screenshot%202023-08-03%20at%2014.33.52.JPG.jpg)

- 그룹 조회
  
  ```python
  print(hdf5_file.keys()) # ['top_group_A', 'top_group_B', 'top_group_C']
  print(top_group_A.keys()) # ['subgroup_a']
  ```
  
  > 생성된 group은 python dictionary와 같은 방식으로 관리
  > 각 group의 name이 key가 되어 name을 이용해 각 group에 접근
  > dictionary의 여러 기능을 이용할 수 있음
  
  - `[key]`, `name`
  
  ```python
  hdf5_file['a'] # [key]
  print(hdf5_file['a'].name) # 'a'
  ```
  
  - `keys()`, `values()`, `items()`
  
  ```python
  print(list(hdf5_file.keys)) # ['a']
  print(list(hdf5_file.values()) # [<HDF5 group "/a" (2 members)>]
  print(list(hdf5_file.items()) # [('a', <HDF5 group "/a" (2 members)>)]
  ```

![Screenshot 2023-08-03 at 14.32.12.JPG](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\Screenshot%202023-08-03%20at%2014.32.12.JPG.jpg)

### Dataset

- 동일한 데이터 타입을 갖는 수치로 이루어진 배열을 저장
- 실제 데이터 값들을 구조화하여 포함

```python
dataset = group.create_dataset(name, shape=None, dtype=None, data=None, ...)
```

> 첫 번째 인자로 name이 들어가고, data와 dtype 등을 지정할 수 있음 `*ndarray`로 데이터를 지정할 때는 shape과 dtype을 지정할 필요 없음*
> 생성된 dataset은 name으로 접근 가능

- `name`, `shape`, `dtype`
  
  ```python
  hdf_file = h5py.File('test2.hdf5', 'w')
  
  float_list = ['0.4', '0.3', '1.4', '5.8', '3.2']
  int_list = ['2', '4', '8', '7', '1']
  
  a = hdf_file .create_group('a')
  
  a.create_dataset('INT_DATA', data=int_list)
  a.create_dataset('FLOAT_DATA', data=float_list)
  
  with h5py.File('test2.hdf5', 'r') as hdf_file:
      a_group = hdf_file['a']
      int_dataset = a_group['INT_DATA']
      int_list = list(int_dataset)
      print(int_dataset.name)
      print(int_list)
      float_dataset = a_group['FLOAT_DATA']
      float_list = list(float_dataset)
      print(float_dataset.name)
      print(float_list)
  
  # 결과
  # /a/INT_DATA
  # [b'2', b'4', b'8', b'7', b'1']
  # /a/FLOAT_DATA
  # [b'0.4', b'0.3', b'1.4', b'5.8', b'3.2']
  ```

![Screenshot 2023-08-03 at 14.25.31.JPG](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\Screenshot%202023-08-03%20at%2014.25.44.JPG.jpg)

![Screenshot 2023-08-03 at 14.25.44.JPG](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\Screenshot%202023-08-03%20at%2014.25.31.JPG.jpg)

- Datatype
  
  - 단일 데이터 요소의 자료형을 나타냄
  
  - 사전에 정의된 타입
    
    | 타입                | 설명                                                  |
    | ----------------- | --------------------------------------------------- |
    | Standard datatype | 모든 플랫폼에서 동일하고 실제 HDF 파일을 열어서 볼 수 있는 데이터에 대한 타입으로 사용 |
    | Native datatype   | 메모리 연산(읽기 및 쓰기)을 단순화 하기 위해 사용되며, 플랫폼에 따라 다를 수 있음    |
  
  - 파생 타입
    
    | 타입                         | 설명                            |
    | -------------------------- | ----------------------------- |
    | Integer                    | 정수                            |
    | Float                      | 실수                            |
    | Character                  | 1바이트 문자 인코딩 배열                |
    | Variable-length            | 데이터 요소의 가변 길이 1차원 배열          |
    | Reference                  | HDF5 파일 내의 다른 객체 또는 영역에 대한 참조 |
    | Enumeration                | 문자열 형식의 기호 이름이 있는 값 목록        |
    | Opaque                     | 불투명 유형. 해석되지 않는 데이터           |
    | Compound                   | 일련의 데이터 유형에 대한 데이터 유형         |
    | User-defined               | 사용자 정의                        |
    | 예) 13비트 정수 또는 고정/가변 길이 문자열 |                               |

### Attribute

- 객체를 문서화하는 데 사용
- 그룹이나 dataset을 부연 설명하는 사용자 정의 메타데이터를 속성으로 지정할 수 있음
- 그룹이나 dataset 객체의 `attrs`로 접근할 수 있으며 dictionary 타입처럼 사용 가능

```python
hdf_file = h5py.File('test.hdf5', 'w')

top_group_A = hdf_file.create_group('top_group_A')
subgroup_a = top_group_A.create_group('subgroup_a')

subgroup_a.attrs['message'] = 'test'
subgroup_a.attrs['date'] = '230801'
print('subgroup_a.attrs["message"] : ', subgroup_a.attrs['message'])
print('subgroup_a.attrs.keys : ', subgroup_a.attrs.keys())

subgroup_b = top_group_A.create_group('subgroup_b')

subgroup_b.attrs['message'] = 'second_test'
print('subgroup_b.attrs["message"] : ', subgroup_b.attrs['message'])

# 결과
# subgroup_a.attrs["message"] :  test
# subgroup_a.attrs.keys :  <KeysViewHDF5 ['date', 'message']>
# subgroup_b.attrs["message"] :  second_test
```

![Screenshot 2023-08-08 at 14.22.53.JPG](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\Screenshot%202023-08-08%20at%2014.22.53.JPG.jpg)

![Screenshot 2023-08-08 at 15.21.34.JPG](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\Screenshot%202023-08-08%20at%2015.21.34.JPG.jpg)

## Read

---

```python
import h5py, numpy as np

with h5py.File('test2.hdf5', 'r') as hdf:
    base_items = list(hdf.items())
    print(base_items)
    group_a = hdf.get('a')
    group_a_items = list(group_a.items())
    print(group_a_items)
# [('a', <HDF5 group "/a" (2 members)>)]
# [('FLOAT_DATA', <HDF5 dataset "FLOAT_DATA": shape (5,), type "|O">), ('INT_DATA', <HDF5 dataset "INT_DATA": shape (5,), type "|O">)]

with h5py.File('test2.hdf5', 'r') as hdf:
    ls = list(hdf.keys())
    print(ls)
    data = hdf.get('a')
    a = np.array(data)
    print(a.shape)
# ['a']
# (2,)

f = h5py.File('test2.hdf5', 'r')
keys_ls = list(f.keys())
values_ls = list(f.values())
items_ls = list(f.items())
print(keys_ls)
print(values_ls)
print(items_ls)
# ['a']
# [<HDF5 group "/a" (2 members)>]
# [('a', <HDF5 group "/a" (2 members)>)]
```

- 특정 데이터 조회하기

```python
import h5py

with h5py.File('20221025RMS.hdf5', 'r') as rms:
    group_idx = 0
    dataset_idx = 2

    group = rms['32769']
    subgroup_names = list(group.keys())

    target_subgroup_name = subgroup_names[group_idx]
    target_subgroup = group[target_subgroup_name]

    target_dataset_name = list(target_subgroup.keys())[dataset_idx]
    target_dataset = target_subgroup[target_dataset_name]

    print(target_subgroup_name)
    print(target_dataset_name)
    print(target_dataset[()])

# 결과
# 11H43M18S.846247
# HDS_HCS_R_P21L
# 1.9505000114440918
```

![Screenshot 2023-08-03 at 08.55.38.JPG](C:\Users\tritech-fall\Desktop\TIL\office\HDF\HDF5.assets\Screenshot%202023-08-03%20at%2008.55.38.JPG.jpg)

- 파일 경로, 인덱스 입력하여 조회하기

```python
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

# 결과
# HDF5 파일 경로를 입력하세요: 20221025RMS.hdf5
# 상위 그룹 인덱스를 입력하세요 (0부터 0까지): 0
# 하위 그룹 인덱스를 입력하세요 (0부터 721까지): 39
# 데이터셋 인덱스를 입력하세요 (0부터 313까지): 48
# Top Group Name: /32769
# Subgroup Name: /32769/11H43M28S.796407
# Dataset Name: PMS_ID_L01_TS02
# Dataset Contents: 24.299999237060547
```

# 🔗참고 링크

[[Python] 파이썬 h5py 설치 및 사용방법 알아보기 : HDF5 예제 - 피알아이브이에이티이](https://playground.naragara.com/715/)

[[h5py] hdf5 소개, h5py 사용법 간단 정리](https://bo-10000.tistory.com/108)

[HDF5 with Python](https://www.youtube.com/playlist?list=PLea0WJq13cnB_ORdGzEkPlZEN20TSt6Lx)

[7.1 HDF5의 특징 - 공학자를 위한 Python](https://wikidocs.net/33122)

[HDF5 User's Guide](https://support.hdfgroup.org/HDF5/doc/UG/HDF5_Users_Guide-Responsive%20HTML5/index.html#t=HDF5_Users_Guide%2FAttributes%2FHDF5_Attributes.htm)
