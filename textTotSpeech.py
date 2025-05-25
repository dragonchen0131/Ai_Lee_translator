import requests
import simpleaudio as sa
import os
import atexit


def cleanup(path):
    if os.path.exists(path):
        os.remove(path)  # remove the file if it exists


def text_to_speech(
    text: str, model_ckpt: str, sovits_pth: str, ref_audio: str, output_wav: str
):
    # clean up the output file as the script exits
    atexit.register(cleanup, output_wav)

    # switch to your own models
    requests.get(
        "http://127.0.0.1:9880/set_gpt_weights", params={"weights_path": model_ckpt}
    )
    requests.get(
        "http://127.0.0.1:9880/set_sovits_weights", params={"weights_path": sovits_pth}
    )

    # run TTS tool
    resp = requests.post(
        "http://127.0.0.1:9880/tts",
        json={
            "text": text,
            "text_lang": "zh",
            "ref_audio_path": ref_audio,
            "prompt_lang": "zh",
        },
    )

    # save the output audio
    with open(output_wav, "wb") as f:
        f.write(resp.content)

    # play the output audio
    wave_obj = sa.WaveObject.from_wave_file(output_wav)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # wait until the audio is done playing
