def warn_the_sheep(queue):
    queue.reverse()
    wolf_index = queue.index('wolf')
    if wolf_index == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!"