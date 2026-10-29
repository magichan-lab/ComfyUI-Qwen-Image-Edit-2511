# ComfyUI-Qwen-Image-Edit-2511

[日本語](README.ja.md)

An image-to-image workflow for **Qwen-Image-Edit-2511** in ComfyUI, with one small custom node that combines an edit request and an instruction to preserve parts of the source image. The workflow uses ComfyUI's built-in Qwen image edit encoder, sampler, and image nodes. It does not include model weights or an example input image.

## Repository layout

```text
├── __init__.py                         # Qwen Image Edit Prompt custom node
├── workflows/
│   └── qwen_image_edit_2511.json      # ComfyUI UI workflow
├── pyproject.toml                      # Comfy Registry metadata
├── LICENSE
├── README.md
└── README.ja.md
```

## Requirements

- A recent ComfyUI version with the built-in `TextEncodeQwenImageEditPlus` node.
- Model files selected in the workflow's loaders:

  | Loader | File | Put in |
  | --- | --- | --- |
  | `UNETLoader` | `qwen_image_edit_2511_int8_convrot.safetensors` | `ComfyUI/models/diffusion_models/` |
  | `CLIPLoader` | `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `ComfyUI/models/text_encoders/` |
  | `VAELoader` | `qwen_image_vae.safetensors` | `ComfyUI/models/vae/` |

The workflow's default diffusion model is the [community INT8 ConvRot build](https://huggingface.co/supermind/int8_convrot_models/blob/main/diffusion_models/qwen/qwen_image_edit_2511_int8_convrot.safetensors). The [text encoder](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) and [VAE](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors) are available from Comfy-Org. Check each model's own terms and hardware requirements before downloading. The repository's MIT license covers only the files in this repository.

You can choose another compatible Qwen-Image-Edit-2511 diffusion model in `UNETLoader` after loading the workflow. The workflow's current sampler settings are starting values, not a guarantee of identical results with other model variants.

## Install and run

1. Clone [this repository](https://github.com/magichan-lab/ComfyUI-Qwen-Image-Edit-2511) into `ComfyUI/custom_nodes/ComfyUI-Qwen-Image-Edit-2511/` and restart ComfyUI. There are no additional Python packages to install.
2. Download the model files into the folders above, or select compatible files already installed.
3. Drag [`workflows/qwen_image_edit_2511.json`](workflows/qwen_image_edit_2511.json) onto the ComfyUI canvas.
4. In `LoadImage`, select your own input image. The saved `reference.png` value is only a placeholder; that image is not shipped here.
5. Edit the two text fields in **Qwen Image Edit Prompt**, check the model selections and output resolution, then queue the workflow. `SaveImage` writes to the usual ComfyUI output folder.

The prompt node joins nonempty fields with a newline. `edit_instruction` describes the change; `preservation_instruction` describes details to retain. The source image feeds the Qwen edit encoder. The sampler starts from an empty 1024 × 1024 latent, so output size is controlled by `EmptySD3LatentImage` rather than by the input image.

## ComfyUI Manager / Registry publishing

The repository is prepared for installation as one custom node package. To publish it to the Comfy Registry:

1. Push the files to the [GitHub repository](https://github.com/magichan-lab/ComfyUI-Qwen-Image-Edit-2511).
2. Create a publisher in the [Comfy Registry](https://registry.comfy.org/). Replace `YOUR_PUBLISHER_ID` in `pyproject.toml` with the publisher ID. The repository URL is already set under `[project.urls]`.
3. Publish with `comfy node publish` or the [documented GitHub Action](https://docs.comfy.org/registry/publishing). A Registry API key is required. The Registry supplies ComfyUI Manager's current package catalog.

The [legacy Manager listing](https://docs.comfy.org/custom-nodes/backend/manager) instead requires a pull request to Manager's `custom-node-list.json` after the public GitHub URL exists. Publishing to either catalog is an external step and has not been performed by this repository.

## License

The workflow, custom node, and documentation in this repository are available under the [MIT License](LICENSE). Model weights are distributed separately under their respective licenses.
