from git import Repo

# Git 仓库路径
repo_path = '/home/liuxxl/Abelliuxl.github.io'

# 提交的消息
commit_message = '自动提交更改'

# GitHub 账户凭据
username = 'Abelliuxl'
password = '131415978DALIANG'

# 打开 Git 仓库
repo = Repo(repo_path)

# 配置远程仓库
origin = repo.remote(name='origin')
origin_url = origin.url
new_origin_url = origin_url.replace('https://', f'https://{username}:{password}@')
repo.git.remote('set-url', 'origin', new_origin_url)

# 获取当前分支
current_branch = repo.active_branch

# 将所有更改添加到暂存区
repo.git.add(all=True)

# 创建提交
repo.index.commit(commit_message)

# 推送到远程仓库
origin.push(current_branch)