# coding=utf-8
import requests
import execjs
import json


class Translate:
    def __init__(self, query_string):
        self.query_string = query_string
        self.post_url = "https://fanyi.baidu.com/v2transapi"
        self.post_url2 = "https://fanyi.baidu.com/langdetect"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "cookie": "BAIDUID=6C85CEDC7D9A32757DB9F729B6B82D93:FG=1; BIDUPSID=6C85CEDC7D9A32757DB9F729B6B82D93; PSTM=1545924966; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __cfduid=db0c65fd40cde5f01c8685ee05d9191f01555138947; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=EdRRWNhemJsUkRHYUh-UnRKN0MycGVOc2NUQlNiUHNMWklJMHlrVnZuWVZTUk5kSVFBQUFBJCQAAAAAAAAAAAEAAABN5intsuLK1LrFNzcwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABW861wVvOtcV; delPer=0; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1559024824; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1559024963; H_WISE_SIDS=130611_124612_127760_100806_132555_113878_114746_132019_120193_132051_132433_132439_130763_132393_132379_132325_132212_131518_132261_118895_118858_131401_118850_118829_118793_132211_131649_131576_131536_131533_131529_130222_131295_131871_131390_129564_131795_131394_130126_132239_131874_130570_131194_131241_129654_127027_132557_132123_132539_131035_131905_132293_132552_131047_129376_129644_132204_132328_110085_132354_127969_131506_123289_132350_132282_127417_131549_131750; rsv_i=458a17VKVNGYA4LozMLywmJoc9l0TEExyt23lX4Qtc%2B%2Fp27XGu2fjyKWx1jd8%2FYuvll%2BnA%2BEO1ghNbndYESMZ6Us07Y0CSM; FEED_SIDS=661313_0528_14; BDPASSGATE=IlPT2AEptyoA_yiU4VKI3kIN8efBKP_BAh8FSyR636S4fCaWmhH3BrUrWz0HSieXBDP6wZTXebZda5XKXlVXa_EqnBsZokJL7UOdxq_Kr0vtKx2-fQIi_Nz5V5E2sA8PbRhL-3MEF32EADIqcgy9huwQch_7c2ZHefn15EDCmMrs1TCG17r6qWaEKHRfXZ0APNu594rXnEpKLDm4YtKtT9PecSIMR7QEy0uync9G2h3IxyUwLQykOAka1Fz5BJV2BxCyGwC78qSo_-Ev9HUkVUIlnUSq-tC; SE_LAUNCH=5%3A25983755; PSINO=7; H_PS_PSSID=1462_21106_29063_28518_29099_28830_28702; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1559023547,1559025988,1559027185; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1559027185; yjs_js_security_passport=42011fc11f18fda0916996c51628c88c5b433670_1559027157_js"
        }

    def get_post_data(self, lan):
        with open("百度翻译.js") as f:
            jsData = f.read()
        p = execjs.compile(jsData).call("e", self.query_string)

        post_data = {
            "query": self.query_string,
            "from": 'zh' if lan == 'zh' else 'en',
            "to": 'en' if lan == 'zh' else 'zh',
            "token": "aafca2ee89544ac6718a3f99e0d87855",
            "sign": p
        }
        return post_data

    def get_lan(self):
        post_data2 = {
            "query": self.query_string
        }
        lan_r = requests.post(self.post_url2, data=post_data2, headers=self.headers)
        lan_r_dict_ret = json.loads(lan_r.content.decode())
        return lan_r_dict_ret['lan']

    def parse_url(self, post_data):
        return requests.post(self.post_url, data=post_data, headers=self.headers)

    def run(self):
        r = self.parse_url(self.get_post_data(self.get_lan()))
        dict_ret = json.loads(r.content.decode())
        ret = dict_ret["trans_result"]["data"][0]["dst"]
        print(ret)


if __name__ == '__main__':
    tran = Translate('你好')
    tran.run()















