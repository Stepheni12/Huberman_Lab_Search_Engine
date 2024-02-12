import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import os
from tqdm import tqdm

# Define transcription pipeline
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-medium"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)


# Generate transcriptions
dir_ = "./audios"
all_pods = os.listdir(dir_)

for pod in tqdm(all_pods, desc="Processing", unit="item"):
    full_path = os.path.join(dir_, pod)
    result = pipe(full_path)
    result_txt = result["text"]

    new_file = pod.replace(".mp3", ".txt")
    new_path = os.path.join("./texts", new_file)

    with open(new_path, 'w') as file:
        file.write(result_txt)