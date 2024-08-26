"""
This script controls a PTZ (Pan-Tilt-Zoom) camera to capture images at random positions. It supports two camera brands: Axis and Hanwha. The script sets random positions for the camera, captures images, archives them into a tar file, and uploads the tar file using a plugin. The number of iterations and movements can be specified as command-line arguments.

The main functions in this script are:
- set_random_position: Sets a random position for the camera based on the specified camera brand.
- grab_image: Grabs an image from the camera.
- tar_images: Archives a folder into a tar file.
- publish_images: Publishes images by creating a tar file, deleting the individual image files, renaming the tar file with a timestamp, and uploading the renamed tar file using a plugin.
- main: The main function that controls the PTZ sampler.

Note: This code assumes the existence of the control module for each camera.

Usage:
python main.py [-cb CAMERA_BRAND] [-it ITERATIONS] [-mv MOVEMENTS] [-un USERNAME] [-pw PASSWORD] [-ip CAMERA_IP]

Arguments:
- cb, --camerabrand: An integer for each accepted camera brand (default=0). 0 is Hanwha, 1 is Axis.
- it, --iterations: An integer with the number of iterations (PTZ rounds) to be run (default=10).
- mv, --movements: An integer with the number of movements in each PTZ round to be run (default=10).
- un, --username: The username of the PTZ camera.
- pw, --password: The password of the PTZ camera.
- ip, --cameraip: The IP address of the PTZ camera.
"""

import time
import datetime
import os
import glob
import os.path
import traceback
import subprocess

import argparse

import numpy as np

from waggle.plugin import Plugin


def set_random_position(camera, camerabrand: int):
    """
    Sets a random position for the camera based on the specified camera brand.

    Args:
        camera: The camera object used for controlling the camera position.
        camerabrand (int): The brand of the camera (0 for axis, 1 for hanwha). 
        Camerabrand is hanwha

    Returns:
        None
    """
    if camerabrand == 0:
        pan_pos = np.random.randint(0, 360)
        tilt_pos = np.random.randint(-20, 90)
        zoom_pos = np.random.randint(1, 2)
    elif camerabrand == 1:
        pan_pos = np.random.randint(-180, 180)
        tilt_pos = np.random.randint(-180, 180)
        zoom_pos = np.random.randint(100, 200)
    try:
        if camerabrand == 0:
            camera.absolute_control(float(pan_pos), float(tilt_pos), float(zoom_pos))
        elif camerabrand == 1:
            camera.absolute_move(float(pan_pos), float(tilt_pos), int(zoom_pos))
    except:
        with Plugin() as plugin:
            plugin.publish('cannot.set.camera.random.position', str(datetime.datetime.now()))

    time.sleep(1)

def set_pos_1(camera, camerabrand: int):
    """
    Sets a random position for the camera based on the specified camera brand.

    Args:
        camera: The camera object used for controlling the camera position.
        camerabrand (int): The brand of the camera (0 for axis, 1 for hanwha). 
        Camerabrand is hanwha

    Returns:
        None
    """
    if camerabrand == 0:
        pan_pos = -180
        tilt_pos = 0
        zoom_pos = 1
    elif camerabrand == 1:
        pan_pos = -180
        tilt_pos = -15
        zoom_pos = 100
    try:
        if camerabrand == 0:
            camera.absolute_control(float(pan_pos), float(tilt_pos), float(zoom_pos))
        elif camerabrand == 1:
            camera.absolute_move(float(pan_pos), float(tilt_pos), int(zoom_pos))
    except:
        with Plugin() as plugin:
            plugin.publish('cannot.set.camera.random.position', str(datetime.datetime.now()))

    time.sleep(1)

