def loading(    def load_game_progress():
    try:  # Try loading the local save game file ("game_progress.txt").
        with open('game_progress.txt') as f:
            if input("Load your existing game? (Y/N) ").lower() == "y":
                return int(f.readlines()[0])  # If player chose to load game, load last index from save file.
            else:
                print("Starting a new game...")
                return 1  # If player chose to start a new game, set index to 1.
    except:  # If save game file wasn't found, start a new game instead.
        print("Starting a new game...")
    try:
        saved_checkpoint = int(open("save_files.txt").read())
        checkpoints[saved_checkpoint]()
    except FileNotFoundError:
        my_module.run)