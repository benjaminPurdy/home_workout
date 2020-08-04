import os
import time


exercises = [
    {
        'name': 'Jumping Jacks',
        'duration': 60
    },
    {
        'name': 'Steam Engines',
        'duration': 60
    },
    {
        'name': 'Squats',
        'duration': 60
    },
    {
        'name': 'Burpees',
        'duration': 60
    },
    {
        'name': 'Supermans',
        'duration': 30
    },
    {
        'name': 'Planks',
        'duration': 30
    },
    {
        'name': 'Rest Break',
        'duration': 30
    },
    {
        'name': 'Jump Ropes',
        'duration': 60
    },
    {
        'name': 'Arm Circles',
        'duration': 30
    },
    {
        'name': 'Ankle Taps',
        'duration': 60
    },
    {
        'name': 'Glute Bridges',
        'duration': 60
    },
    {
        'name': 'Push-ups',
        'duration': 30
    },
    {
        'name': 'Rest Break',
        'duration': 30
    },
    {
        'name': 'Jumping Jacks',
        'duration': 60
    },
    {
        'name': 'Toe Touches',
        'duration': 60
    },
    {
        'name': 'Jump Ropes',
        'duration': 60
    },
    {
        'name': 'Planks',
        'duration': 30
    },
    {
        'name': 'Rest Break',
        'duration': 30
    },
    {
        'name': 'Jumping Jacks',
        'duration': 60
    },
    {
        'name': 'Mountain Climbers',
        'duration': 30
    },
    {
        'name': 'Side Plank Left',
        'duration': 30
    },
    {
        'name': 'Side Plank Right',
        'duration': 30
    },
    {
        'name': 'Raise the roof',
        'duration': 30
    },
    {
        'name': 'Flutter Kicks',
        'duration': 30
    },
    {
        'name': 'Jump Ropes',
        'duration': 30
    },
    {
        'name': 'Jumping Jacks',
        'duration': 30
    },
    {
        'name': 'Squats',
        'duration': 30
    },
]

os.system("say 'Starting in 30 seconds'")
print('Starting in 30 seconds')
time.sleep(30)

for exercise in exercises:
    name = exercise.get('name')
    duration = exercise.get('duration')
    os.system(f"say '{name} for {duration} seconds'")
    print(f'{name} for {duration} seconds')
    time.sleep(duration)
    print('-------------------------------------------------')

os.system("say 'Congratulations on completing this workout!'")




