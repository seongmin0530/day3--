#class

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성 :", end=' ')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전!')


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(전기) 시전!')


class Ggoboogi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(물) 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다')


class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격(불) 시전!')


while True:
    menu = input('1) 포켓몬 생성   2) 프로그램 종료')
    if menu == '2':
        print('프로그램을 종료합니다.')
        break
    elif menu == '1':
        pkoemon = input('1) 피카츄  2) 꼬부기  3)  파이리 :')
        if pkoemon == '1':
            name = input('플레이어 이름 입력: ')
            skil = input('사용 가능한 기술 입력(/로 구분하여 입력) :')
            p = Pikachu(name,skil)
        elif pkoemon == '2':
            name = input('플레이어 이름 입력: ')
            skil = input('사용 가능한 기술 입력(/로 구분하여 입력) :')
            p = Ggoboogi(name, skil)
        elif pkoemon == '3':
            name = input('플레이어 이름 입력: ')
            skil = input('사용 가능한 기술 입력(/로 구분하여 입력) :')
            p = Pairi(name, skil)
        else:
            print('메뉴에서 골라주세요.')
        info_attack = input('1) 정보조회 2) 공격 :')
        if info_attack == '1':
            p.info()
        elif info_attack == '2':
            p.info()
            attack_menu = input('공격 번호 선택 : ')
            p.attack(int(attack_menu) - 1)
        else:
            print('메뉴에서 골라주세요.')
    else:
        print('메뉴에서 골라주세요.')

