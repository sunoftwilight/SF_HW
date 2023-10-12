CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);



BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;


-- zoo table에 6개의 데이터가 입력됨
-- zoo 테이블에서 weight 필드의 값이 100 미만인 데이터들은 삭제
-- 방금 한 실행을 되돌리기
-- zoo 테이블에서 eat 필드가 omnivore인 데이터 삭제
-- 저장
-- zoo 테이블의 데이터 개수 조회