def set_pos_2(camera, camerabrand: int):
    """
    Sets a random position for the camera based on the specified camera brand.

    Args:
        camera: The camera object used for controlling the camera position.
        camerabrand (int): The brand of the camera (0 for axis, 1 for hanwha). 
        Camerabrand is hanwha

    Returns:
        None
    """
    if camerabrand == 0:
        pan_pos = -180
        tilt_pos = -90
        zoom_pos = 1
    elif camerabrand == 1:
        pan_pos = -90
        tilt_pos = -15
        zoom_pos = 100
    try:
        if camerabrand == 0:
            camera.absolute_control(float(pan_pos), float(tilt_pos), float(zoom_pos))
        elif camerabrand == 1:
            camera.absolute_move(float(pan_pos), float(tilt_pos), int(zoom_pos))
    except:
        with Plugin() as plugin:
            plugin.publish('cannot.set.camera.random.position', str(datetime.datetime.now()))

    time.sleep(1)

def set_pos_3(camera, camerabrand: int):
    """
    Sets a random position for the camera based on the specified camera brand.

    Args:
        camera: The camera object used for controlling the camera position.
        camerabrand (int): The brand of the camera (0 for axis, 1 for hanwha). 
        Camerabrand is hanwha

    Returns:
        None
    """
    if camerabrand == 0:
        pan_pos = 0
        tilt_pos = 0
        zoom_pos = 1
    elif camerabrand == 1:
        pan_pos = 0
        tilt_pos = -15
        zoom_pos = 100
    try:
        if camerabrand == 0:
            camera.absolute_control(float(pan_pos), float(tilt_pos), float(zoom_pos))
        elif camerabrand == 1:
            camera.absolute_move(float(pan_pos), float(tilt_pos), int(zoom_pos))
    except:
        with Plugin() as plugin:
            plugin.publish('cannot.set.camera.random.position', str(datetime.datetime.now()))

    time.sleep(1)

def set_pos_4(camera, camerabrand: int):
    """
    Sets a random position for the camera based on the specified camera brand.

    Args:
        camera: The camera object used for controlling the camera position.
        camerabrand (int): The brand of the camera (0 for axis, 1 for hanwha). 
        Camerabrand is hanwha

    Returns:
        None
    """

    if camerabrand == 0:
        pan_pos = 90
        tilt_pos = 0
        zoom_pos = 1
    elif camerabrand == 1:
        pan_pos = 90
        tilt_pos = -15
        zoom_pos = 100
    try:
        if camerabrand == 0:
            camera.absolute_control(float(pan_pos), float(tilt_pos), float(zoom_pos))
        elif camerabrand == 1:
            camera.absolute_move(float(pan_pos), float(tilt_pos), int(zoom_pos))
    except:
        with Plugin() as plugin:
            plugin.publish('cannot.set.camera.random.position', str(datetime.datetime.now()))

    time.sleep(1)

def grab_image(camera, camerabrand: int):
    """
    Grabs an image from the camera.

    Args:
        camera: The camera object.
        camerabrand (int): The brand of the camera (0 for axis, 1 for hanwha).

    Raises:
        ValueError: If the camerabrand is not 0 or 1.

    Returns:
        None
    """
    if camerabrand == 0:
        position = camera.requesting_cameras_position_information()
    elif camerabrand == 1:
        position = camera.get_ptz()

    pos_str = str(position[0]) + ',' + str(position[1]) + ',' + str(position[2]) + ' '
    # ct stores current time
    ct = str(datetime.datetime.now())
    try:
        camera.snap_shot('./imgs/' + pos_str + ct + '.jpg')
    except:
        with Plugin() as plugin:
            plugin.publish('cannot.capture.image.from.camera', str(datetime.datetime.now()))


def tar_images(output_filename, folder_to_archive):
    """
    Archives the specified folder into a tar file.

    Args:
        output_filename (str): The name of the output tar file.
        folder_to_archive (str): The path to the folder to be archived.

    Raises:
        Exception: If an error occurs during the archiving process.

    Returns:
        None
    """
    try:
        cmd = ['tar', 'cvf', output_filename, folder_to_archive]
        output = subprocess.check_output(cmd).decode("utf-8").strip()
        print(output)
    except Exception:
        print(f"E: {traceback.format_exc()}")


