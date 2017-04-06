# system-trading-python

## tensorflow

- https://tensorflowkorea.gitbooks.io/tensorflow-kr/g3doc/get_started/
- https://www.tensorflow.org/versions/r0.10/tutorials/
- https://github.com/aymericdamien/TensorFlow-Examples
- https://gist.github.com/haje01/202ac276bace4b25dd3f

##  기본 개념 익히기

### 용어

#### 오퍼레이션(Operation)
그래프 상의 노드는 오퍼레이션(줄임말 op)으로 불립니다. 
오퍼레이션은 하나 이상의 텐서를 받을 수 있습니다.
오퍼레이션은 계산을 수행하고, 결과를 하나 이상의 `텐서`로 반환할 수 있습니다.

#### 텐서(Tensor)
내부적으로 모든 데이터는 텐서를 통해 표현됩니다.
텐서는 일종의 다차원 배열인데, 그래프 내의 오퍼레이션 간에는 텐서만이 전달됩니다.
(Caffe 의 Blob과 유사합니다)

#### 세션(Session)
그래프를 실행하기 위해서는 세션 객체가 필요합니다.
세션은 오퍼레이션의 실행 환경을 캡슐화한 것입니다.

#### 변수(Variables)
변수는 그래프의 실행시, 파라미터를 저장하고 갱신하는데 사용됩니다.
메모리 상에서 텐서를 저장하는 버퍼 역할을 합니다.






## 시뮬레이션 테스트


- [2017.04.03_발표](https://rawgit.com/jacegem/system-trading-python/master/remark/2017.04.03.html)


### 출처

- https://rawgit.com/


## 할일

- 슬랙 연동
- firebase 연동


## 주가 확인

- http://finance.daum.net/item/chart.daum?code=023350

이곳에서 5,20,60,120 평균선을 확인할 수 있습니다


## jupyter

- 실행 명령어 : jupyter notebook
- 기본 포트 : http://localhost:8888/


## 데이터 구조

- stock_datas
  - {code, stock_data}

- stock_data
  - item
    {code, name}
  - df


많은 의견 부탁드립니다.

## 목표

- 경제적 자유를 얻는다

## 이력

- 2017.04.01 프로젝트 시작