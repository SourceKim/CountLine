# 数行数。

请使用 python3 环境

## 配置文件：(可忽略，使用默认)

```c
[file]
suffix 要扫描的文件名
ignoreDir 要忽略的文件夹
```

## how to use?

1. 将要扫描的工程放到 `./Source` 的文件夹之下
2. 填好配置文件 （默认不需要）
3. CD 到该工具的目录
4. 执行脚本 `python main.py`

## Addition

日志文件 `Out/output.txt` 记录了输出，包含： 层级、文件夹、行数（行数是包含所有子文件以及所有子文件夹的）