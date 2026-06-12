def theft_detection(
        engine_locked,
        speed):

    if engine_locked and speed > 5:
        return True

    return False