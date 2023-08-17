import subprocess
import os

def git_commit_and_push(commit_message, repo_path):
    try:
        # 切换到仓库目录
        os.chdir(repo_path)

        # 添加所有文件到暂存区
        subprocess.check_output('git add .', shell=True, stderr=subprocess.STDOUT)

        # 提交所有改动，即使没有任何更改
        subprocess.check_call(f'git commit --allow-empty -m "{commit_message}"', shell=True)

        # 推送改动到远程仓库
        subprocess.check_output('git push', shell=True, stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError as e:
        print("尝试提交和推送更改时出现错误。")
        print("输出:", e.output.decode('utf8'))  # 使用UTF-8编码解码output
        return False  # 表示操作未成功

    return True  # 表示操作成功

git_commit_and_push("update", "/home/liuxxl/Abelliuxl.github.io")