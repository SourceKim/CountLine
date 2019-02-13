#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import os, sys, json

try:
    import configparser
except:
    import ConfigParser as configparser

global configs
global outputFile0

def isLineComment(line):
    
    return line.startswith("//")

def isBlockComment(line):
    return line.startswith("/*")

def isComment(line):

    return isLineComment(line) or isBlockComment(line)

def isBlank(line):
    
    # stripLine = line.strip()
    stripLine = line # 在外部 strip 掉
    isBlank = len(stripLine) == 0
    return isBlank

def withBlockEnd(line):

    return ("*/" in line)

def doCountLines(path):
    
    # print(" == " + path + "==")

    lineCommentCount = 0
    blockCommentCount = 0
    blankLineCount = 0
    codeLineCount = 0

    theFile = open(path, "r")
    lines = theFile.readlines()

    seekingBlockEnd = False # 是否正在找寻 快注释 结束标记 */

    i = 0
    for line in lines:
        line = line.strip() # 先在这里去除首尾空格

        if seekingBlockEnd:
            # 正在找寻 快注释 结束标记 */
            if withBlockEnd(line):
                seekingBlockEnd = False
            blockCommentCount += 1 # 即使找到了也要 +1

        else:

            if isBlank(line):
                blankLineCount += 1
                # print("line " + str(i) + " blank")

            elif isLineComment(line):
                lineCommentCount += 1
                # print("line " + str(i) + " line comment")

            elif isBlockComment(line):
                blockCommentCount += 1
                seekingBlockEnd = True

                # print("line " + str(i) + " block comment")

            else:
                codeLineCount += 1
                # print("line " + str(i) + " code")

        i += 1

    # 输出结果

    # print("Line comment count: " + str(lineCommentCount))
    # print("Block comment count: " + str(blockCommentCount))
    # print("Blank lines count: " + str(blankLineCount))
    # print("Code lines count: " + str(codeLineCount))

    return codeLineCount

def record(path, depth, count):
    prefixPrint = "--" * depth
    res = str(depth) + prefixPrint + " " + path + " " + str(count) + "\r"
    outputFile0.write(res)


def countLines(path, depth):

    fds = os.listdir(path)

    suffixFilter = configs["file"]["suffix"]
    ignoreDir = json.loads(configs["file"]["ignoreDir"])

    count = 0

    for fd in fds:

        totalPath = os.path.join(path, fd)

        # 检验要忽略的文件夹
        if fd in ignoreDir:
            print("ignore " + totalPath)
            continue

        if not os.path.isdir(totalPath):
        # ==== 如果不是文件夹 =====

            fdSuffix = fd.split(".")[-1]
            if fdSuffix not in suffixFilter:
                # 不在配置文件的 suffix 列出
                print(fd + " is no need to parse")
                continue
            else:
                count += doCountLines(totalPath)

        else:
            # ==== 如果是文件夹，则递归 =====
            nextDepth = depth + 1
            count += countLines(totalPath, nextDepth)

    record(path, depth, count)
    return count


if __name__ == "__main__":

    rootPath = "./Source"

    pathExist = os.path.exists(rootPath)

    if not pathExist:
        print("No such path")
        exit(5)

    # load configs
    global configs
    configs = configparser.ConfigParser()
    configs.read("config.ini")

    # load outputs
    global outputFile0
    outputFile0 = open("./Out/output.txt", "w")
    
    countLines(rootPath, 0)