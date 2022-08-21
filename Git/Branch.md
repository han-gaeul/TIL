### Branch

-------------

#### 📝 branch란?

- 독립적으로 어떤 작업을 진행하기 위한 개념
- 필요에 의해 만들어지는 각각의 브랜치는 다른 브랜치의 영향을 받지 않음

​		➡️ 여러 작업을 동시에 진행할 수 있음



##### `branch 목적`

독립적인 버전들을 만들어가기 위해서



##### `branch 종류별 특징`

- master (main)
  - 배포 가능한 상태의 코드
  - 제품으로 출시될 수 있는 브랜치

- develop (main)
  - 다음 출시 버전을 개발하는 브랜치
  - 기능 개발을 위한 브랜치들을 병합하기 위해 사용
  - feature branch로 나뉘거나, 발생된 버그 수정 등 개발 진행
  - 개발 이후 release branch로 갈라짐.
- feature branches (supporting)
  - 기능별 개발 브랜치(topic branch)
  - 기능이 반영되거나 드랍되는 경우 브랜치 삭제
- realease branches (supporting)
  - 이번 출시 버전을 준비하는 브랜치
  - 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 minor bug fix 등 반영
- hotfixes (supporting)
  - 출시 버전에서 발생한 버그를 수정하는 브랜치
  - 긴급하게 반영 해야하는 bug fix
  - Release branch는 다음 버전을 위한 것이라면 hotfix branch는 현재 버전을 위한 것



👉🏻 *참고 링크*

 i. [[GitHub] Git 브랜치의 종류 및 사용법](https://gmlwjd9405.github.io/2018/05/11/types-of-git-branch.html)





#### 🔎 branch 기본 명령어

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



#### 🔎 branch merge

- 각 branch에서 작업을 한 이후 이력(커밋/버전)을 합치기 위해서는 일반적으로 merge 명령어 사용

- 병합을 진행할 때, 만약 서로 다른 이력(commit)에서 동일한 파일을 수정한 경우 충돌이 발생할 수 있음

- 이 경우 반드시 직접 수정을 진행 해야 하며 충돌이 발생한 것은 오류가 발생한 것이 아니라

  이력이 변경되는 과정에서 반드시 발생할 수 있는 것

**`Branch merge - fast-forward`**

- 기존 master 브랜치에 변경사항이 없어 단순히 앞으로 이동

  ```python
  (master) $ git merge feature-a
  Updating 54b9314..5429f25
  Fast-forward
  ```

  > 1. feature-a branch로 이동 후 commit
  > 2. master 별도 변경 없음
  > 3. master branch로 병합

**`Branch merge - merge commit`**

- 기존 master 브랜치에 변경사항이 있어 병합 커밋 발생

  ```python
  (master) $ git merge feature-a
  Already up to date!
  Merga made by the 'recursive' strategy.
  ```

  > 1. feature-a branch로 이동 후 commit
  > 2. Master branch commit
  > 3. master branch로 병합
