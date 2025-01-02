import subprocess


def query(category: str | list[str], parameters: str | list[str]) -> list[dict[str, str]]:
    category = category if isinstance(category, list) else [category]
    parameters = parameters if isinstance(parameters, list) else [parameters]
    process = subprocess.run(
        ["wmic"] + category + ["get", ",".join(parameters)],
        capture_output=True
    )
    content = process.stdout.decode("utf-8")

    def without_empty_strings(l: list[str]) -> list[str]:
        return list(filter(lambda h: h is not None and len(h) > 0, l))

    lines = without_empty_strings(content.splitlines())
    header, data_rows = lines[0].lower(), lines[1:]
    columns = without_empty_strings(header.split(" "))

    params_formatted = sorted(map(lambda p: p.lower(), parameters))
    if params_formatted != columns:
        raise ValueError("invalid query")

    offsets = list(map(lambda c: header.index(c), columns))

    def parse_row(row_raw: str) -> dict:
        values = [row_raw[i:j].strip() for i, j in zip(offsets, offsets[1:] + [len(row_raw)])]
        return dict(zip(columns, values))

    return list(map(lambda r: parse_row(r), data_rows))
