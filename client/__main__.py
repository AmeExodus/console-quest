"""Консольная точка входа первого этапа."""

from client.domain import GameState, choose, get_scene


def main() -> None:
    name = input("Имя героя: ").strip() or "Игрок"
    state = GameState.new(name)
    while True:
        scene = get_scene(state.current_scene_id)
        print(scene["description"])
        if scene["kind"] == "ending":
            print(f"Финал: {scene['ending']}")
            return
        for index, item in enumerate(scene["choices"], start=1):
            print(f"{index}. {item['text']}")
        try:
            state = choose(state, int(input("Ваш выбор: ")))
        except (ValueError, TypeError) as error:
            print(f"Ошибка ввода: {error}")


if __name__ == "__main__":
    main()