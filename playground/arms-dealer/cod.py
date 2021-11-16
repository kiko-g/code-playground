import sys
import subprocess

prefix = "https://my.callofduty.com/player/store/sku/"
suffix = "/title/mw"

def openPortionOfTabsAllAtOnce(portionSize=10, portionIndex=0, start=400000):
  index = 0
  origin = start + portionSize * portionIndex
  command = "powershell.exe Start-Process -FilePath Chrome -ArgumentList '--new-window "
  print("Launching tabs between " + str(origin) + " and " + str(origin+portionSize-1))
  while index < portionSize:
    url = prefix + str(origin + index) + suffix
    command += url + ' '
    index += 1
  command += '\''
  subprocess.call(command, shell=False)
  print("Launched browser tabs!")


def openPortionOfTabsOneAtATime(portionSize, portionIndex):
  index = 0
  origin = 400000 + portionSize * portionIndex
  print("Launching tabs between " + str(origin) + " and " + str(origin+portionSize-1))
  while index < portionSize:
    url = prefix + str(origin + index) + suffix
    command = "powershell.exe start chrome " + url
    subprocess.call(command, shell=False)
    index += 1
  print("Finished launching browser tabs!")


def seenOrUnseenTabs(seen, launch=False, origin=400000):
  file = open("hits.txt", "r")
  sfile = open("seen.txt", "w")
  sfile.write("# Seen or Unseen\n")
  file.readline()
  for i in range(origin, origin + 600):
    line = file.readline().split(" - ")
    url = prefix + line[0] + suffix
    sfile.write(line[0]) 
    if line[1] == "N/A\n":
      sfile.write(" NO\n")
      if not seen and launch:
        command = "powershell.exe start chrome " + url
        subprocess.call(command, shell=False)

    elif line[1] != "N/A\n":
      sfile.write(" YES\n")
      if seen and launch:
        command = "powershell.exe start chrome " + url
        subprocess.call(command, shell=False)


if __name__ == '__main__':
  seenOrUnseenTabs(seen=False, launch=True)
  # openPortionOfTabsAllAtOnce(portionSize=100, portionIndex=int(sys.argv[1]))
