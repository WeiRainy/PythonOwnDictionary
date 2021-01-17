# 英汉字典的制作
# 学号：4201993 姓名：卓乐
import csv
#模块导入
Dict = {}
words = []
csv_header = ["单词","释义"]
# 全局变量

def welcome():
    #欢迎
    print('{0:*^60}'.format('*'))
    print('{:*^60}'.format(" Welcome to DIY English Dictionary!"))
    print('{0:*^60}'.format('*'))
    print('已默认导入预置的词典.csv文件作为词典，退出时请保存。')
    print("请输入序号以使用该词典的不同功能:")


def add_word():
    #添加单词
    print("{:-^60}".format(""))
    print("进入添加单词功能，输入0回到主菜单。")

    while 1:
        word = input('请输入单词：')
        if word != '0':
            inter = input('请输入词义：')
            Dict[word] = inter
            print("条目添加成功！\n")
            continue
        else:
            print("{:-^60}".format(""))
            break


def delete():
    #删除单词
    print("{:-^60}".format(""))
    print("进入删除单词功能，输入0回到主菜单。")

    while 1:
        word = input('要删除的单词是：')
        if word != '0':
            if word in Dict:
                print('目标单词:{},对应释义:{}'.format(word, Dict[word]))
                Dict.pop(word)
                print('已删除\n')
                continue
            else:
                print('该单词不在词典中。')
                continue
        else:
            print("{:-^60}".format(""))
            break

def search():
    #搜索
    print("{:-^60}".format(""))
    print("进入删除单词功能，输入0回到主菜单。")

    while 1:
        word = input('要查询的单词是：')
        if word != '0':
            if word in Dict:
                print("{}的释义是：{}\n".format(word,Dict[word]))#完整检索
                continue
            else:
                fuzzy_words = []
                print("\n该单词不在词典中，正在尝试联想查询...")
                for i in Dict:
                    if word[0:2] == i[0:2]:#模糊检索 首二字相同生成模糊列表
                        fuzzy_words.append(i)
                fuzzy_search(fuzzy_words)
                continue
        else:
            print("{:-^60}".format(""))
            break


def fuzzy_search(ls):
    #查询模糊列表
    if len(ls) != 0:
        for i in ls:
            print("{}: {}".format(i, Dict[i]))
        else:
            print("")
    else:
        print("不存在近似单词。\n")


def modify():
    print("{:-^60}".format(""))
    print("进入修改单词功能，输入0回到主菜单。")

    while 1:
        word = input('要修改的单词为：')
        if word != '0':
            if word in Dict:
                inter = input('请输入要修改为的释义：')
                Dict[word] = inter
                print("修改成功，单词'{}'的释义已修改为'{}'\n".format(word, Dict[word]))
                continue
        else:
            print("{:-^60}".format(""))
            break


def view():
    print("词典全部条目：")
    print("{:-^60}".format(""))
    if len(Dict) != 0:
        for i in Dict:
            print("{}: {}".format(i, Dict[i]))
    else:
        print("词典为空。")
    print("{:-^60}".format(""))


def csv_save():
    word = list(Dict.keys())
    ys = list(Dict.values())
    for i in range(len(Dict)):
        words.append([word[i], ys[i]])
    with open("./词典.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(csv_header)
        for j in range(len(words)):
            w.writerow(words[j])


def import_dict():
    with open("./词典.csv", "r") as f:
        w = csv.DictReader(f)
        for row in w:
            Dict[row['单词']] = row['释义']


def IO():
    print("{:-^60}".format(""))
    print("所有文件皆为同目录下的'词典.csv'，每次使用过程只能进行一次导出操作，否则数据会混乱。")
    print("1.导出为CSV词典\n2.导入CSV作为词典")
    num = eval(input('请输入功能序号：'))
    if num == 1:
        csv_save()
        print("{:-^60}".format(""))
    if num == 2:
        import_dict()
        print("{:-^60}".format(""))


def using():
    while (1):
        print("1.添加条目\n2.删除条目\n3.查询单词\n4.修改条目\n5.查看词典\n6.导入导出\n0.退出词典")
        num = eval(input('请输入功能序号：'))
        if num == 0:
            break
        if num == 1:
            add_word()
        if num == 2:
            delete()
        if num == 3:
            search()
        if num == 4:
            modify()
        if num == 5:
            view()
        if num == 6:
            IO()

def main():
    welcome()
    try:
        using()
    except SyntaxError:
        print('输入有误，请重新输入\n')
        using()


if __name__ == '__main__':
    import_dict()
    main()
