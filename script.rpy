# Define characters with names and dialogue colors
define t = Character("Tomoya", color="#1E90FF")      # Tomoya Okazaki
define n = Character("Nagisa", color="#FF69B4")      # Nagisa Furukawa
define u = Character("Ushio", color="#FFB6C1")       # Ushio Okazaki
define a = Character("Akio", color="#FF4500")        # Akio Furukawa
define s = Character("Sanae", color="#FFD700")       # Sanae Furukawa
define su = Character("Sunohara", color="#00CED1")   # Youhei Sunohara
define k = Character("Kyou", color="#DA70D6")        # Kyou Fujibayashi
define to = Character("Tomoyo", color="#C0C0C0")     # Tomoyo Sakagami
define f = Character("Fuko", color="#98FB98")        # Fuko Ibuki
define ko = Character("Kotomi", color="#8A2BE2")     # Kotomi Ichinose
define y = Character("Yukine", color="#4682B4")      # Yukine Miyazawa
define m = Character("Misae", color="#FF6347")       # Misae Sagara
define i = Character("Kouko", color="#32CD32")       # Kouko Ibuki

# Define variables for game mechanics
default light_orbs = 0            # Collected through positive choices to unlock True Ending
default reconciliation = False    # Determines if Tomoya bonds with Ushio

# Backgrounds (placeholders; replace with actual image files)
image bg school_hill = "school_hill.jpg"
image bg classroom = "classroom.jpg"
image bg bakery = "bakery.jpg"
image bg apartment = "apartment.jpg"
image bg hospital = "hospital.jpg"
image bg park = "park.jpg"
image bg field = "field.jpg"
image bg street = "street.jpg"

# Sprites (placeholders; replace with actual sprite files)
image tomoya neutral = "tomoya_neutral.png"
image tomoya happy = "tomoya_happy.png"
image tomoya sad = "tomoya_sad.png"
image nagisa happy = "nagisa_happy.png"
image nagisa sad = "nagisa_sad.png"
image nagisa weak = "nagisa_weak.png"
image ushio happy = "ushio_happy.png"
image ushio sad = "ushio_sad.png"
image akio neutral = "akio_neutral.png"
image sanae neutral = "sanae_neutral.png"
image sunohara neutral = "sunohara_neutral.png"
image kyou neutral = "kyou_neutral.png"
image tomoyo neutral = "tomoyo_neutral.png"
image fuko neutral = "fuko_neutral.png"
image kotomi neutral = "kotomi_neutral.png"

# Music (placeholders; replace with actual audio files)
define audio.school_bgm = "school_bgm.mp3"
define audio.bakery_bgm = "bakery_bgm.mp3"
define audio.sad_bgm = "sad_bgm.mp3"
define audio.happy_bgm = "happy_bgm.mp3"
define audio.field_bgm = "field_bgm.mp3"
define audio.street_bgm = "street_bgm.mp3"  # Added to fix the AttributeError

# Start of the game
label start:
    play music audio.school_bgm fadein 1.0
    scene bg school_hill with fade
    show tomoya neutral
    t "(narration) I walk up this hill every day, but today feels different."
    show nagisa sad at right
    n "Anpan... anpan..."
    t "(narration) There's a girl standing there, muttering about bread."
    
    menu:
        "Talk to her":
            $ light_orbs += 1
            t "Hey, are you okay?"
            n "Oh! Um, yes. I was just... thinking about something."
            t "You looked a bit lost. First day?"
            n "Actually, I'm a third-year too. I've been away for a while."
            t "I'm Tomoya Okazaki."
            n "I'm Nagisa Furukawa. Nice to meet you!"
            "A faint light flickers—a sign of something special beginning."
        "Ignore her":
            t "(narration) Not my business. I'll just keep walking."
            hide nagisa with dissolve
            "Tomoya continues to school, but fate has other plans."
    
    jump school_days

