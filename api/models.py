from django.db import models

class PlayerScore(models.Model):
    username = models.CharField(max_length=100, unique=True) # Nome do jogador no Roblox
    score = models.IntegerField(default=0)                   # Pontuação total
    level = models.IntegerField(default=1)                   # Nível atual
    last_updated = models.DateTimeField(auto_now=True)       # Data da última jogada

    def __str__(self):
        return f"{self.username} - Level: {self.level} - Score: {self.score}"