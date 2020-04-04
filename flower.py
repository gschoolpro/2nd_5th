#!/usr/bin/env python
# -*- coding: utf-8 -*-
# マインクラフト用のパッケージのインポート
from mcpi.minecraft import Minecraft
# sleep関数を使用するためのパッケージのインポート
from time import sleep
# ワールドの読み込み
mc = Minecraft.create()
# 花ブロックのblockTypeIdの宣言
flower = 38
# プログラムが実行されている間ずっと
while True:
    # プレイヤーの現在位置の読み込み
    x, y, z = mc.player.getPos()
    # プレイヤーのいる位置にフラワーブロックを設置
    mc.setBlock(x, y, z, flower)
    sleep(0.1)
