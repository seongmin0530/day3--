# class

class Pokemon:  #클래스
    def __init__(self, name, owner, skils):  #객체 초기화 메서드
        self.name = name  # 속성
        self.owner = owner  # 속성
        self.skils = skils.split('/')
        print(f"포켓몬 {name} 객체 생성됨")

    def info(self):  # 멤버 함수
        print(f"\n{self.owner}의 포켓몬은 {self.name}입니다.")
        for skil in self.skils:
            print(f"{self.name}이 사용할 수 있는 기술은 {skil}입니다.")

p1 = Pokemon('피카츄', '한지우', '50만 볼트/100만 볼트/번개')  # p1 = 인스턴스
p2 = Pokemon('꼬부기', '오바람', '고속스핀/하이드로펌프/몸통박치기/거품')  # p2 = 인스턴스
p1.info()
p2.info()