#!/usr/bin/env python
# -*- coding: utf-8 -*-
# マインクラフト用のパッケージのインポート
from mcpi.minecraft import Minecraft
# sleep関数を使用するためのパッケージのインポート
from time import sleep
# ワールドの読み込み
mc = Minecraft.create()
# TNTブロック・石ブロックのblockTypeIdの宣言
tnt = 46
stone = 1
# プログラムが実行されている間ずっと
while True:
    # クリックしたブロックの座標をblockEventsに代入
    blockEvents = mc.events.pollBlockHits()
    # クリックしたかどうかを確認
    for block in blockEvents:
        # クリックしたブロックが石ブロック(stone)だったら
        if mc.getBlock(block.pos.x, block.pos.y, block.pos.z) == stone:
            # TNTブロック(tnt)に変更する
            mc.setBlock(block.pos.x, block.pos.y, block.pos.z, tnt)
