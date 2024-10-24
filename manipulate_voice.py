import os
from parselmouth import Sound
from parselmouth.praat import call

def manipulate_voice(
        input_file: str, 
        output_file: str,
        **kwargs
    ):
    """
    Manipulate the voice of the input file and save the manipulated voice to the output file.
    **kwargs: pitch_floor, pitch_ceiling, formant_shift_ratio, new_pitch_median, pitch_range_factor, duration_factor
    """
    pitch_floor = kwargs.get('pitch_floor')
    pitch_ceiling = kwargs.get('pitch_ceiling')
    formant_shift_ratio = kwargs.get('formant_shift_ratio')
    new_pitch_median = kwargs.get('new_pitch_median')
    pitch_range_factor = kwargs.get('pitch_range_factor')
    duration_factor = kwargs.get('duration_factor')
    
    if None in [pitch_floor, pitch_ceiling, formant_shift_ratio, new_pitch_median, pitch_range_factor, duration_factor]:
        raise ValueError('Some parameters are missing. Please provide all the required parameters.')

    sound = Sound(input_file)
    sound = sound.convert_to_mono()
    print(f'Processed {input_file}...')

    manipulated_sound = call(
        sound,
        'Change gender',
        pitch_floor,
        pitch_ceiling,
        formant_shift_ratio,
        new_pitch_median,
        pitch_range_factor,
        duration_factor,
    )
    print(f'Manipulated the voice of {input_file}...')

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    manipulated_sound.save(output_file, 'WAV')
    print(f'Saved the manipulated voice to {output_file}...')
