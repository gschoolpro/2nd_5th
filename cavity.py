#!/usr/bin/env python
# -*- coding: utf-8 -*-
# マインクラフト用のパッケージのインポート
from mcpi.minecraft import Minecraft
# ワールドの読み込み
mc = Minecraft.create()
# プレイヤーの現在位置の読み込み
x, y, z = mc.player.getPos()
# 5 x 5 x 5の立方体ブロックを設置
mc.setBlocks(x+1, y+1, z+1, x+6, y+6, z+6, 1)
# 4 x 4 x 4の空気ブロックを設置
mc.setBlocks(x+2, y+2, z+2, x+5, y+5, z+5, 0)
