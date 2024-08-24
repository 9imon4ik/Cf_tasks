import codeforces_api
import math
import os

cf_api = codeforces_api.CodeforcesApi(os.environ['TOKEN1'], os.environ['TOKEN2'])
tasks = cf_api.problemset_problems(lang="ru")

tags = dict()
for task in tasks['problems']:
    for i in task.to_dict()['tags']:
        tags.setdefault(i, 0)
        tags[i] += 1

maxcnt = max(tags.values())

for i in tags.keys():
    tags[i] = 1 - tags[i] / maxcnt

# for i in tags.keys():
#     tags[i] = math.log(len(tasks['problems']) / tags[i])

tasks_parsed = []
for task in tasks['problems']:
    cur = task.to_dict()
    if cur['rating'] is None:
        cur['rating'] = 0
    task_tags = dict()
    for i in cur['tags']:
        task_tags.setdefault(i, tags[i])
    for i in tags:
        task_tags.setdefault(i, 0.0)
    cur['tags'] = task_tags
    tasks_parsed.append(cur)


def get_rating(x):
    a = (x // 100) * 100
    return min(max(800, a), 3500)


def get_norm_rating(x):
    return (x - 800) / (3500 - 800)


def diff(a, b):
    ans = 0
    for i in tags.keys():
        ans += (a['tags'][i] - b['tags'][i]) ** 2
    ans += (get_norm_rating(a['rating']) - get_norm_rating(b['rating'])) ** 2
    return ans


def find_problem(id, index):
    ind = 0
    for i in tasks_parsed:
        if i['contest_id'] == id and i['index'] == index:
            return ind
        ind += 1
    return -1


def find_similar(task):
    temp = tasks_parsed.copy()

    def comp(b):
        return diff(task, b)

    temp.sort(key=comp)
    # print(diff(task, temp[0]))
    return temp[:11]
