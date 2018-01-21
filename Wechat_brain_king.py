# -*- coding: utf-8 -*-
import json,ssl,os,time,random
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class brain_king:

    def __init__(self):
        self.index = 0
        self.score = [0,0,0,0]
        self.choose = ['A','B','C','D']
        self.question_db = {'s':0}
        self.total = 0
        self.right_num = 0
        self.x = 0
        self.y = 0


    def Get_qus_choose(self):
        try:
            with open('D:\\tmp.txt','r',encoding='utf-8-sig') as f:
                content = f.readline()
                data = json.loads(content)
                return data['data']['quiz'],data['data']['options'][0:4],data['data']['num']
        except:
            return 0,0,0


    def Zhidao_baidu(self,keyword):
        payload = {
            'lm':'0',
            'rm':'20',
            'pn':'0',
            'fr':'search',
            'ie':'utf-8',
            'word':keyword
        }
        agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        headers = {
            "Host": "zhidao.baidu.com",
            "Referer": "https://zhidao.baidu.com/",
            'User-Agent': agent
        }
        url = 'https://zhidao.baidu.com/search'
        r = requests.get(url,headers = headers,params=payload,verify=False,allow_redirects = True)
        r.encoding = 'gbk'
        return r.text

    def make_choose(self,web_txt,Content):
        if Content[0] in self.question_db:
            return self.question_db[Content[0]]
        else:
            for i in range(0,4):
                self.score[i] = web_txt.count(str(Content[i]))
                print(self.score[i], Content[i])
            '''
            判断条件策越
            '''
            if min(self.score) == max(self.score):
                print('Can''t make choose,please choose by your self \n')
                return random.randint(0,3)
            if  self.score.count(0) == 1:
                return self.score.index(min(self.score))
            else:
                return self.score.index(max(self.score))

    def Get_right_answer(self,Content):
        try:
            with open('D:\\Answer.txt','r',encoding='utf-8-sig') as f:
                content = f.readline()
                data = json.loads(content)
                self.question_db[Content] = data['data']['answer'] - 1
                with open(r'D:\question_db.txt', 'a', encoding='utf-8') as f:
                    f.write('题目:{}\n答案:{}\n'.format(Content, self.choose[self.question_db[Content]]))
                return True
        except:
            return False

    def Adb_input(self,choose):
        time.sleep(random.uniform(2.9,2.9))
        if choose == 0:
            self.x = random.randint(350,650),
            self.y = random.randint(900,940),
        if choose == 1:
            self.x=random.randint(350,650),
            self.y=random.randint(1050,1150),

        if choose == 2:
            self.x=random.randint(350,650),
            self.y=random.randint(1250,1350),

        if choose == 3:
            self.x=random.randint(350,650),
            self.y=random.randint(1450,1550),
        cmd = 'adb shell input swipe {0} {1} {0} {1} {2}'.format(self.x[0],self.y[0],random.randint(520, 520))
        os.system(cmd)


brain = brain_king()
while True:
    try:
        Content = brain.Get_qus_choose()
        if Content[2] > brain.index:
            brain.total = brain.total + 1
            brain.index = Content[2]
            print('\n'+str(Content[0:2]))
            web_txt = brain.Zhidao_baidu(Content[0])
            choose = brain.make_choose(web_txt,Content[1])
            with open(r'D:\answer_log.txt','a',encoding='utf-8') as f:
                f.write('题目{}:{}\n'.format(brain.index,Content[0]))
                f.write('次数:{}A:{}\n 次数:{} B:{}\n 次数:{} C:{}\n 次数:{} D:{}\n'.format(brain.score[0],Content[1][0],brain.score[1],Content[1][1],brain.score[2],Content[1][2],brain.score[3],Content[1][3]))
                f.write('我的选择:'+ brain.choose[choose] + '\n')
            print('\n我的选择:'+brain.choose[choose])
            brain.Adb_input(choose)
            while(False == brain.Get_right_answer(Content[0])):
                continue
            if os.path.exists('D:\\Answer.txt'):
                os.remove('D:\\Answer.txt')
            with open(r'D:\answer_log.txt','a',encoding='utf-8') as f:
                f.write('正确答案:{}\n'.format(brain.choose[brain.question_db[Content[0]]]))
            if choose == brain.question_db[Content[0]]:
                brain.right_num = brain.right_num + 1
            print('the right answer is {}\n total:{} right_num:{}\n'.format(brain.choose[brain.question_db[Content[0]]],brain.total,brain.right_num))

        if Content[2] == 5:
            print('game is over')
            brain.index = 0
            if os.path.exists('D:\\tmp.txt'):
                os.remove('D:\\tmp.txt')
            time.sleep(15)
            cmd = 'adb shell input swipe {0} {1} {0} {1} {2}'.format(530, 1270, random.randint(500, 550))
            os.system(cmd)
            time.sleep(5)
            cmd = 'adb shell input swipe {0} {1} {0} {1} {2}'.format(530, 1700, random.randint(500, 550))
            os.system(cmd)
            time.sleep(3)
            #break
    except:
        pass






