import winsound

# Поочерёдное воспроизведение звука остановки и вопроса в Windows

winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

winsound.PlaySound("SystemHand", winsound.SND_ALIAS)