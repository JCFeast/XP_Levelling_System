import os.path

# XP and Levelling system
# --------------------------------------------------------------------------------------------------------------------


def initial_stats():
    global XP
    global Level
    global level_up_threshold
    global quest_complete

    def reading_xp_from_txt_file():

        global XP
        global splitting_the_xp_string

        XP_file = open("XP_token.txt", "r")
        XP = XP_file.readline()
        splitting_the_xp_string = XP.split(".", -1)
        XP = splitting_the_xp_string[0]
        XP_file.close()

        XP = int(XP)

    def reading_level_up_threshold_from_txt_file():

        global level_up_threshold
        global splitting_the_level_up_threshold_string

        level_up_threshold_file = open("level_up_threshold_token.txt", "r")
        level_up_threshold = level_up_threshold_file.readline()
        splitting_the_level_up_threshold_string = level_up_threshold.split(".", 1)
        level_up_threshold = splitting_the_level_up_threshold_string[0]
        level_up_threshold_file.close()

        level_up_threshold = int(level_up_threshold)

    def reading_level_from_txt_file():

        global Level

        Level_file = open("Level_token.txt", "r")
        Level = Level_file.readline()
        Level_file.close()

        Level = int(Level)

    if os.path.isfile("XP_token.txt") == True:

        reading_xp_from_txt_file()

    else:
        XP = 0

    if os.path.isfile("Level_up_threshold_token.txt") == True:

        reading_level_up_threshold_from_txt_file()

    else:
        level_up_threshold = 100

    if os.path.isfile("Level_token.txt") == True:

        reading_level_from_txt_file()

    else:
        Level = 0

    quest_complete = 0


initial_stats()


def level_up_threshold_increase():
    global level_up_threshold
    global previous_level_up_threshold
    global level_up_threshold_token

    previous_level_up_threshold = level_up_threshold
    level_up_threshold = level_up_threshold * 1.5

    level_up_threshold_token = open("Level_up_threshold_token.txt", "w")
    level_up_threshold_token.write(str(level_up_threshold))


def reset_xp_after_level():
    global XP

    XP = XP - previous_level_up_threshold


def xp_seg_check():
    global xp_seg
    global Level
    global XP_token
    global XP

    level_up_threshold_increase()
    reset_xp_after_level()

    XP_token = open("XP_token.txt", "w")
    XP_token.write(str(XP))

    xp_seg = XP // level_up_threshold

    if xp_seg >= 1:

        level_up_check()

    else:
        level_up()


def level_up_check():
    global Level
    global XP
    global level_up_threshold
    global xp_seg
    global quest_complete

    xp_seg = XP // level_up_threshold

    while quest_complete == 1:

        if XP >= level_up_threshold:

            if xp_seg >= 1:

                Level = Level + 1

                xp_seg_check()

        else:
            quest_complete = 0
            XP_token = open("XP_token.txt", "w")
            XP_token.write(str(XP))
            print("Quest complete!")


def level_up():
    global level_str
    global default_level_up_message
    global XP

    Level_token = open("Level_token.txt", "w")
    Level_token.write(str(Level))

    level_str = str(Level)

    default_level_up_message = "Congratulations! You have leveled up!\nYou are now level: " + level_str + \
                               "\nGood job! You should be proud."

    print(default_level_up_message)


# --------------------------------------------------------------------------------------------------------------------

# Quests
# --------------------------------------------------------------------------------------------------------------------


def shower():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def have_a_shower():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def brush_teeth():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def brush_your_teeth():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def wake_up():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def get_up():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def get_out_of_bed():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def eat_breakfast():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 200

    level_up_check()


def eat_lunch():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 200

    level_up_check()


def eat_dinner():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 200

    level_up_check()


def eat_a_snack():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 150

    level_up_check()


def eat():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 200

    level_up_check()


def go_to_work():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 125

    level_up_check()


def work():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 125

    level_up_check()


def work_out():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 500

    level_up_check()


def pack():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def pack_bags():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def pack_for_tomorrow():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


def do_work():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 125

    level_up_check()


def revise():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 125

    level_up_check()


def do_revision():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 125

    level_up_check()


def level_up_quest():
    global XP
    global quest_complete

    quest_complete = 1

    XP += 100

    level_up_check()


work_out()
