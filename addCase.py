from modulefinder import LOAD_CONST


filename = input('请输入事件名称:')
beginTime = input('请输入开始日期:')
endTime = input('请输入结束日期(没有就直接回车):')
place = input('请输入地点:')
death = input('请输入死亡人数:')
lost_raw = input('请输入灾害损失(单位亿):')
type = input('请输入灾害类型:')
freetxt = input('请输入事件内容:')

lost = 100000000 * ((float)(lost_raw))

doc = '''{{{{自然灾害案例
|日期={1}
|开始日期={1}
|结束日期={2}
|地点={3}
|死亡人数={4}
|灾害损失={5}
|自然灾害类型={6}
}}}}

= 事件内容 =
{7}
'''.format(filename, beginTime, endTime, place, death, lost, type, freetxt)

with open('pages/' + filename + '.txt', 'w', encoding = 'utf-8') as f:
  f.write(doc)
  f.close()
