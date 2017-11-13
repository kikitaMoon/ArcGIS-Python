#-*-coding:utf-8 -*-
__author__ = 'kikita'




# 清理数据，判断数据的分隔符，并返回分隔符是.的数据。
def sanitize(time_string):

    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins,secs) = time_string.split(splitter)
    return(mins + '.' + secs)


# 定义 Athlete Class，类的属性有name,dob,times
class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    # 定义一个取时间前三的方法
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])

    # 定义一个添加单个新时间的方法
    def addtime(self,newtime):
        return(self.times.append(newtime))

    # 定义一个添加一个或者多个新时间的方法
    def addtimes(self,newtimes):
        return(self.times.extend(newtimes))



# 定义打开文件，并且把内容赋值给 Athlete Class
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        # pop函数功能：删除指定位置元素。注意：pop(n)，n指明在列表中的位置，如果pop(),默认弹出最后一个元素(出栈操作）。
        return(Athlete(templ.pop(0),templ.pop(0),templ))

    except IOError as ioerr:
        print('File Error'+str(ioerr))
        return(None)



james = get_coach_data('james2.txt')


# 输出结果，调用类的属性（name）和方法（top3）。
print(james.name + "'s fastest times are:" + str(james.top3()))

# 调用新增的方法 addtime 和 addtimes
james.addtime('1.2')
print(james.name + "'s fastest times are:" + str(james.top3()))

james.addtimes(['1.82','1.93'])
print(james.name + "'s fastest times are:" + str(james.top3()))