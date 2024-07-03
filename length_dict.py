import os
import json
directory = '/Users/wangaiyuan/PycharmProjects/search/data'  # 替换为你的文件目录路径
num_files = 44970  # 文件数量
dict={}
for num in range(1,num_files+1):
    filepath=os.path.join(directory,str(num))
    if not os.path.join(directory,str(num)):
        print(f"文件不存在：{filepath}")
        continue
    try:
        with open(filepath, 'r', encoding='gbk') as f:
            content = f.read()
            words = content.strip().split()  # 分词
            sum=0
            for word in words:
                sum+=1
            dict[int(num)]=int(sum)
    except Exception as e:
        print(f"读取文件时出错: {filepath}, 错误: {e}")

with open('length.json', 'w', encoding='utf-8') as f:
    json.dump(dict, f, ensure_ascii=False, indent=4)

