import os

tasks = []
done = []

clear_str = "cls" if os.name == "nt" else "clear"

while True:
    os.system(clear_str)

    tasks = sorted(tasks)
    done = sorted(done)

    print(f"tasks: \n")
    for task in tasks:
        print(f"[ ] {task}")
    for task in done:
        print(f"[X] {task}")

    u_input = input("\nEnter your task: ").strip()

    if u_input in tasks:
        done.append(u_input)
        tasks.remove(u_input)
        continue

    if u_input in done:
        done.remove(u_input)
        continue

    tasks.append(u_input)
