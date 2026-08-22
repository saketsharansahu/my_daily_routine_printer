#student app maneger

CAMERA = 1 #0001
MICROPHONE = 2 #0010
STORAGE = 4 #0100
LOCATION = 8 #1000

#list of apps avalible to student
aproved_apps = [
    "coding app",
    "math app",
    "science app",
    "reading app",
]  

student_name = input("enter your name").lower()
requested_apps = input("enter your app that you want to access").lower()

print(" indentity operator check ")

if type(student_name) is str:
    print("your name is stored as text")
if type(requested_apps) is not int:
    print("the requested is not stored as number")

print(" membership operator check ")

if requested_apps in aproved_apps:
    print(requested_apps, " is a aproved app")
else:
    print(requested_apps, " is not a aproved app")

#use not in to check not aproved apps
not_approved_apps = [
    "gaming app",
    "shopping app",
    "social media app"
]

if requested_apps not in not_approved_apps:
    print("your app is not in restricted list")
else:
    print("access denied because the app is restricted")

print(" app permision settings ")

student_permission = CAMERA | MICROPHONE | STORAGE

print("permission value", student_name)

if student_permission and CAMERA:
    print("camera permission : enable")
if student_permission and MICROPHONE:
    print("microphone permission : enable")
if student_permission and STORAGE:
    print("storage permission : enable")
if student_permission and LOCATION:
    print("location permission : enable")
else:
  print("location permission : disable ")


print(" Bit Shift Demonstration ")
 
next_permission = CAMERA << 1
 
print("Camera bit:", bin(CAMERA))
print("After left shift:", bin(next_permission))

previous_permission = STORAGE >> 1
 
print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(previous_permission))
 
print(" Final Access Result ")

if requested_apps in aproved_apps and requested_apps not in not_approved_apps:
    print("Access granted to"), requested_apps
else:
    print("Access denied to", requested_apps)


