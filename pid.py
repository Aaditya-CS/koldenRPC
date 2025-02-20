from subprocess import check_output
def get_pid(name):
    return check_output(["pidof",name])

print(get_pid("dota2"))