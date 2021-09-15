from __future__ import annotations
import datetime
import random
import typer
import tqdm


app = typer.Typer()


MAX_BITHDAY_AMOUNT = 100
START_DATE = datetime.date(2021, 1, 1)


def to_percent(x: float) -> str:
    return "{0:.0%}".format(x)


def get_birthdays(amount: int) -> list[datetime.datetime]:
    return [START_DATE + datetime.timedelta(days=random.randint(0, 365)) for _ in range(amount)]


def get_matching_birthdays(birthdays: list[datetime.datetime]) -> list[datetime.datetime]:
    if len(birthdays) == len(set(birthdays)):
        return []

    matching_birthdays = []

    for i, birthday1 in enumerate(birthdays):
        for j, birthday2 in enumerate(birthdays):
            if i == j or (birthday1 in matching_birthdays or birthday2 in matching_birthdays):
                continue
            if birthday1 == birthday2:
                matching_birthdays.append(birthday1)

    return matching_birthdays

@app.command()
def main(birthday_amount: int=23, simulation_amount: int=100000) -> None:
    if birthday_amount > MAX_BITHDAY_AMOUNT:
        raise ValueError(f"Birthday amount [{birthday_amount}] can't be grater than {MAX_BITHDAY_AMOUNT}")
    if birthday_amount < 1:
        raise ValueError("Birthday amount shall be grater than 0")
    if simulation_amount < 1:
        raise ValueError("Simulation amount shall be grater than 0")

    sim_res = []

    print(f"Starting simulation process. Amount:{simulation_amount}; Birthday Gen:{birthday_amount}")


    for i in tqdm.tqdm(range(simulation_amount), ncols=100):
        birthdays = get_birthdays(birthday_amount)
        matching_birthdays = get_matching_birthdays(birthdays)
        matching_count = len(matching_birthdays)
        # print(f"Simulation [{i}] - matches:{matching_count}")
        sim_res.append(matching_count)

    print(f"Max:{max(sim_res)}")
    # print(f"Min:{min(sim_res)}")  # Lol
    average = sum(sim_res) / len(sim_res)
    print(f"Average:{average}")
    print(f"Chance: {to_percent(average)}")


if __name__ == '__main__':
    app()
