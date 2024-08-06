function Record() {
    music.play(music.builtinPlayableSoundEffect(soundExpression.soaring), music.PlaybackMode.InBackground)
    basic.showString("Let's Record...")
    basic.showString("3, 2, 1, GO!")
    record.startRecording(record.BlockingState.Blocking)
    basic.showString("Long Press")
}

function Sad() {
    
    if (greeting == 0) {
        basic.showString("Hello!")
    }
    
    greeting = 1
    basic.showString("I feel...")
    basic.showIcon(IconNames.Sad)
    soundExpression.sad.playUntilDone()
}

input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    record.playAudio(record.BlockingState.Nonblocking)
    basic.showIcon(IconNames.Asleep)
})
function Happy() {
    
    if (greeting == 0) {
        basic.showString("Hello!")
    }
    
    greeting = 1
    basic.showString("I feel:")
    basic.showIcon(IconNames.Happy)
    soundExpression.giggle.playUntilDone()
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    Evil()
})
function Evil() {
    
    if (greeting == 0) {
        basic.showString("Hello!")
    }
    
    greeting = 1
    basic.showString("I am EVIL:")
    basic.showIcon(IconNames.Angry)
    soundExpression.mysterious.playUntilDone()
}

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    Sad()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    Record()
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showIcon(IconNames.Asleep)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    Happy()
})
let greeting = 0
greeting = 0
basic.showIcon(IconNames.Asleep)
