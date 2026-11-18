from pathlib import Path

def find_connection_error(log_path: Path) -> tuple[str, int] | None:
    with log_path.open(encoding="utf-8") as log:
        for line_num, line in enumerate(log, start=1):
            if "ECONNREFUSED" in line:
                return log_path.name, line_num
    return None
