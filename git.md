# git



#### git이란?

분산 버전 관리 시스템이다.

​	- 버전 : 컴퓨터 소프트웨어의 특정 상태



---



#### 명령어

​	- `pwd` (print working directory) : 현재 디렉토리(폴더/파일) 출력

​	- `cd` (change directory) : 디렉토리 하위 이동

​	- `cd ..` : 디렉토리 상위 이동(띄어쓰기 필수)

​	- `ls` (list) : 목록

​	- `ls -al` : 폴더 안에 있는 파일, 폴더 목록

​	- `mkdir` (make directory) : 디렉토리 생성

​	- `touch` : 파일의 날짜와 시간 수정(0바이트 빈 파일 생성)

​	- `rm` : 파일 삭제

​	- `rm -r` : 폴더 삭제

​	- `rm -fr .git` : git 삭제

​	- 단축키 `control + l` 또는 명령어 `clear` : 터미널 내용 지우기



​	- `git init` : 로컬 저장소 생성

​	- `git add <파일명>` : 특정 파일/폴더의 변경 사항 추가

​	- `git commit -m 'message'` : 버전(커밋) 기록

​	- `git log` : 버전(커밋) 기록 확인

​	- `git log -p` : 자세한 기록 확인

​	- `git log -1` : 가장 최근 기록된 커밋 확인

​	- `git log --oneline` : 한 줄로 기록 확인

​	- `git status` : 상태 확인(1통, 2통, 3통)





---



#### Git 정보 설정

```
$ git config --global user.name '이름'
$ git config --global user.email '이메일'
```

- Commit을 작성한 사람(author)으로 저장됨.
- 이름과 이메일 정보는 Github에서 사용하고 있는 것과 동일하게 설정





---



#### Git 사용

1. git init(저장소 생성)

```
$ git init
```

- git 저장소를 만들면 해당 디렉토리 안에 `.git` 폴더가 생성
- 터미널에서는 `(master)` 라는 표기가 생김
- git 설정 또는 명령어를 작성할 때 현재 경로를 꼭 확인해야 함

- `Desktop` 에 저장소 만드는 건 추천하지 않음

<img src="git.assets/스크린샷 2022-07-06 17.54.12.png" alt="스크린샷 2022-07-06 17.54.12" style="zoom: 67%;" />



2. add

```
$ git add .
$ git add <파일명>
```

- 작업 위치(Working Directory) 안에 있는 파일을 Staging Area로 옮기기 위해 사용

  Staging Area는 commit을 진행하기 전에 임시 저장된 상태

- `1.txt` 라는 파일을 생성 후 `git status` 명령어를 입력하면 '변경 사항을 추가하지 않았음 (git add를 사용)' 하라는 문구가 나옴

![스크린샷 2022-07-06 18.05.54](git.assets/스크린샷 2022-07-06 18.05.54.png)

- `git add 1.txt` 입력 후 다시 `git status` 명령어를 입력하면 Staging Area에 추가 완료

![스크린샷 2022-07-06 18.08.36](git.assets/스크린샷 2022-07-06 18.08.36.png)



3. commit

```
$ git commit -m 'message'
```

- 버전(커밋) 기록을 할 때 알아보기 쉬운 내용으로 작성

- 영어로 작성하는 것이 보편적

  - 참고자료 

    [좋은 커밋 메시지를 작성하기 위한 7가지 약속](https://meetup.toast.com/posts/106) / [좋은 커밋 메시지를 위한 영어 사전](https://blog.ull.im/engineering/2019/03/10/logs-on-git.html)

- 커밋 기록을 확인하기 위해서 `git log` 명령어 사용

![커밋기록](git.assets/스크린샷 2022-07-06 18.20.04.png)



4. 

w