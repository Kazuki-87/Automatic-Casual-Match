#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Hat, Direction, Stick, Tilt
import requests
import time, cv2, os, re, datetime, glob, json
import numpy as np

class Auto_AI_Buttle_victory(ImageProcPythonCommand):
    NAME = 'ヴィクトリーロードモード AI対戦自動周回'
    TAGS = ['イナズマイレブンV']

    def __init__(self, cam):
        super().__init__(cam)
        self.show_value = False

    def do(self):
        print("===================================")
        print("ヴィクトリーロードモード AI対戦自動周回")
        print("===================================")

        #AI対戦をONにしておく

        self.judgePokeConEdition()

        #変数初期化
        line_num = 6
        self.use_LINEnotice = False
        self.is_sleep = True
        
        self.threshold = 0.7

        ret = self.set_param()
        line_num = int(ret[0])
        self.use_LINEnotice = ret[1]
        self.is_sleep = ret[2]
        print(f"周回回数:{line_num}")
        print("スタート！")

        count = 1
        start_time = datetime.datetime.now()
        while True:
            print("-------------------------------")
            print("対戦中…(",count,"回目)")
            cycle_start_time = datetime.datetime.now()
            state = 0

            # 試合終了まで放置
            while True:
                # 試合開始前
                if state == 0:
                    if (self.isContainTemplate('Inazuma_ElevenV/casualMatch.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("カジュアルマッチ画面")
                        self.press(Hat.BTM, 0.1, 0.5)
                        self.wait(1)
                        self.press(Button.A, wait=5)
                        self.press(Hat.BTM, 0.1, 0.5)
                        self.press(Hat.BTM, 0.1, 0.5)
                        self.press(Hat.BTM, 0.1, 0.5)
                    elif (self.isContainTemplate('Inazuma_ElevenV/search.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("探すを選択")
                        self.press(Button.A, wait=5)
                        state = 1
                    else:
                        self.wait(5)
                # 対戦相手募集中
                if state == 1:
                    if (self.isContainTemplate('Inazuma_ElevenV/50.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("レベル50")
                        print("マッチング成功")
                        self.wait(10)
                        self.press(Button.A, wait=3)
                        state = 2
                    elif (self.isContainTemplate('Inazuma_ElevenV/cancel.png', threshold=0.7, use_gray=True, show_value=False)):
                        self.wait(10)
                    elif (self.isContainTemplate('Inazuma_ElevenV/failedNetwork.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("通信失敗")
                        self.press(Button.A, wait=3)
                        self.press(Button.A, wait=3)
                        self.press(Button.A, wait=3)
                        self.wait(3)
                    elif (self.isContainTemplate('Inazuma_ElevenV/NOWLOADING.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("NOWLOADING")
                        if (self.isContainTemplate('Inazuma_ElevenV/pressA.png', threshold=0.8, use_gray=True, show_value=False)):
                            print("press A")
                            print("マッチング成功")
                            self.press(Button.A, wait=3)
                            state = 2
                        else:
                            self.wait(3)
                    elif (self.isContainTemplate('Inazuma_ElevenV/pressA.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("press A")
                        print("マッチング成功")
                        self.press(Button.A, wait=3)
                        state = 2
                    else:
                        self.wait(3)
                # キックオフ手前
                if state == 2:
                    if (self.isContainTemplate('Inazuma_ElevenV/hensei.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("編成終了")
                        self.wait(5)
                        self.press(Button.A, wait=3)
                    elif (self.isContainTemplate('Inazuma_ElevenV/Next.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("次へ")
                        self.wait(2)
                        self.press(Button.A, wait=3)
                    elif (self.isContainTemplate('Inazuma_ElevenV/kickOff.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("キックオフ！")
                        self.wait(5)
                        self.press(Button.B, wait=1)
                        self.press(Hat.BTM, 0.1, 0.5)
                        print("AI監督モード開始")
                        state = 3
                    elif (self.isContainTemplate('Inazuma_ElevenV/T.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("編成終了")
                        self.wait(5)
                        self.press(Button.A, wait=3)
                    else:
                        self.wait(5)
                # 試合開始後
                if state == 3:
                    if (self.isContainTemplate('Inazuma_ElevenV/endGame.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("試合終了です！")
                        self.wait(5)
                        self.press(Button.A, wait=1)
                        self.wait(3)
                    elif (self.isContainTemplate('Inazuma_ElevenV/Next.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("次へ")
                        self.wait(2)
                        self.press(Button.A, wait=1)
                        self.wait(3)
                    elif (self.isContainTemplate('Inazuma_ElevenV/kouhan.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("後半開始")
                        self.wait(5)
                        self.press(Button.A, wait=1)
                        self.wait(3)
                    elif (self.isContainTemplate('Inazuma_ElevenV/casualMatch.png', threshold=0.7, use_gray=True, show_value=False)):
                        print("カジュアルマッチ画面")
                        self.wait(5)
                        break
                    else:
                        self.wait(5)
            
            if count >= line_num:
                break
            else:
                count += 1
            
        if self.use_LINEnotice:
            end_time = datetime.datetime.now()
            self.LINE_text(f'イナイレV AI対戦自動化完了\n【周回数】{line_num}\n【総実行時間】{end_time - start_time}')
        if self.is_sleep:
            self.power_sleep()
        else:
            self.press(Button.HOME, wait=2)
        end_time = datetime.datetime.now()
        print("総実行時間:",end_time - start_time)
        self.finish()
                
    def judgePokeConEdition(self):
        '''
        PokeCon判別プログラム改
        developed by 非公表
        '''        
        if hasattr(self.__class__, 'print_t2b'):    # 継承している関数にprint_t1b関数が含まれるか? print_tb1関数はextension版のみ。
            self.mode_extension = True
            self.jprint("実行環境:Poke-Controller-Modified Extension")
        elif hasattr(self.__class__, 'dialogue6widget'):   # 継承している関数にdialogue6widget関数が含まれるか? dialogue6widget関数はmodified版/extension版のみ。
            self.mode_extension = False
            self.jprint("実行環境:Poke-Controller-Modified")
        else:
            print("本家PokeConでは実行できません。")
            self.finish()

    def jprint(self, text: str):
        '''
        print出力(上書きなし)
        developed by 非公表
        '''
        if self.mode_extension:
            self.print_tbs("a", text + "\n")
        else:
            print(text)

    def jprint_overwrite(self, text: str):
        '''
        print出力(上書きあり)
        developed by 非公表
        '''
        if self.mode_extension:
            self.print_tb("w", text + "\n")
        else:
            print(text)

    def jprint_append(self, text: str):
        '''
        print出力(上書きあり)
        developed by 非公表
        '''
        if self.mode_extension:
            self.print_tb("a", text + "\n")
        else:
            print(text)

    def set_param(self):
        is_set_param = False
        line_num = 6
        is_notice_LINE= True
        is_sleep = True

        while True:
            dialogue_list = [
                ['Entry','周回回数',line_num], #0
                ['Check','LINE通知する？',is_notice_LINE], #1
                ['Check','スリープする？',is_sleep], #2
            ]
            ret = self.dialogue6widget("クロニクルモード AI対戦自動周回設定", dialogue_list)

            if type(ret) == bool:
                if ret == False:
                    self.jprint_append("キャンセルが押されました。プログラムを終了します。")
                    self.finish()
            elif "" not in ret[:-2]:
                break
            else:
                self.jprint("未設定項目があります。再度設定してください。")
                continue
        
        return ret
    
    # スリープモードにする
    def power_sleep(self):
        self.press(Button.HOME, wait=2) #HOMEに戻る
        self.press(Direction.DOWN,wait=0.3)
        self.press(Direction.DOWN,wait=0.3)
        self.press(Direction.DOWN,wait=0.3)
        self.press(Direction.DOWN,wait=0.3)
        self.press(Direction.RIGHT,wait=0.3)
        self.press(Direction.RIGHT,wait=0.3)
        self.press(Direction.RIGHT,wait=0.3)
        self.press(Direction.RIGHT,wait=0.3)
        self.press(Direction.RIGHT,wait=0.3)
        self.press(Direction.RIGHT,wait=0.3)
        self.press(Direction.RIGHT,wait=0.3)
        self.press(Direction.RIGHT,wait=0.3)
        self.press(Direction.RIGHT,wait=0.3)
        self.press(Button.A, wait=1.5)
        self.press(Button.A, wait=1.5)
        self.press(Button.A, wait=1.5)
