#!/usr/bin/env python
# -*- coding: utf-8 -*-
# マインクラフト用のパッケージのインポート
from mcpi.minecraft import Minecraft
# ワールドの読み込み
mc = Minecraft.create()
# プレイヤーの現在位置の読み込み
x, y, z = mc.player.getPos()
# TNTブロックのIDの宣言
tnt = 46
# ブロックの設置
mc.setBlock(x+1, y, z, tnt, 1)
