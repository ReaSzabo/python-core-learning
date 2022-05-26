# coding: utf-8

array = []
with open("data.txt") as file:
    for line in file:

        episode = []

        # date
        line = line.strip()
        episode.append(line)

        # name of series
        line = next(file).strip()
        episode.append(line)

        # episode
        line = next(file).strip()
        episode.append(line)

        # length
        line = next(file).strip()
        episode.append(line)

        # is watched
        line = next(file).strip()
        episode.append(line)

        array.append(episode)

    print(array)