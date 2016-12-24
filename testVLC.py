import vlc

instance = vlc.Instance('--fullscreen')
player = instance.media_player_new()
media = instance.media_new('test.mp4')
media.get_mrl()
player.set_media(media)
player.play()