# School Days: Helping Nagisa and meeting other characters
label school_days:
    scene bg classroom with dissolve
    "Tomoya and Nagisa grow closer as they work to restart the drama club."
    show nagisa happy
    n "Tomoya, will you help me with the drama club?"
    
    menu:
        "Help her":
            $ light_orbs += 1
            t "Sure, why not? Could be fun."
            n "Thank you so much, Tomoya!"
            "Another faint light glimmers."
        "Decline":
            t "Sorry, not really my thing."
            n "Oh... okay. I'll try to manage."

    # Interactions with other characters to earn light orbs
    scene bg park with dissolve
    show fuko neutral
    f "Tomoya, want to help me carve starfish for my sister's wedding?"
    
    menu:
        "Help Fuko":
            $ light_orbs += 1
            t "Alright, let's do it."
            f "Yay! You're the best!"
        "Refuse":
            t "Sorry, I'm busy."
            f "Oh, okay..."

    scene bg library with dissolve
    show kotomi neutral
    ko "Tomoya, do you want to study together?"
    
    menu:
        "Study with Kotomi":
            $ light_orbs += 1
            t "Sure, I could use the help."
            ko "Great! Let's start with quantum mechanics."
        "Decline":
            t "Nah, I'm good."
            hide kotomi with dissolve

    scene bg street with dissolve
    show tomoyo neutral
    to "I'm running for student council president. Will you support me?"
    
    menu:
        "Support Tomoyo":
            $ light_orbs += 1
            t "Yeah, I'll help out."
            to "Thank you, Tomoya."
        "Stay out of it":
            t "Politics aren't my thing."
            hide tomoyo with dissolve
    
    jump graduation

# Graduation and Post-Graduation
label graduation:
    scene bg school with fade
    "Graduation day arrives. Tomoya and Nagisa stand together, ready for the future."
    show tomoya happy
    show nagisa happy at right
    t "We did it, Nagisa."
    n "Yes! And now, we can start our new lives."
    
    jump post_graduation

label post_graduation:
    stop music fadeout 1.0
    play music audio.street_bgm fadein 1.0
    scene bg street with fade
    "Tomoya becomes an electrician, while Nagisa helps at the bakery."
    show tomoya neutral
    t "Work’s tough, but it’s honest. Nagisa’s always there to cheer me up."
    
    jump marriage

label marriage:
    scene bg bakery with fade
    play music audio.bakery_bgm fadein 1.0
    show nagisa happy
    n "Tomoya, I want us to get married!"
    t "Yes, let’s do it."
    "They marry in a small ceremony at the bakery."
    
    jump parenthood

label parenthood:
    scene bg apartment with fade
    "A year later, Nagisa is pregnant."
    show nagisa happy
    n "Tomoya! We’re going to have a baby!"
    t "That’s amazing, Nagisa."

    # Nagisa’s illness
    scene bg apartment with dissolve
    "As winter nears, Nagisa’s health declines."
    show nagisa weak
    n "Tomoya… I’m so tired."
    t "Rest, Nagisa. I’ll take care of everything."
    
    jump tragedy

label tragedy:
    stop music fadeout 1.0
    play music audio.sad_bgm fadein 1.0
    scene bg hospital with fade
    "Nagisa gives birth to Ushio but passes away shortly after."
    show tomoya sad
    t "Nagisa… no… this can’t be happening."
    hide nagisa with dissolve
    
    jump depression

label depression:
    scene bg apartment with fade
    "Tomoya falls into depression, leaving Ushio with Akio and Sanae."
    show tomoya sad
    t "I can’t do this without her."
    
    jump reconciliation_choice

label reconciliation_choice:
    scene bg park with fade
    "Five years later, Akio urges Tomoya to reconnect with Ushio."
    show a neutral
    a "Tomoya, Ushio needs her father."
    
    menu:
        "Reconnect with Ushio":
            $ reconciliation = True
            t "You’re right. I’ve been running too long."
            jump ushio_route
        "Stay distant":
            $ reconciliation = False
            t "I can’t face her."
            jump bad_end

label ushio_route:
    scene bg field with fade
    play music audio.field_bgm fadein 1.0
    show ushio happy
    u "Daddy, this place is beautiful!"
    t "Yeah, it is."
    
    # Ushio’s illness
    scene bg hospital with dissolve
    show ushio sad
    u "Daddy, I’m scared."
    t "It’s okay, I’m here."
    
    if light_orbs >= 5:
        "A warm light fills the room."
        jump true_end
    else:
        "Ushio recovers, and Tomoya raises her alone."
        jump normal_end

label normal_end:
    scene bg park with fade
    show tomoya neutral
    show ushio happy at right
    t "We’ll be okay, Ushio. Together."
    "Normal Ending"
    return

label true_end:
    scene bg hospital with fade
    play music audio.happy_bgm fadein 1.0
    "Time rewinds. Nagisa survives."
    show nagisa happy
    n "Tomoya, Ushio, I’m here!"
    t "Nagisa! It’s a miracle!"
    "True Ending"
    return

label bad_end:
    scene bg apartment with fade
    show tomoya sad
    t "I lost everything."
    "Bad Ending"
    return