# -*- coding: utf-8 -*-

import subprocess

# 执行shell
def shell(cmd):
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    (stdout_output, err_output) = p.communicate()
    if err_output != None and len(err_output) != 0:
        print("Shell err_output: " + str(err_output))
    # print("stdout_output: " + str(stdout_output))
    return stdout_output

# 判断app应用是否在前台
def is_activity_started(package_name, device_id = ''):
    if device_id != '':
        cmd_current_activity = "adb -s %s shell dumpsys activity activities | sed -En -e '/Running activities/,/Run #0/p'" % device_id
    else:
        cmd_current_activity = "adb shell dumpsys activity activities | sed -En -e '/Running activities/,/Run #0/p'"
    cmd_result = str(shell(cmd_current_activity))
    # 如果当前应用处于前台或resume后台状态，返回True
    if package_name in cmd_result:
        return True
    else:
        return False