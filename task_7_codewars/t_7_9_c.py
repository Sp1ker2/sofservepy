def are_you_playing_banjo(name):
    # Implement me!
    for i in range(len(name)):

        if name[i].lower() == 'r':
            return name + " plays banjo"
        else:
            return name + " does not play banjo"
    return name
