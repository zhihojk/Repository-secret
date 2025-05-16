import gradio as gr
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice

tts = TextToSpeech()

def load_custom_voice():
    voice_samples, conditioning_latents = load_voice("user_voice")
    return voice_samples, conditioning_latents

def generate_voice(text):
    voice_samples, conditioning_latents = load_custom_voice()
    gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, preset="fast")
    tts.save_audio(gen, "output.wav")
    return "output.wav"

demo = gr.Interface(
    fn=generate_voice,
    inputs=gr.Textbox(label="输入文本"),
    outputs=gr.Audio(type="filepath", label="合成音频"),
    title="声音克隆演示",
    description="输入一段文本，生成模仿你声音的语音。"
)

demo.launch()