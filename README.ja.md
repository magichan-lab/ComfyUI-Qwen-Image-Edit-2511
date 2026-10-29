# ComfyUI-Qwen-Image-Edit-2511

[English](README.md)

ComfyUI で **Qwen-Image-Edit-2511** を使う Image2Image ワークフローです。編集指示と元画像で保持したい要素を結合するカスタムノードを 1 個同梱します。画像編集エンコーダー、サンプラー、画像入出力には ComfyUI 標準ノードを使います。モデルと入力画像は同梱していません。

## リポジトリ構成

```text
├── __init__.py                         # Qwen Image Edit Prompt カスタムノード
├── workflows/
│   └── qwen_image_edit_2511.json      # ComfyUI ワークフロー
├── pyproject.toml                      # Comfy Registry 用メタデータ
├── LICENSE
├── README.md
└── README.ja.md
```

## 必要な環境とモデル

- 標準ノード `TextEncodeQwenImageEditPlus` を含む新しい ComfyUI。
- ワークフローで選択されている以下のモデルファイル。

  | ローダー | ファイル | 配置先 |
  | --- | --- | --- |
  | `UNETLoader` | `qwen_image_edit_2511_int8_convrot.safetensors` | `ComfyUI/models/diffusion_models/` |
  | `CLIPLoader` | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `ComfyUI/models/text_encoders/` |
  | `VAELoader` | `qwen_image_vae.safetensors` | `ComfyUI/models/vae/` |

既定の拡散モデルは[コミュニティ製 INT8 ConvRot 版](https://huggingface.co/supermind/int8_convrot_models/blob/main/diffusion_models/qwen/qwen_image_edit_2511_int8_convrot.safetensors)です。[テキストエンコーダー](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)と [VAE](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors) は Comfy-Org から入手できます。ダウンロード前に、各モデルの利用条件と必要なハードウェアを確認してください。このリポジトリの MIT ライセンスは、同梱ファイルにのみ適用されます。

互換性のある別の Qwen-Image-Edit-2511 拡散モデルを使う場合は、読み込み後に `UNETLoader` で選び直してください。現在のサンプラー設定は開始点であり、モデルを替えた場合に同一結果になるとは限りません。

## インストールと使い方

1. [このリポジトリ](https://github.com/magichan-lab/ComfyUI-Qwen-Image-Edit-2511)を `ComfyUI/custom_nodes/ComfyUI-Qwen-Image-Edit-2511/` に clone し、ComfyUI を再起動します。追加の Python パッケージは不要です。
2. 上記のフォルダーにモデルを配置するか、既存の互換モデルを選択します。
3. [`workflows/qwen_image_edit_2511.json`](workflows/qwen_image_edit_2511.json) を ComfyUI のキャンバスにドラッグします。
4. `LoadImage` で入力画像を選択します。保存されている `reference.png` は仮のファイル名で、画像は同梱していません。
5. **Qwen Image Edit Prompt** の 2 つの欄を編集し、モデルと出力解像度を確認して実行します。結果は通常の ComfyUI 出力フォルダーに保存されます。

プロンプトノードは空欄を除いて 2 つの文を改行で結合します。`edit_instruction` は変更内容、`preservation_instruction` は保持する要素です。元画像は Qwen の編集エンコーダーに入力されます。サンプラーには 1024 × 1024 の空の潜在画像を渡しているため、出力サイズは入力画像ではなく `EmptySD3LatentImage` で決まります。

## ComfyUI Manager / Registry への公開

このリポジトリは、1 つのカスタムノードパッケージとしてインストールできる構成です。Comfy Registry への公開には次の作業が必要です。

1. [GitHub リポジトリ](https://github.com/magichan-lab/ComfyUI-Qwen-Image-Edit-2511)にファイルを push します。
2. [Comfy Registry](https://registry.comfy.org/) で Publisher を作り、`pyproject.toml` の `YOUR_PUBLISHER_ID` を実際の ID に変更します。リポジトリ URL は `[project.urls]` に設定済みです。
3. `comfy node publish` または[公式ドキュメントの GitHub Action](https://docs.comfy.org/registry/publishing) で公開します。Registry API キーが必要です。現在の ComfyUI Manager は Registry のパッケージ一覧を利用します。

[従来の Manager 一覧への登録](https://docs.comfy.org/custom-nodes/backend/manager)には、GitHub 公開後に Manager の `custom-node-list.json` へ登録する Pull Request が必要です。このリポジトリから外部サービスへの公開・登録はまだ行っていません。

## ライセンス

このリポジトリのワークフロー、カスタムノード、文書は [MIT License](LICENSE) で公開します。モデルの重みには、それぞれの配布元のライセンスが適用されます。
