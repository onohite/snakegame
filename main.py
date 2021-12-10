from food import Food
from game import Game
from snake import Snake


def start():
    game = Game()
    snake = Snake(game.green)
    food = Food(game.brown, game.screen_width, game.screen_height)
    game.init_and_check_for_errors()
    game.set_surface_and_title()

    while True:
        snake.change_to = game.event_loop(snake.change_to)

        snake.validate_direction_and_change()
        snake.change_head_position()
        game.score, food.food_pos,tick = snake.snake_body_mechanism(
            game.score, food.food_pos, game.screen_width, game.screen_height)
        snake.draw_snake(game.play_surface, game.white)

        food.draw_food(game.play_surface)

        snake.check_for_boundaries(
            game.game_over)
        game.show_score()
        game.refresh_screen(tick)


if __name__ == '__main__':
    start()


