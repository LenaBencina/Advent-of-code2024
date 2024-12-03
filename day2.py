with open('input_day2.txt') as f:
    reports = f.readlines()


def check_if_safe(report: list) -> bool:
    is_desc, is_asc = True, True

    i = 0
    while i < len(report):
        level = int(report[i])

        if i != 0:
            if level > level_prev and (level - level_prev) < 4 and is_asc:
                is_asc, is_desc = True, False
            elif level_prev > level and (level_prev - level) < 4 and is_desc:
                is_desc, is_asc = True, False
            else:
                return False

        level_prev = level
        i += 1

    return True


def check_if_safe_skip_one(report: list) -> bool:
    for skip_i in range(len(report)):
        is_safe = check_if_safe(report[:skip_i] + report[skip_i + 1:])
        if is_safe:
            return True
    return False


n_safe = 0
for report in reports:
    report = report.strip().split()
    is_safe = check_if_safe(report)
    # add this for part 2
    if not is_safe:
        is_safe = check_if_safe_skip_one(report)

    n_safe += is_safe

print(f"Number of safe reports: {n_safe}")
