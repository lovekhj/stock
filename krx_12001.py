import requests
import pandas as pd
from io import BytesIO
import time


def krx_price(tdate):
    print(tdate)

    gen_req_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    query_str_parms = {
        'locale': 'ko_KR',
        'mktid': 'All',
        'trdDd': '20220304',
        'share': '1',
        'money': '1',
        'csvxls_isNo': 'false',
        'name': 'fileDown',
        'url': 'dbms/MDC/STAT/standard/MDCSTAT01501'
    }
    headers = {
        'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020101',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'
    }
    otp = requests.post(gen_req_url, query_str_parms, headers=headers)

    time.sleep(1.0)

    # download.cmd
    down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
    # post 함수를 이용해서 otp 코드를 제출함
    r = requests.post(down_url, {'code': otp}, headers=headers)
    time.sleep(1.0)
    try:
        down_ks = pd.read_csv(BytesIO(r.content), encoding='EUC-KR')
        print(down_ks)
        # df = pd.read_excel(BytesIO(r.content), thousands=','
        #                    converters={'종목코드': str})
        # df.to_excel('krx_0302.xlsx', index=False,
        #             index_label=None, encoding='utf-8-sig')
    except:
        print("파일이 손상되었습니다.")
        return ""


# -------------------------------------------------------
# krx : 12001 전종목시세 다운로드
# -------------------------------------------------------
krx_price('20220304')
