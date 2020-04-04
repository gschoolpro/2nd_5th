#!/usr/bin/env python
# -*- coding: utf-8 -*-
# マインクラフト用のパッケージのインポート
from mcpi.minecraft import Minecraft
# ワールドの読み込み
mc = Minecraft.create()
# プレイヤーの現在位置の読み込み
x, y, z = mc.player.getPos()
# プレイヤーの移動
mc.player.setPos(x, y+100, z)
