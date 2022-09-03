### `MarkDown 문법`

***

### 제목

​	- h1 ~ h6 까지 #의 개수로 구분하여 조절

# h1

## h2

### h3

#### h4

##### h5

###### h6



```
# h1
## h2
### h3
#### h4
##### h5
###### h6
```





---



### 강조 표현

- `*`, `_`  : *이탤릭체*, _이탤릭체2_
- `**`, `__`  : **굵게**, __굵게2__
- `~~`  : ~~취소선~~
- `***` : ***굵게이탤릭체***



---



### 목록

**순서가 있는 목록(ol)**  : `1.`  사용 

**순서가 없는 목록(ul)**  : -, *, +



> 1. 순서가 있는 목록
> 2. 순서가 있는 목록2
>    1. 순서가 있는 목록2-1
> 3. 순서가 있는 목록3
>
> 
>
> - 순서가 없는 목록
>   - 순서가 없는 목록-1
> - 순서가 없는 목록2



​	- `Tab`  키를 사용하여 들여쓰기 가능



---



### 링크

​	- `[ ]( )` : 대괄호 안에 문자열을 작성하고, 소괄호 안에 url 작성

- [github](https://github.com/)
- [google](https://www.google.co.kr/)

```
[Title](link)
[github](https://github.com/)
```



​	- 일반적인 url 또는 이메일 주소의 경우

- Url : <https://www.google.co.kr/>
- 이메일 : <gmlakdcjs314@gmail.com>

```
url : <https://www.google.co.kr/>
이메일 : gmlakdcjs314@gmail.com
```



---



### 이미지

`![ ]()` : 대괄호 안에 이미지 이름을 쓰고, 소괄호 안에 이미지 링크를 작성



![Python](https://www.python.org/static/img/python-logo@2x.png)

![다운로드](markdown.assets/다운로드-7116684.jpeg)



---



### 코드 블록

- 펜스 코드 블록(Fenced Code block)

` ``` ` : `backtick` 기호 3개 작성 후 코드 언어`(Python, JavaScript, HTML 등)를 선택



```python
print("Hello World")
```

```html
<head>
  제목
</head>
<body>
  내용
</body>
```

````
```
{
  "firstName": "gaeul",
  "lastName": "Han",
  "age": 25
}
```
````



- 인라인 코드 블록(Inline Code block)

` ` : `backtick` 기호 1개를 활용



---



### 표(Table)

| 제목 | 제목2 | 제목3 |
| ---- | ----- | ----- |
| 내용 | 내용2 | 내용3 |
| 내용 | 내용2 | 내용3 |
| 내용 | 내용2 | 내용3 |



```
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```



- Mac 단축키 : option + command + T



---



### 인용문(Blockquotes)

`>`  를 사용

> 인용문
>
> > 인용문 -1
> >
> > > 인용문 -2



```
> 인용문
> > 인용문 -1
> > > 인용문 -2
```



> #### h4
>
> 1. 목록
>
> ```
> code
> ```



다른 요소를 추가해서 사용 가능



---



### 참고

- [마크다운 사용법-GitHub](https://gist.github.com/ihoneymon/652be052a0727ad59601#1-%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4%EC%97%90-%EA%B4%80%ED%95%98%EC%97%AC)
- [마크다운 사용법-Velog](https://velog.io/@bboding/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4MarkDown-%EC%82%AC%EC%9A%A9%EB%B2%95)
- [마크다운 치트 시트](https://www.markdownguide.org/cheat-sheet/)

