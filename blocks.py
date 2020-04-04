#!/usr/bin/env python
# -*- coding: utf-8 -*-
# マインクラフト用のパッケージのインポート
from mcpi.minecraft import Minecraft
# ワールドの読み込み
mc = Minecraft.create()
# プレイヤーの現在位置の読み込み
x, y, z = mc.player.getPos()
# ５個分の立方体ブロックを設置
mc.setBlocks(x+1, y, z+1, x+6, y+5, z+6, 1)
