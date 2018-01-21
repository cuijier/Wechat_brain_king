#### 使用说明
---
> 
大致思路如下

1. 使用fidder工具抓包，可以看到发送的数据中有sign一串数据，不知道这个数据是如何得来的，所以无法通过python url 来模仿获取数据。


   方式：POST
 
 
   URL：/question/fight/findQuiz
   
   
   ![Alt text](https://github.com/weiqiu/Wechat_brain_king/blob/master/pic/111.png)

2.  抓包发现返回的 js 数据中就是题目和题目的选项，如下，如此可以直接修改fiddler custom rules 抓取 Response 数据保存在本地 tmp 文件中.


    ![Alt text](https://github.com/weiqiu/Wechat_brain_king/blob/master/pic/2.png)

3. python 端 读取tmp文件获取题目和选项，然后通过 百度知道搜索题目，根据选项出现次数制定不同的选择策略，并将答题记录保存在 answer_log.txt 文件中，
4.  自动做出选择之后可以通过adb 命令来自动答题

---
> 答题记录

1. 答题记录举例如下，会先在本地题库搜索题目，如没有记录，再在网络搜索，根据关键词的次数来做出选择，该题结束后也会从Server端获取该题目的正确答案并添加到本地题库


    题目1:马铃薯的原产地是哪个国家或地区？
  
    次数:0A:俄罗斯
  
    次数:0 B:北美洲
  
    次数:7 C:中国
  
  
    次数:7 D:南美洲
  
    我的选择:C
  
    正确答案:D


   题目2:下列属于古代「阿拉伯帝国」首都的是？
   
   
   次数:0A:伊斯坦布尔
   
   
   次数:0 B:利雅得
   
   
   次数:5 C:巴格达
   
   
   次数:0 D:迦太基
   
   
   我的选择:C
   
   
   正确答案:C
   
   题目3:中国大陆地区第二个拥有地铁的城市是？
 
 
   次数:4A:深圳
   
   
   次数:9 B:天津
  
  
    次数:4 C:广州
   
   
    次数:9 D:上海
   
   
    我的选择:B
   
   
    正确答案:B

---
> To do list

1.  JS 脚本 OnBeforeResponse 函数中 File.WriteAllText 函数未加文件锁，如果是高并发response 会多有多个进程都在写这个文件
2.  adb  input swipe 未根据手机实际分辨率做适配，当前写死了
3.  本地题库只是保存在本地了，并未打开起查询作用，起查询作用的只是用了一个dict ，且程序终止就不能使用，待改进
4.  当前做出选择只添加了两条策略，待根据答题 log 中 错误的情况添加新的策略。



        