def publish_images():
    """
    Publishes images by creating a tar file, deleting the individual image files, renaming the tar file with a timestamp,
    and uploading the renamed tar file using a plugin.
    """
    tar_images('images.tar', './imgs')
    files = glob.glob('./imgs/*.jpg', recursive=True)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    with Plugin() as plugin:
        ct = str(datetime.datetime.now())
        os.rename('images.tar', ct + '_images.tar')
        plugin.upload_file(ct + '_images.tar')


def main():
    """
    The main function that controls the PTZ sampler.

    Returns:
        None
    """
    parser = argparse.ArgumentParser("PTZ sampler")
    parser.add_argument("-cb", "--camerabrand",
                        help="An integer for each accepted camera brand (default=0). 0 is Hanwha, 1 is Axis.", type=int,
                        default=0)
    parser.add_argument("-it", "--iterations",
                        help="An integer with the number of iterations (PTZ rounds) to be run (default=10).", type=int,
                        default=1)
    parser.add_argument("-mv", "--movements",
                        help="An integer with the number of movements in each PTZ round to be run (default=10).",
                        type=int, default=1)
    parser.add_argument("-un", "--username",
                        help="The username of the PTZ camera.",
                        type=str, default='')
    parser.add_argument("-pw", "--password",
                        help="The password of the PTZ camera.",
                        type=str, default='')
    parser.add_argument("-ip", "--cameraip",
                        help="The ip of the PTZ camera.",
                        type=str, default='')
    args = parser.parse_args()

    if args.camerabrand==0:
        print('Importing Hanwha')
        from source import sunapi_control as sunapi_control
    elif args.camerabrand==1:
        print('Importing Axis')
        from source import vapix_control as sunapi_control
        #from source import onvif_control as sunapi_control
    else:
        print('Not known camera brand number: ', args.camerabrand)

    iterations = args.iterations
    number_of_commands = args.movements

    try:
        Camera1 = sunapi_control.CameraControl(args.cameraip, args.username, args.password)
    except:
        with Plugin() as plugin:
            plugin.publish('cannot.get.camera.from.ip', args.cameraip, timestamp=datetime.datetime.now())
            plugin.publish('cannot.get.camera.from.un', args.username, timestamp=datetime.datetime.now())
            plugin.publish('cannot.get.camera.from.pw', args.password, timestamp=datetime.datetime.now())

    if args.camerabrand==0:
        Camera1.absolute_control(1, 1, 1)
        time.sleep(1)
    elif args.camerabrand==1:
        Camera1.absolute_move(1, 1, 1)
        time.sleep(1)


    with Plugin() as plugin:
        plugin.publish('starting.new.image.collection.the.number.of.iterations.is', iterations)
        plugin.publish('the.number.of.images.recorded.by.iteration.is', number_of_commands)



    os.mkdir('./imgs')

    set_pos_1(camera=Camera1, camerabrand=args.camerabrand)
    grab_image(camera=Camera1, camerabrand=args.camerabrand)

    set_pos_2(camera=Camera1, camerabrand=args.camerabrand)
    grab_image(camera=Camera1, camerabrand=args.camerabrand)
    
    set_pos_3(camera=Camera1, camerabrand=args.camerabrand)
    grab_image(camera=Camera1, camerabrand=args.camerabrand)

    set_pos_4(camera=Camera1, camerabrand=args.camerabrand)
    grab_image(camera=Camera1, camerabrand=args.camerabrand)

    publish_images()
    os.rmdir('./imgs')

    if args.camerabrand==0:
        Camera1.absolute_control(1, 1, 1)
        time.sleep(1)
    elif args.camerabrand==1:
        Camera1.absolute_move(1, 1, 1)
        time.sleep(1)
    print('DONE!')

    with Plugin() as plugin:
        plugin.publish('finishing.image.collection', str(datetime.datetime.now()))

if __name__ == "__main__":
    main()
