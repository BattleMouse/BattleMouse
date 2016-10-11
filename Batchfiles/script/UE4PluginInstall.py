# -*- coding: utf-8 -*-

import sys
import os
import shutil

# 引数1 : Live2DのSDKフォルダーパス
# 引数2 : Platform
# 引数3 : vsVersion
# 引数4 : Live2DForDLLの依存フォルダーのパス

inputPath = sys.argv[ 1 ]
outputPath = sys.argv[ 2 ]

# inputPathが空または存在しない場合はエラーとする
try:
    if inputPath == "none":
        raise Exception("[Error] File path is empty.")
    if os.path.isdir(inputPath) == False:
        raise Exception("[Error] File does not exist.")
except Exception as e:
    sys.exit( e.message )

copyfolderName = inputPath.rsplit("\\", 1)[ 1 ]

# パス確認
print( "path check" )
print(( "input Path = %s" ) % ( inputPath ))
print(( "output Path = %s" ) % ( outputPath ))
print(( "copy folder name = %s" ) % ( copyfolderName ))

# すでにフォルダーがある場合は一回削除してからコピー開始
if os.path.isdir(outputPath + "\\" + copyfolderName):
    t = shutil.rmtree(outputPath + "\\" + copyfolderName)

# コピー開始
shutil.copytree(inputPath, outputPath + "\\" + copyfolderName)

print(( "\n%s Copy Complete!!" ) % (copyfolderName))
