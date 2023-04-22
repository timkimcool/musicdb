def join_items(item, results):
    if item in results:
        if item == "tracks":
            return ", ".join([item["name"] for item in results[item]["items"]])
        return ", ".join([item["name"] for item in results[item]])
    else:
        return "NONE"


def album_print(header, results, pipe=False):
    # KEYS
    # 'album_group', 'album_type', 'artists', 'available_markets', 'copyrights', 'external_ids',
    # 'external_urls', 'genres', 'href', 'id', 'images', 'label', 'name', 'popularity',
    # 'release_date', 'release_date_precision', 'total_tracks', 'tracks', 'type', 'uri'
    new_list = []
    if header:
        print("@@@@@@@@@@@@@@@@@@@@\n", header + "\n@@@@@@@@@@@@@@@@@@@@")
    for result in results:
        new_results = {}
        new_results["name"] = result.get("name", "")
        new_results["popularity"] = result.get("popularity", "")
        new_results["album_group"] = result.get("album_group", "")
        new_results["album_type"] = result.get("album_type", "")
        new_results["artists"] = join_items("artists", result)
        new_results["label"] = result.get("label", "")
        new_results["total_tracks"] = result.get("total_tracks", "")
        new_results["tracks"] = join_items("tracks", result)
        new_results["release_date"] = result.get("release_date", "")
        new_results["type"] = result.get("type", "")
        new_results["genres"] = result.get("genres", "")

        new_list.append(new_results)

    if pipe:
        header = ""
        first = True
        for new_results in new_list:
            result = ""
            for key in new_results.keys():
                header += key + "|"
                result += str(new_results[key]) + "|"
            if first:
                print(header[0:-1])
                first = False
            print(result[0:-1])
    else:
        for new_results in new_list:
            print("@@@")
            for key in new_results.keys():
                print(key, "-", new_results[key])


def track_print(header, results, pipe=False):
    # KEYS
    # 'album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit',
    # 'external_ids', 'external_urls', 'href', 'id', 'is_local', 'name', 'popularity',
    # 'preview_url', 'track_number', 'type', 'uri'
    new_list = []
    if header:
        print("@@@@@@@@@@@@@@@@@@@@\n", header + "\n@@@@@@@@@@@@@@@@@@@@")
    for result in results:
        new_results = {}
        new_results["name"] = result.get("name", "")
        new_results["popularity"] = result.get("popularity", "")
        new_results["album"] = result.get("album", {}).get("name", "")
        new_results["artists"] = join_items("artists", result)
        new_results["disc_number"] = result.get("disc_number", "")
        new_results["duration_ms"] = result.get("duration_ms", "")
        new_results["explicit"] = result.get("explicit", "")
        new_results["track_number"] = result.get("track_number", "")
        new_results["type"] = result.get("type", "")
        new_results["release_date"] = result.get("album", {}).get("release_date")

        new_list.append(new_results)

    if pipe:
        header = ""
        first = True
        for new_results in new_list:
            result = ""
            for key in new_results.keys():
                header += key + "|"
                result += str(new_results[key]) + "|"
            if first:
                print(header[0:-1])
                first = False
            print(result[0:-1])
    else:
        for new_results in new_list:
            print("@@@")
            for key in new_results.keys():
                print(key, "-", new_results[key])


def track_feature_print(header, results, pipe=False):
    # KEYS
    # 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
    # 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href',
    # 'analysis_url', 'duration_ms', 'time_signature'
    new_list = []
    if header:
        print("@@@@@@@@@@@@@@@@@@@@\n", header + "\n@@@@@@@@@@@@@@@@@@@@")
    for result in results:
        new_results = {}
        new_results["danceability"] = result.get("danceability", "")
        new_results["energy"] = result.get("energy", "")
        new_results["key"] = result.get("key", "")
        new_results["loudness"] = result.get("loudness", "")
        new_results["mode"] = result.get("mode", "")
        new_results["energy"] = result.get("energy", "")
        new_results["speechiness"] = result.get("speechiness", "")
        new_results["acousticness"] = result.get("acousticness", "")
        new_results["instrumentalness"] = result.get("instrumentalness", "")
        new_results["liveness"] = result.get("liveness", "")
        new_results["valence"] = result.get("valence", "")
        new_results["tempo"] = result.get("tempo", "")
        new_results["type"] = result.get("type", "")

        new_list.append(new_results)

    if pipe:
        header = ""
        first = True
        for new_results in new_list:
            result = ""
            for key in new_results.keys():
                header += key + "|"
                result += str(new_results[key]) + "|"
            if first:
                print(header[0:-1])
                first = False
            print(result[0:-1])
    else:
        for new_results in new_list:
            print("@@@")
            for key in new_results.keys():
                print(key, "-", new_results[key])


def artist_print(header, results, pipe=False):
    # KEYS
    # 'external_urls', 'followers', 'genres', 'href', 'id', 'images', 'name', 'popularity',
    # 'type', 'uri'
    new_list = []
    if header:
        print("@@@@@@@@@@@@@@@@@@@@\n", header + "\n@@@@@@@@@@@@@@@@@@@@")
    for result in results:
        new_results = {}
        new_results["name"] = result.get("name", "")
        new_results["popularity"] = result.get("popularity", "")
        new_results["genres"] = result.get("genres", "")
        new_results["type"] = result.get("type", "")

        new_list.append(new_results)

    if pipe:
        header = ""
        first = True
        for new_results in new_list:
            result = ""
            for key in new_results.keys():
                header += key + "|"
                result += str(new_results[key]) + "|"
            if first:
                print(header[0:-1])
                first = False
            print(result[0:-1])
    else:
        for new_results in new_list:
            print("@@@")
            for key in new_results.keys():
                print(key, "-", new_results[key])


def playlist_print(header, results, pipe=False):
    # KEYS
    # 'collaborative', 'description', 'external_urls', 'followers', 'href', 'id', 'images',
    # 'name', 'owner', 'primary_color', 'public', 'snapshot_id', 'tracks', 'type', 'uri'
    new_list = []
    if header:
        print("@@@@@@@@@@@@@@@@@@@@\n", header + "\n@@@@@@@@@@@@@@@@@@@@")
    for result in results:
        new_results = {}
        new_results["collaborative"] = result.get("collaborative", "")
        new_results["name"] = result.get("name", "")
        new_results["owner"] = result["owner"]["type"] + "," + result["owner"]["display_name"]
        new_results["type"] = result.get("type", "")
        new_results["external_urls"] = result.get("external_urls", "")
        new_results["track_count"] = len(result.get("tracks", ""))
        new_results["total"] = result.get("total")

        new_list.append(new_results)

    if pipe:
        header = ""
        first = True
        for new_results in new_list:
            result = ""
            for key in new_results.keys():
                header += key + "|"
                result += str(new_results[key]) + "|"
            if first:
                print(header[0:-1])
                first = False
            print(result[0:-1])
    else:
        for new_results in new_list:
            print("@@@")
            for key in new_results.keys():
                print(key, "-", new_results[key])
