import pypresence
import time

from subprocess import check_output
def get_pid(name):
    return check_output(["pidof",name])

dotapid = get_pid("dota2")

client_id = ""
RPC = pypresence.Client(client_id)
RPC.start()

print(RPC.set_activity(pid = int(dotapid),state = "Playing Dota 2",details = "Playing a game",large_image = "https://www.citypng.com/public/uploads/preview/hd-dota-2-official-logo-png-701751694788589vbfyq561nz.png",large_text = "Hello world"))


while True:
    if (int(dotapid) == None):
        RPC.close() 
    time.sleep(15)