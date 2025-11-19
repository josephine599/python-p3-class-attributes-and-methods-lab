class Song:
    all = []
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Add instance to class list
        Song.all.append(self)

        # Increment total count
        Song.count += 1

        # Track genres
        if genre not in Song.genres:
            Song.genres.append(genre)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        # Track artists
        if artist not in Song.artists:
            Song.artists.append(artist)
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
