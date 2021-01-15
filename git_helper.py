# -*- coding: utf-8 -*-
import re
import git

g = git.Git(".")


def git_steps(g, tag, msg):
    g.add('.')
    g.commit("-m", msg)
    print(f'commit -m {msg}')
    g.tag('-a', tag, '-m', tag[1:])
    print(f'创建tag  {tag}')
    g.push(origin, branch, tag)
    print(f'push 完成')


def jekis_bushu(tag):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    import json
    print(tag)
    json_data = {"parameter": {"name": "git_tag", "value": tag},
                 "statusCode": "303",
                 "redirectTo": ".",
                 }
    data = {
        "name": "git_tag",
        "value": tag,
        "statusCode": "303",
        "redirectTo": ".",
        'json': json.dumps(json_data),
        "Submit": "开始构建",
    }
    url = f"http://{host}/view/%E5%85%AC%E5%8F%B8%E5%86%85%E7%BD%91-%E4%B8%B4%E6%97%B6/job/{job}/build?delay=0sec"
    res = requests.post(url, headers=headers, data=data, auth=(user, psd))
    print(res.text)
    # ret = re.search(f'/job/{job}/\d+?/console', res.text)
    # try:
    #     ret = ret.group(0)
    # except Exception:
    #     print(res.text)
    # url = f"http://{host}" + ret
    # print(f"控制台地址为 {url}")
    # from tqdm import tqdm
    #
    # # total参数设置进度条的总长度
    # with tqdm(total=100) as pbar:
    #     cur_process = 0
    #     pbar.set_description('更新进度')
    #     while 1:
    #         data = requests.get(url, headers=headers, auth=(user, psd))
    #         d = re.search("预计剩余时间.*?width:(.*?)%", data.text)
    #         if d:
    #             pbar.update(int(d.groups()[0])-cur_process)
    #         else:
    #             if 'Finished: SUCCESS' in data.text:
    #                 pbar.update(100-cur_process)
    #             else:
    #                 print(data.text)
    #                 print('更新失败，重新更新')
    #                 jekis_bushu(tag)
    #             break
    #         cur_process = int(d.groups()[0])

if __name__ == '__main__':
    import requests
    with open('git_jenkins.txt', 'r', encoding='utf-8') as f:
        origin, branch, host, user, psd, job = [i.strip().split('=')[-1].strip() for i in f.readlines() if i.strip() and not i.startswith('#')]
    # print(g.tag(sort='taggerdate'))
    tags = g.tag(sort='taggerdate').split('\n')
    new_tag = tags[-1]
    print(f'现在的最新标签为: {new_tag}')
    # print(f"最近8个tag为{'  '.join(tags[-2:-10:-1])}")
    create_tag = input('请输入新标签, 不输入直接更新(回退)\n')
    if not create_tag:
        create_tag = input(f"当前tag为{new_tag}, 最近8个tag为{'  '.join(tags[-2:-10:-1])}, 请输入更新的tag\n")
        create_tag = 'v' + create_tag.replace('v', '')
        if create_tag in tags:
            jekis_bushu(create_tag)
        else:
            print('没有这个tag')
    else:
        commit_message = input('请输入commit信息\n')
        create_tag = 'v' + create_tag.replace('v', '')
        git_steps(g, create_tag, commit_message)
        data = input("是否部署到服务器上, 不想部署则输入0\n")
        if data != '0':
            print('部署到服务器上')
            jekis_bushu(create_tag)
        else:
            print('不部署到服务器上')


