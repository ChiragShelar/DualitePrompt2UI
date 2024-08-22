import subprocess


def generate_image(prompt):
    command = f'python Midjourney_api\\sender.py --params Midjourney_api\\sender_params.json --prompt "{prompt}"'
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
