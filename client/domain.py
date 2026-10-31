"""Предметное состояние и переходы первого этапа."""

from __future__ import annotations

from dataclasses import dataclass, replace

SCENES = {
    "START": {
        "id": "START",
        "kind": "choice",
        "description": "Перед вами две двери.",
        "choices": (
            {"text": "Открыть светлую дверь", "next_scene_id": "WIN"},
            {"text": "Открыть тёмную дверь", "next_scene_id": "LOSS"},
        ),
    },
    "WIN": {
        "id": "WIN",
        "kind": "ending",
        "description": "Вы нашли выход.",
        "ending": "positive",
    },
    "LOSS": {
        "id": "LOSS",
        "kind": "ending",
        "description": "Путь завершился неудачей.",
        "ending": "negative",
    },
}

@dataclass(frozen=True)
class GameState:
    current_scene_id: str
    name: str
    hp: int
    strength: int
    defense: int

    @classmethod
    def new(cls, name: str) -> GameState:
        return cls("START", name, 10, 3, 2)


def get_scene(scene_id: str) -> dict[str, object]:
    try:
        return SCENES[scene_id]
    except KeyError as error:
        raise ValueError(f"Неизвестная сцена: {scene_id}") from error

def choose(state: GameState, number: object) -> GameState:
    if not isinstance(number, int):
        raise ValueError("Номер выбора должен быть целым числом")
    scene = get_scene(state.current_scene_id)
    choices = scene.get("choices", ())
    if not 1 <= number <= len(choices):
        raise ValueError(f"Номер выбора должен быть от 1 до {len(choices)}")
    target = choices[number - 1]["next_scene_id"]
    return replace(state, current_scene_id=target)