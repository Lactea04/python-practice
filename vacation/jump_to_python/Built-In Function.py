#abs -> abs(x): x의 절댓값 return
#all -> all(x): x는 iterable 자료형(ex: list, tuple, dictionary 등등)내의 요소 중 하나라도 거짓이면 거짓
#any -> any(x): all의 반대

#chr -> chr(int()): 아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 출력
#dir -> dir(x): x는 object이고, 그 object가 가지고 있는 method를 출력해줌
#divmod -> divmod(a(숫자), b(숫자)) a를 b로 나누었을 때, (몫, 나머지) 출력 (Note: //(몫 구하는 연산자), %(나머지 구하는 연산자))

#enumerate -> 반복가능한 자료형을 입력 받아서 for 문에 활용시 (index, value)의 형태로 값을 출력함
#eval -> eval(실행 가능한 문자열): 문자열의 결과 출력
#filter -> filter(function, iterable): (ex: list(filter(lambda x: x%2 ==0, [1, 2, 3, 4]))) >>> [2, 4]

#hex -> hex(int()): 정수값을 입력받아 16진수로 변환하여 주는 함수
#id -> id(object): 객체의 고유 주소값 출력

#isinstance -> isinstance(object, class): object가 해당 class의 instance인지 참거짓 판별
#map -> map(function, iterable) iterable 자료에 function을 적용한 것을 리턴함
#oct -> oct(int()): 정수를 8진수 문자열로 전환

#ord -> ord(c): 문자의 아스키 코드값을 돌려주는 함수
#pow -> pow(x, y): x**y
#range -> range([start,] stop [,step]): start부터 stop 앞까지 step 크기만큼 간격을 두어 iterable 제작

#round -> round(number[, ndigits]): 반올림 (ex: round(2.3) >>> 2)
#zip -> zip(*iterable): iterable 자료 여러개를 묶어줌 (ex:zip([1, 2, 3], [4, 5, 6]) >>> [(1, 4), (2, 5), (3, 6)])