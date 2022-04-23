#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # 1. feladat
    with open("tavirathu13.txt") as file:

        # 2. feladat
        print("2. feladat")
        last_time = 0
        selected_city = "BP"
        for line in file:
            line = line.strip()
            line = line.split()
            city = line[0]
            time = line[1]
            wind = line[2]
            temperature = int(line[3])
            if city == selected_city:
                last_time = time

        print("Utolsó mérési adat a megadott településről: "
              + last_time[0] + last_time[1] + ":" + last_time[2] + last_time[3])


        # 3. feladat
        print("3. feladat")

        file.seek(0)

        min_temp = 999999999
        min_temp_city = ""
        min_temp_time = ""
        for line in file:
            line = line.strip()
            line = line.split()
            city = line[0]
            time = line[1]
            wind = line[2]
            temperature = int(line[3])
            if temperature < min_temp:
                min_temp = temperature
                min_temp_city = city
                min_temp_time = time

        print("Legalacsonyabb hőmérséklet: " + min_temp_city + " " +
              min_temp_time[0] + min_temp_time[1] + ":" + min_temp_time[2] + min_temp_time[3] + " " +
              str(min_temp) + " fok")


        file.seek(0)
        max_temp = -999999999
        max_temp_city = ""
        max_temp_time = ""
        for line in file:
            line = line.strip()
            line = line.split()
            city = line[0]
            time = line[1]
            wind = line[2]
            temperature = int(line[3])
            if temperature > max_temp:
                max_temp = temperature
                max_temp_city = city
                max_temp_time = time

        print("Legalacsonyabb hőmérséklet: " + max_temp_city + " " +
              max_temp_time[0] + max_temp_time[1] + ":" + max_temp_time[2] + max_temp_time[3] + " " +
              str(max_temp) + " fok")


        # 4. feladat
        print("4. feladat")
        file.seek(0)

        has_0 = False
        for line in file:
            line = line.strip()
            line = line.split()
            city = line[0]
            time = line[1]
            wind = line[2]
            temperature = int(line[3])
            if wind == "00000":
                has_0 = True
                print(city + " " + time[0] + time[1] + ":" + time[2] + time[3])

        if has_0 == True:
            print("Nem volt szélcsend a mérések idején.")


        # 5. feladat
        print("5. feladat")

        file.seek(0)
        cities = {}

        # a lehetséges városok kigyűjtése
        for line in file:
            line = line.strip()
            line = line.split()
            city = line[0]
            time = line[1]
            wind = line[2]
            temperature = int(line[3])

            cities[city] = []

        file.seek(0)

        # városonként min, max és sum hőmérséklet

        for current_city in cities.items():
            city_name = current_city[0]
            sum = 0
            avg_counter = 0
            min = 9999999
            max = -9999999
            has_01 = False
            has_07 = False
            has_13 = False
            has_19 = False



            for line in file:
                line = line.strip()
                line = line.split()
                city = line[0]
                time = line[1]
                wind = line[2]
                temperature = int(line[3])

                hour = time[0] + time[1]

                if city == city_name:

                    if hour == '01':
                        has_01 = True
                    if hour == '07':
                        has_07 = True
                    if hour == '13':
                        has_13 = True
                    if hour == '19':
                        has_19 = True

                    if hour in ['01', '07', '13', '19']:
                        sum = sum + temperature
                        avg_counter = avg_counter + 1
                    if min > temperature:
                        min = temperature
                    if max < temperature:
                        max = temperature

            file.seek(0)

            if has_01 and has_07 and has_13 and has_19:
                print(city_name + " Középhomerseklet: " + str(sum / avg_counter) +", Hőmérséklet ingadozás: " + str(max-min))
            else:
                print(city_name + " Középhomerseklet: NA, Hőmérséklet ingadozás: " + str(max-min))

        file.seek(0)
