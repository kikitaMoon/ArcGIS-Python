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



# 定义一个list继承类
class AthleteList(list):

    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        #self.times = a_times
        self.extend(a_times)

    def top3(self):
        #return(sorted(set([sanitize(t) for t in self.times]))[0:3])
        return(sorted(set([sanitize(t) for t in self]))[0:3])



# 定义打开文件，并且把内容赋值给 Athlete Class
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        # pop函数功能：删除指定位置元素。注意：pop(n)，n指明在列表中的位置，如果pop(),默认弹出最后一个元素(出栈操作）。
        return(AthleteList(templ.pop(0),templ.pop(0),templ))

    except IOError as ioerr:
        print('File Error'+str(ioerr))
        return(None)


james = get_coach_data('james2.txt')






##################################################################################

# 输出结果，调用类的属性（name）和方法（top3）。
print(james.name + "'s fastest times are:" + str(james.top3()))

# 调用继承方法，追加新值，重新输出结果。
james.extend(["0:01"])

print('New: ' + james.name + "'s fastest times are:" + str(james.top3()))
