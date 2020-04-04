#!/usr/bin/env python
# -*- coding: utf-8 -*-
# マインクラフト用のパッケージのインポート
from mcpi.minecraft import Minecraft
# ワールドの読み込み
mc = Minecraft.create()
# 画面上に文字を表示する
mc.postToChat("Hello World")
