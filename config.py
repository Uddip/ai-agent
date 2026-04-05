MAX_CHARS = 10000
WORKING_DIR = "./calculator"
GEMINI_2_0_FLASH = "gemini-2.0-flash-001"
GEMINI_2_0_FLASH_LITE = "gemini-2.0-flash-lite-001"
GEMINI_3_1_FLASH_LITE_PREVIEW = "gemini-3.1-flash-lite-preview"

def trunc_message(file_path):
    return f"[...File \"{file_path}\" truncated at 10000 characters]"
