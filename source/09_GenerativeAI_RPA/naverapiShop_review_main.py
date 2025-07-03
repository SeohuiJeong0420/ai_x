#파일 백업 후, 현재 리스트(now_list)를 예전 리스트(prev_list)로 보내고, 현재 리스트 업데이트
from naverapiShop_review import get_naver_api_data, str_json_dataframe
import xlwings as xw
import datetime
import shutil
import handle_sheet as hs #파일 백업 후 업데이트하는 클래스스

def main():
    # 1. 파일 열기
    file_path = "genai_rpa.xlsx"
    wb = xw.Book(file_path)

    #2. 파일 백업 후 기존 now_list를 prev_list로 보내기
    hs.handle_init_sheet(file_path=file_path, wb=wb)

    # 3. 네이버 api쇼핑목록 데이터 출력

    str_data = get_naver_api_data("shop", "노트북")
    df_laptop_shopping = str_json_dataframe(str_data)

    # 4. 2번 내용 업데이트
    hs.update_now_list(wb, df_laptop_shopping)

    # 5. 파일 저장 밎 닫기
    hs.save_close_file(file_path, wb)

if __name__ == "__main__":
    main()