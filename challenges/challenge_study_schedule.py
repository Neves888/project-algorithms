def study_schedule(permanence_period, target_time):
    result = 0
    try:
        for student_time in permanence_period:
            if student_time[0] <= target_time <= student_time[1]:
                result += 1
        return result
    except TypeError:
        return None
