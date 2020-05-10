#!/usr/bin/python


def perfometer_cobian_backup(row, check_command, perf_data):
    seconds_ago = float(perf_data[0][1])
    seconds_warn = float(perf_data[0][3])
    seconds_error = float(perf_data[0][4])

    left_until_overdue = seconds_error - seconds_ago
    percent = (seconds_ago/seconds_error)*100

    days,    rest    = divmod(left_until_overdue, 60*60*24)
    hours,   rest    = divmod(rest,   60*60)
    minutes, seconds = divmod(rest,      60)

    return "overdue in %02dd %02dh %02dm" % (days, hours, minutes), perfometer_linear(percent, '#00BB33')

perfometers["check_mk-cobian_backup"] = perfometer_cobian_backup
