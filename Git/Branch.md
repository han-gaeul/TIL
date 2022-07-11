# Branch



## branch란?

- 독립적으로 어떤 작업을 진행하기 위한 개념
- 필요에 의해 만들어지는 각각의 브랜치는 다른 브랜치의 영향을 받지 않음

​		➡️ 여러 작업을 동시에 진행할 수 있음



## branch 목적

독립적인 버전들을 만들어가기 위해서



## branch 종류별 특징

- **master (main)**
  - 배포 가능한 상태의 코드
  - 제품으로 출시될 수 있는 브랜치

- **develop (main)**
  - 다음 출시 버전을 개발하는 브랜치
  - 기능 개발을 위한 브랜치들을 병합하기 위해 사용
  - feature branch로 나뉘거나, 발생된 버그 수정 등 개발 진행
  - 개발 이후 release branch로 갈라짐.
- **feature branches (supporting)**
  - 기능별 개발 브랜치(topic branch)
  - 기능이 반영되거나 드랍되는 경우 브랜치 삭제
- **realease branches (supporting)**
  - 이번 출시 버전을 준비하는 브랜치
  - 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 minor bug fix 등 반영
- **hotfixes (supporting)**
  - 출시 버전에서 발생한 버그를 수정하는 브랜치
  - 긴급하게 반영 해야하는 bug fix
  - Release branch는 다음 버전을 위한 것이라면 hotfix branch는 현재 버전을 위한 것



👉🏻 *참고 링크*

 i. [[GitHub] Git 브랜치의 종류 및 사용법](https://gmlwjd9405.github.io/2018/05/11/types-of-git-branch.html)





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







## branch merge







