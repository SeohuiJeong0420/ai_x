import pandas as pd
from dotenv import load_dotenv
import urllib.request
import os
import sys
import json
# 네이버 쇼핑 데이터 처리 함수 만들기 복습

# 1. word에 대해 media검색한 결과의 문자열 리턴
def get_naver_api_data(media, word):
    load_dotenv(".env")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    encText = urllib.parse.quote(word)#문자열을 URL 인코딩(퍼센트 인코딩)으로 변환
    url = f"https://openapi.naver.com/v1/search/{media}?sort=date&display=15&query={encText}"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)

#json형식 문자열을 데이터프레임으로 변환 후 리턴
def str_json_dataframe(str_json_result):
    if isinstance(str_json_result, str): #str_json_result가 str이면 제이슨으로 파싱 후 저장
        json_result = json.loads(str_json_result)
    else:# 아닐경우 빈 딕셔너리 저장
        json_result = {}
    #json_result(딕셔너리)를 데이터 프레임으로 바꾸기
    items = json_result.get('items',[]) #딕셔너리에서 'items' 키의 값을 가져오되, 키가 없으면 기본값 [](빈 리스트)를 반환
    df = pd.DataFrame(items)
    df['순위']=range(1,len(df)+1)
    df.set_index("순위", inplace=True) # "순위" 컬럼을 인덱스로 설정하고 원본 DataFrame을 직접 변경
    return df

#main함수
def main():
    #네이버 쇼핑몰 데이터 출력
    str_data = get_naver_api_data("shop", "노트북")
    df_laptop_shopping = str_json_dataframe(str_data)
    print(df_laptop_shopping)

#이 파일이 직접 실행될 때만 main() 함수를 호출 (다른 파일에서 import될 때는 실행되지 않음)
if __name__ =='__main__':
    main()