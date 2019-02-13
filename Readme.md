# 数行数。

请使用 python3 环境

## 配置文件：(可忽略，使用默认)

```c
[file]
suffix 要扫描的文件名
ignoreDir 要忽略的文件夹
```

## how to use?

1. 填好配置文件 `config.ini`, 其中 `analyzePath` 是要统计的目录
2. CD 到该工具的目录
3. 执行脚本 `python main.py`

## Addition

日志文件 `Out/output.txt` 记录了输出，包含： 层级、文件夹、行数（行数是包含所有子文件以及所有子文件夹的）