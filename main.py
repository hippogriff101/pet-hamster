def Record():
    music.play(music.builtin_playable_sound_effect(soundExpression.soaring),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_string("Let's Record...")
    basic.show_string("3, 2, 1, GO!")
    record.start_recording(record.BlockingState.BLOCKING)
    basic.show_string("Long Press")
def Sad():
    global greeting
    if greeting == 0:
        basic.show_string("Hello!")
    greeting = 1
    basic.show_string("I feel...")
    basic.show_icon(IconNames.SAD)
    soundExpression.sad.play_until_done()

def on_logo_long_pressed():
    record.play_audio(record.BlockingState.NONBLOCKING)
    basic.show_icon(IconNames.ASLEEP)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def Happy():
    global greeting
    if greeting == 0:
        basic.show_string("Hello!")
    greeting = 1
    basic.show_string("I feel:")
    basic.show_icon(IconNames.HAPPY)
    soundExpression.giggle.play_until_done()

def on_button_pressed_a():
    Evil()
input.on_button_pressed(Button.A, on_button_pressed_a)

def Evil():
    global greeting
    if greeting == 0:
        basic.show_string("Hello!")
    greeting = 1
    basic.show_string("I am EVIL:")
    basic.show_icon(IconNames.ANGRY)
    soundExpression.mysterious.play_until_done()

def on_button_pressed_ab():
    Sad()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Record()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_icon(IconNames.ASLEEP)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    Happy()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

greeting = 0
greeting = 0
basic.show_icon(IconNames.ASLEEP)