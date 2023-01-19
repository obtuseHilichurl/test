# 1月11日笔记
> 今天学习了==git==的使用，创建了==github==账户。以下是今日笔记
## 部分==linux==命令学习

1. cd  改变目录到（后面写路径），直接cd进入默认目录
2. cd ..  （注意要加空格）回退到上一个目录
3. pwd  显示当先所在的目录路径
4. ls(||)  列出当前目录所有文件，(||)使得内容更详细
5. touch   在当前目录新建一个文件，后面写文件名
6. rm  删除一个文件，后面写文件名
7. mkdir  新建一个目录（文件夹）
8. rm -r  删除一个目录（文件夹），后面写文件夹名
9. mv  移动文件（使用格式：mv 文件路径 目标路径）
10. reset  重新初始化终端/清屏
11. clear  清屏（git控制台的屏）
12. history  查看命令历史
13. help  帮助
14. exit  退出
15. #表示注释

## 部分==git==的命令
1. git config -l  查看git的配置(l代表list)

2. git config --global user.name "设置用户名"

3. git config --global user.email "设置用户邮箱" 

4. git config --global --list查看用户配置（名+邮）

5. git init  初始化（在当前目录生成.git文件夹）

6. git add .  把当前目录内容传进暂存区

7. git commit -m（提交信息）

8. git clone [url] 克隆远程仓库一个项目至本地（[url]表示源地址）

9. git status  查看目录中文件状态：

   （1）untracked：文件在文件夹中，但不在库中

   （2）unmodify：文件已入库，未修改（与本地库相同）

   （3）modified：文件已修改，与库中不同

   （4）stage：文件进入暂存区

10. 额外补充（https://blog.csdn.net/weixin_64608867/article/details/126358076）


## git基本理论

> git在本地有三个工作区域：工作目录、暂存区、资源库（还有远程的git仓库）。

对于工作目录里的文件，先用git add.（或git add 名）将目录（文件）内容传进暂存区，再用git commit将暂存区内传进资源库（本地库），再用git push将本地库传进远程库。

对于远程库里的文件，用git pull传进本地库，用git reset传进暂存区，再用git checkout传入工作区（若有相同文件会替换）

![1](https://hhhaa114514-1919810-1316522227.cos.ap-guangzhou.myqcloud.com/img/1.png)

## 文件忽略

![](https://hhhaa114514-1919810-1316522227.cos.ap-guangzhou.myqcloud.com/img/2.png)

