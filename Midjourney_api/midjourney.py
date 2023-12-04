import subprocess

#For more details follow this github link: https://github.com/George-iam/Midjourney_api

def generate_image(prompt):
    command = f'python Midjourney_api\\sender.py --params Midjourney_api\\sender_params.json --prompt "{prompt}"'
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
