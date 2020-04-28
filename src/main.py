if __name__ == "__main__":
    import colorama
    from Game import Game

    colorama.init()
    
    game = Game()
    game.start()
    game.run()