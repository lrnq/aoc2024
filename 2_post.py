from aocd import get_data

lines = [list(map(int, line.split())) for line in get_data().splitlines()]

for part in [1, 2]:
    ans = sum(
        any(
            all(
                (a > b if mod_line[0] > mod_line[1] else a < b) and abs(a - b) <= 3
                for a, b in zip(mod_line, mod_line[1:])
            )
            for mod_line in (
                [line] if part == 1 else [line[:i] + line[i+1:] for i in range(len(line))]
            )
        )
        for line in lines
    )
    print(f"Part {part}:", ans)
