def classify(mark):
    if mark >= 70:
        return "First"
    elif mark >= 60:
        return "Upper Second (2:1)"
    elif mark >= 40:
        return "Third"
    else:
        return "Fail"
def weighted_average(marks_credits):
    fifteen_credits = []
    thirty_credits = []
    sixty_credits = []
    current_average = 0
    for module in marks_credits:
        if module[1] == 15:
            fifteen_credits.append(module[0])
        elif module[1] == 30:
            thirty_credits.append(module[0])
        elif module[1] == 60:
            sixty_credits.append(module[0])

    if len(fifteen_credits) > 0:
        current_average += 15/120 * sum(fifteen_credits)
    if len(thirty_credits) > 0:
        current_average += 30/120 * sum(thirty_credits)
    if len(sixty_credits) > 0:
        current_average += 60/120 * sum(sixty_credits)

    return current_average

def calculate_best_classification(year2, year3):
    year2_avg = weighted_average(year2)

    fifteen_modules = []
    project_mark = 0
    for module in year3:
        if module[1] == 60:
            project_mark = module[0]
        if module[1] == 15:
            fifteen_modules.append(module)

    results = []
    fifteen_modules = sorted(fifteen_modules, key=lambda x: x[0], reverse=True)
    for num_modules, proj_weight in [(4, 30), (3, 45), (2, 60)]:
        total_score = 0

        module_combo = fifteen_modules[:num_modules]
        total_credits = sum(credit for _, credit in module_combo) + proj_weight

        if total_credits == 90:
            for grade, _ in module_combo:
                total_score += ((15 / 90) * grade)

            total_score += (proj_weight/90) * project_mark
            year3_avg = total_score

            for ratio in [(0.1, 0.9), (0.2, 0.8)]:
                final = (ratio[0] * year2_avg + ratio[1] * year3_avg)
                result = {
                    'ratio': f"{int(ratio[0] * 100)}:{int(ratio[1] * 100)}",
                    'year2_avg': year2_avg,
                    'year3_avg': year3_avg,
                    'modules_used': module_combo,
                    'project_weight': proj_weight,
                    'final': final,
                    'classification': classify(final)
                }
                results.append(result)


    best = max(results, key=lambda x: x['final'])
    print("")
    print("-------------------------------------")
    print("★ BEST RESULT ★")
    print(f"Ratio Used        : {best['ratio']}")
    print(f"Year 2 Average    : {best['year2_avg']}")
    print(f"Year 3 Average    : {best['year3_avg']}")
    print(f"Project Weight    : {best['project_weight']}/90")
    print(f"Modules Used      : {[mark for mark, _ in best['modules_used']]}")
    print(f"Final Mark        : {best['final']}")
    print(f"Classification    : {best['classification']}")
    print("-------------------------------------")
    print(" ")

# Example usage:
# year2_marks = [(55, 15), (60, 15), (65, 15), (70, 15), (75, 15), (80, 15), (60, 30)]
# year3_marks = [(70, 15), (75, 15), (80, 15), (90, 15), (65, 60)]


year2_marks = [(92, 15), (74, 15), (81, 15), (74, 15), (87, 15), (86, 15), (83, 30)]
year3_marks = [(86, 15), (99, 15), (85, 15), (64, 15), (65, 60)]



calculate_best_classification(year2_marks, year3_marks)
