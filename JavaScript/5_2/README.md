`동기` : 이전의 요청이 완전히 처리되고, 응답을 받아야 비로소 다음 요청을 수행하는 방식

`비동기` : 이전의 요청에 대하 응답 여부와 관계 없이 다음 요청을 수행하는 방식 (병렬적 처리 가능)


교수님 정답
* 동기식
  - js는 싱글 쓰레드 => 한 번에 한 가지 작업만 처리
  - 동기식 처리 : 이전 작업이 끝날 때까지 다른 작업을 처리할 수 없다

* 비동기식
  - js 비동기 함수를 만나면 => web api로 처리 주체를 넘김
  - js 동작 완료를 기다리지 않고, 바로 다음 코드를 실행
  - web api에서 동작이 끝나면 task queue로 이동하여 event loop를 통해 call stack으로 돌아감 (콜백함수)
