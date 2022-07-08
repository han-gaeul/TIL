# Branch



## Git flow

- Git을 활용하여 협업하는 흐름
- Branch를 활용하는 전략



## branch 종류별 특징

- **master (main)**
  - 배포 가능한 상태의 코드

- **develop (main)**
  - feature branch로 나뉘거나, 발생된 버그 수정 등 개발 진행
  - 개발 이후 release branch로 갈라짐.
- **feature branches (supporting)**
  - 기능별 개발 브랜치(topic branch)
  - 기능이 반영되거나 드랍되는 경우 브랜치 삭제
- **realease branches (supporting)**
  - 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 minor bug fix 등 반영
- **hotfixes (supporting)**
  - 긴급하게 반영 해야하는 bug fix
  - Release branch는 다음 버전을 위한 것이라면 hotfix branch는 현재 버전을 위한 것





## branch 기본 명령어

1. 브랜치 생성

```tex
(master) $ git branch 'branch name'
```

2. 브랜치 이동

```tex
(master) $ git checkout 'branch name'
```

3. 브랜치 생성 및 이동

```tex
(master) $ git checkout -b 'branch name'
```

4. 브랜치 목록

```tex
(master) $ git branch
```

5. 브랜치 삭제

```tex
(master) $ git branch -d 'branch name'
```









