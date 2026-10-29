"""ComfyUI nodes for the Qwen Image Edit 2511 workflow."""


class QwenImageEditPrompt:
    """Join an edit request and a preservation instruction for image editing."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "edit_instruction": (
                    "STRING",
                    {"multiline": True, "default": "Change the clothing to a black leather jacket."},
                ),
                "preservation_instruction": (
                    "STRING",
                    {"multiline": True, "default": "Preserve the original identity and facial features."},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "join"
    CATEGORY = "Qwen Image Edit/Prompt"

    def join(self, edit_instruction, preservation_instruction):
        parts = (edit_instruction, preservation_instruction)
        return ("\n".join(part.strip() for part in parts if part.strip()),)


NODE_CLASS_MAPPINGS = {"QwenImageEditPrompt": QwenImageEditPrompt}
NODE_DISPLAY_NAME_MAPPINGS = {"QwenImageEditPrompt": "Qwen Image Edit Prompt"}
