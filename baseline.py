from pathlib import Path

SOURCE_PATH = {"job.log": Path("fixtures/port-mismatch/job.log"), "pr.diff": Path("fixtures/port-mismatch/pr.diff"), "compose.yml": Path("fixtures/port-mismatch/compose.yml")}

def find_connection_error(log_path: Path) -> tuple[str, int] | None:
    with log_path.open(encoding="utf-8") as log:
        for line_num, line in enumerate(log, start=1):
            if "ECONNREFUSED" in line:
                return log_path.name, line_num
    return None


def read_excerpts(source_id: Path, start_line, end_line) -> tuple[str, int] | None:
    results = list()
    if (start_line > end_line or start_line < 1):
        raise ValueError("Invalid start line value")
    with source_id.open(encoding="utf-8") as source:
        for line_num, line in enumerate(source, start=1):
            if line_num >= start_line and line_num <= end_line:
                results.append([line_num, line])
                if (line_num == end_line):
                    return results
    raise ValueError("Invalid end line value")


def can_cite(
    read_lines: dict[str, set[int]], source_id: str, start_line: int, end_line: int
) -> bool:
    """Check whether one investigator read every line in a citation."""
    if start_line < 1 or end_line < start_line:
        return False

    source_lines = read_lines.get(source_id)
    if source_lines is None:
        return False

    return all(line_number in source_lines for line_number in range(start_line, end_line + 1))
