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

​	- `mkdir` (make directory) : 디렉토리 생성

​	- `touch` : 파일의 날짜와 시간 수정(0바이트 빈 파일 생성)

​	- `rm` : 파일 삭제

​	- `rm -r` : 폴더 삭제

​	- 단축키 `control + l` 또는 명령어 `clear` : 터미널 내용 지우기



​	- `git init` : 로컬 저장소 생성

​	- `git add <파일명>` : 특정 파일/폴더의 변경 사항 추가

​	- `git commit -m 'message'` : 버전(커밋) 기록

​	- `git log` : 버전(커밋) 기록 확인

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

1. 저장소 생성

```
$ git init
```

- git 저장소를 만들면 해당 디렉토리 안에 `.git` 폴더가 생성
- 터미널에서는 `(master)` 라는 표기가 생김
- git 설정 또는 명령어를 작성할 때 현재 경로를 꼭 확인해야 함



![image-20220706173409687](git.assets/image-20220706173409687.png)



- `Desktop` 에 저장소 만드는 건 추천하지 않음



2. add

- 작업 위치(Working Directory) 안에 있는 파일을 Staging Area로 옮기기 위해 사용

  Staging Area는 commit을 진행하기 전에 임시 저장된 상태

- 