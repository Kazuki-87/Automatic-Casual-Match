# Automatic-Casual-Match

このプロジェクトは、PokeControllerを使用してイナズマイレブンVの大会モード「カジュアルマッチ」を自動周回するためのスクリプトです。

## 機能
- カジュアルマッチの自動周回
- AI監督モードの自動操作
- LINE通知機能（オプション）
- 周回終了後のスリープモード設定（オプション）

## 必要環境
- PokeController Modified または PokeController Modified Extension
- Python 3.x
- 必要なライブラリ（`cv2`, `numpy`, `requests` など）

## 使用方法
1. PokeControllerをセットアップし、イナズマイレブンVを起動します。
2. スクリプトを実行し、設定ダイアログで周回回数や通知設定を行います。
3. スクリプトが自動的にカジュアルマッチを周回します。

## 注意事項
- 本スクリプトはPokeController ModifiedまたはModified Extensionでのみ動作します。本家PokeControllerでは動作しません。
- 使用する際は、自己責任でお願いします。

## ファイル構成
- `SerialController/Commands/PythonCommands/inazuma_eleven/Auto_AI_Buttle_victory.py`  
  自動周回のメインスクリプト。
- `SerialController/Template/Inazuma_ElevenV/`  
  画像テンプレートを格納するディレクトリ。

## ライセンス
本プロジェクトのコードは、特定の条件下でのみ使用可能です。詳細はライセンスファイルをご確認ください。