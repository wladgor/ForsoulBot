import pydub


def slowfast_music(file_path, sootnoshenie):
    sound = pydub.AudioSegment.from_file(file_path)
    modified_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * sootnoshenie)
    })

    modified_sound.export(file_path, format="wav")

