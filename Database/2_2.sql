CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');
-- 테이블 이름 다음에 (필드 목록) 작성이 필요함 => zoo (필드목록) 으로 작성하기


-- 2)
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);
-- rowid는 내장된 값으로 우리가 입력하지 않는다 => rowid는 제거하기


-- 3)
INSERT INTO zoo (name, eat, age) VALUES
('dolphin', 'carnivore', 3);
-- weight는 NOT NULL 제약조건이 걸려있는데 빈값으로 두었다 => weight 값도 넣어주기
