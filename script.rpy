define e = Character("Evelyn")
define j = Character("James")

# Start of the game
label start:

    scene bg room_day
    show evelyn normal at center
    with fade

    e "I knew it would come to this... a choice that can't be undone."

    show james worried at right
    j "Are you sure about this, Evelyn? Once we do it, there's no going back."

    menu:
        "Sacrifice your treasure to save the village":
            jump sacrifice_treasure
        "Keep your treasure and risk everyone":
            jump keep_treasure

label sacrifice_treasure:

    e "I... I have to do it. The village comes first."
    
    scene bg village_safe with fade
    e "The village is safe... but at what cost?"
    
    j "Sometimes the hardest choices are the ones that matter the most."
    
    "THE END: Sacrifice for the greater good."
    return

label keep_treasure:

    e "I... I can't let go. Maybe they'll understand..."
    
    scene bg village_destroyed with fade
    e "The village suffered because of my choice."
    
    j "Some sacrifices are unavoidable, and we learn the hard way."
    
    "THE END: Greed over duty."
    return
