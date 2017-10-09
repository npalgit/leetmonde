#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pm_rd
# Created by yangchao 2017/8/22


def read():
    content = raw_input("")
    arr = [int(i) for i in content.split(' ')]
    ideas = []
    for j in range(arr[2]):
        content = raw_input("")
        temp = [int(i) for i in content.split(' ')]
        temp.append(j)
        ideas.append(temp)
    return process(arr, ideas)


def process(arr, ideas):
    # 结果
    ret = [0 for x in range(arr[2])]
    # 每个rd 当前任务剩余时间
    rds = [0 for x in range(arr[1])]
    # 每个rd 当前进行的任务
    task = [-1 for x in range(arr[1])]

    def _cmp(b, a):
        if a[2] > b[2]:
            return 1
        if a[2] < b[2]:
            return -1
        if a[3] > b[3]:
            return -1
        if a[3] < b[3]:
            return 1
        if a[1] > b[1]:
            return -1
        if a[1] < b[1]:
            return 1
        return 0

    # 按照优先级排序
    new_ideas = sorted(ideas, _cmp)
    # 当前该做的任务
    idea_index = 0
    # 当前时间轴
    timeline = 0
    # 当前所有rd 的最小任务时间
    min_time = 0
    new_min_time = None
    # 没有任务rd 的set
    no_task_rds = set()
    while True:
        if new_min_time is None:
            new_min_time = new_ideas[0][3]
        else:
            new_min_time = max(rds)
        timeline += min_time
        for x in range(arr[1]):
            if x in no_task_rds:
                continue
            rds[x] -= min_time
            if rds[x] == 0:
                # rd 完成了一个任务
                task_id = task[x]
                if task_id > -1:
                    # 记录时间
                    ret[task_id] = timeline
                # 还有任务
                if idea_index < arr[2]:
                    rds[x] = new_ideas[idea_index][3]
                    task[x] = new_ideas[idea_index][4]
                    idea_index += 1
                    if rds[x] < new_min_time:
                        new_min_time = rds[x]
                else:
                    # 没有任务了
                    no_task_rds.add(x)
                    rds[x] = 0
            else:
                if rds[x] < new_min_time:
                    new_min_time = rds[x]
        if new_min_time == 0:
            return ret

        min_time = new_min_time
    return ret


ret = read()
for x in ret:
    print x