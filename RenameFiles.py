import os

name_kor = [
"스페셜 위크",
"사일런스 스즈카",
"토카이 테이오",
"마루젠스키",
"후지 키세키",
"오구리 캡",
"골드 쉽",
"보드카",
"다이와 스칼렛",
"타이키 셔틀",
"그래스 원더",
"히시 아마존",
"메지로 맥퀸",
"엘 콘도르 파사",
"티엠 오페라 오",
"나리타 브라이언",
"심볼리 루돌프",
"에어 그루브",
"아그네스 디지털",
"세이운 스카이",
"타마모 크로스",
"파인 모션",
"비와 하야히데",
"마야노 탑건",
"맨하탄 카페",
"미호노 부르봉",
"메지로 라이언",
"히시 아케보노",
"유키노 비진",
"라이스 샤워",
"아이네스 후진",
"아그네스 타키온",
"어드마이어 베가",
"이나리 원",
"위닝 티켓",
"에어 샤커",
"에이신 플래시",
"카렌짱",
"카와카미 프린세스",
"골드 시티",
"사쿠라 바쿠신 오",
"시킹 더 펄",
"신코 윈디",
"스윕 토쇼",
"슈퍼 크릭",
"스마트 팔콘",
"젠노 롭 로이",
"토센 조던",
"나카야마 페스타",
"나리타 타이신",
"니시노 플라워",
"하루 우라라",
"뱀부 메모리",
"비코 페가수스",
"마블러스 선데이",
"마치카네 후쿠키타루",
"미스터 시비",
"메이쇼 도토",
"메지로 도베르",
"나이스 네이처",
"킹 헤일로",
"마치카네 탄호이저",
"이쿠노 딕터스",
"메지로 파머",
"다이타쿠 헬리오스",
"트윈 터보",
"사토노 다이아몬드",
"키타산 블랙",
"사쿠라 치요노 오",
"시리우스 심볼리",
"메지로 아르당",
"야에노 무테키",
"츠루마루 츠요시",
"메지로 브라이트",
"데어링 택트",
"사쿠라 로렐",
"나리타 탑 로드",
"야마닌 제퍼",
"노스 플라이트",
"심볼리 크리스 에스",
"타니노 김렛",
"다이이치 루비",
"메지로 라모누",
"애스턴 마짱",
"사토노 크라운",
"슈발 그랑",
"케이에스 미라클",
"정글 포켓",
"코파노 리키",
"홋코 타루마에",
"원더 어큐트",
"사운드 오브 어스",
"카츠라기 에이스",
"네오 유니버스",
"히시 미라클",
"탭 댄스 시티",
]

download_dir = "./downloads/"

def rename_files():
    file_list = os.listdir(download_dir)

    for file_name in file_list:
        tokens1 = file_name.split("-")
        idx = int(tokens1[0])
        char_name = name_kor[idx - 1];

        re_name = file_name.replace(" 制服", "_교복")
        re_name = re_name.replace(" 勝負服", "_승부복")
        re_name = re_name.replace(" 原案", "_원안")
        re_name = re_name.replace(" STARTING FUTURE", "_STARTING-FUTURE")
        tokens2 = re_name.split("_")

        target_name = "{}_{}_{}_{}".format(file_name[:5], char_name, tokens2[2], tokens2[3])

        file_path = os.path.join(download_dir, file_name)
        target_path = os.path.join(download_dir, target_name)

        print(file_path + " -> " + target_path)
        os.rename(file_path, target_path)

if __name__ == "__main__":
    rename_files()