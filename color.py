#!/usr/bin/env python
# -*- coding: utf-8 -*-
# マインクラフト用のパッケージのインポート
from mcpi.minecraft import Minecraft
# ワールドの読み込み
mc = Minecraft.create()
# プレイヤーの現在位置の読み込み
x, y, z = mc.player.getPos()
# ウールブロックのIDの宣言
mc.setBlock(x+1, y, z, wool, 1)
