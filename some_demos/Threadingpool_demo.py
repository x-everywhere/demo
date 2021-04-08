#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'guozhuangzhi'

from queue import Queue
import threading
import datetime
import requests
import os

queue = Queue()


IMAGE_LIST = [
    f"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2934236407,2961049037&fm=26&gp=0.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465501219&di=4a9944a693d7f63a1b452b54764ae1d4&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F00%2F86%2F89%2F8956ec576d4d7f5.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465501219&di=05167939c016021ee64c482a17b4ed2b&imgtype=0&src=http%3A%2F%2Fku.90sjimg.com%2Felement_origin_min_pic%2F01%2F34%2F84%2F79573bc42e081c1.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465501218&di=2d009a5deffc313fb9b3043ed8af8996&imgtype=0&src=http%3A%2F%2Fku.90sjimg.com%2Felement_origin_min_pic%2F01%2F35%2F29%2F95573bdcc0d4911.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465501218&di=f5941ef741189d2a6f15ed997e90eaf7&imgtype=0&src=http%3A%2F%2Fku.90sjimg.com%2Felement_origin_min_pic%2F01%2F51%2F22%2F0857458398ca197.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679658&di=296a34d42f157f7e3db24dc263618623&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F01%2F37%2F00%2F75573c359bb0413.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679658&di=6ade66ae1cb74d95678e93251230cf8e&imgtype=0&src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F01%2F18%2F96%2F59051eca0ce28_610.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679658&di=2d26c59e1c2524c2c8355c7cde141c4a&imgtype=0&src=http%3A%2F%2Fku.90sjimg.com%2Felement_origin_min_pic%2F01%2F61%2F16%2F575748bb238a078.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679657&di=c7c43a472971cf35dc9fb709382bb98c&imgtype=0&src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F03%2F59%2F49%2F5bd117b5f1b9f_610.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679657&di=564b2f07b5c2f3441546148f1939967c&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F01%2F49%2F81%2F695744871999d35.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679657&di=5befd0a0b42858d324e7321f41d3e8a9&imgtype=0&src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F00%2F59%2F52%2F585670de3919d_610.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679655&di=05d934863a546ab107d08ace88b9f8fc&imgtype=0&src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F01%2F29%2F78%2F5923a89b0f13f_610.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679655&di=272c86015f8f6a9f40d5e63fe6536586&imgtype=0&src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F01%2F08%2F26%2F59019eb43c0b0_610.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679655&di=605b6f62623c7df022d00d9dbeaf779d&imgtype=0&src=http%3A%2F%2Fwww.51yuansu.com%2Fpic2%2Fcover%2F00%2F27%2F46%2F57feedfe9da75_610.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679655&di=85cd6d411cc78f66c425fe2e35799393&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F01%2F46%2F75%2F28574323fd3a0c9.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679654&di=019d04d2d75a71f48d5762cac93c186e&imgtype=0&src=http%3A%2F%2Fku.90sjimg.com%2Felement_origin_min_pic%2F01%2F39%2F25%2F28573cb2f76d7c2.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679653&di=7c063d57b347a82c42510d66ef97def5&imgtype=0&src=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_130804.png",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679652&di=0debd47055e036af6acb6f456b4862e5&imgtype=0&src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F02%2F24%2F67%2F59bf21cea685f_610.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679652&di=328058d16bc16fb0c21f78e68e1bcde8&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F01%2F34%2F40%2F80573badbedbf82.jpg",
    f"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570465679651&di=6ecd67b285295e416de704d667ac835e&imgtype=0&src=http%3A%2F%2Fku.90sjimg.com%2Felement_origin_min_pic%2F01%2F55%2F26%2F7657475e35e437b.jpg",
]


def get_icon_multi(i):
    image_folder = os.path.abspath(os.path.dirname(__file__))
    r = requests.get(IMAGE_LIST[i])
    if os.path.exists(f"{image_folder}/icon_{200+i}.png"):
        os.remove(f"{image_folder}/icon_{200+i}.png")
    with open(f"{image_folder}/icon_{200+i}.png", "wb") as f:
        f.write(r.content)


class myThread(threading.Thread):

    def __init__(self, task_queue):
        threading.Thread.__init__(self)
        self.task_queue = task_queue

    def run(self):
        while not self.task_queue.empty():
            func, args = self.task_queue.get()
            print("current thread:", threading.current_thread(), func, args)
            func(args)
            self.task_queue.task_done()


def main():
    start_time = datetime.datetime.now()
    q = Queue()
    for i in range(len(IMAGE_LIST)):
        q.put((get_icon_multi, i), block=True)
    for _ in range(len(IMAGE_LIST)):
        t = myThread(q)
        t.setDaemon(False)
        t.start()
    q.join()
    end_time = datetime.datetime.now()
    print(f"Finished in {end_time-start_time} s")


if __name__ == '__main__':
    main()
    # print(len(IMAGE_LIST))
    # q = Queue()
    # q.put(None)
    # q.get()
    # q.get()
    # print(q.empty())
    # time.sleep(2)
    # print_kwargs(target=print_hello, args=(2, 3))
