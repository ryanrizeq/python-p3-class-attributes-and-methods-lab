class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count ={}

    @classmethod
    def add_song_to_count(cls):
        Song.count += 1

    @classmethod
    def add_to_genres(cls, obj):
        if obj.genre not in Song.genres:
            Song.genres.append(obj.genre)
        if obj.genre not in Song.genre_count:
            Song.genre_count[obj.genre] = 1
        else:
            Song.genre_count[obj.genre] += 1

    @classmethod
    def add_to_artists(cls, obj):
        if obj.artist not in Song.artists:
            Song.artists.append(obj.artist)
        if obj.artist not in Song.artist_count:
            Song.artist_count[obj.artist] = 1
        else:
            Song.artist_count[obj.artist] += 1

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)

    
