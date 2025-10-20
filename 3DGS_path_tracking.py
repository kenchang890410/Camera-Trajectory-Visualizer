import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
import matplotlib.cm as cm

def read_file(file_path):
    camera_positions = []
    camera_ids = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines:

            data = line.split()
            
            if len(data) < 10:
                continue

            camera_id = int(data[0])
            quaternion = [float(data[1]), float(data[2]), float(data[3]), float(data[4])]
            translation = [float(data[5]), float(data[6]), float(data[7])]
            rotation_matrix = R.from_quat([quaternion[1], quaternion[2], quaternion[3], quaternion[0]]).as_matrix()
    
            camera_center = -np.transpose(rotation_matrix).dot(translation)        
            camera_positions.append(camera_center)
            camera_ids.append(camera_id)
    
    sorted_indices = np.argsort(camera_ids)
    camera_positions = np.array(camera_positions)[sorted_indices]
    return camera_positions

def plot_camera_positions(camera_positions):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    num_points = len(camera_positions)
    colors = cm.coolwarm(np.linspace(1, 0, num_points))
    
    for i in range(1, num_points):
        ax.plot(camera_positions[i-1:i+1, 0], camera_positions[i-1:i+1, 1], camera_positions[i-1:i+1, 2], 
                color=colors[i], linewidth=2)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Camera Trajectory in 3D Space')

    for i in range(len(camera_positions) - 1):
        ax.quiver(camera_positions[i, 0], camera_positions[i, 1], camera_positions[i, 2],
                  camera_positions[i+1, 0] - camera_positions[i, 0], 
                  camera_positions[i+1, 1] - camera_positions[i, 1], 
                  camera_positions[i+1, 2] - camera_positions[i, 2],
                  color=colors[i], arrow_length_ratio=0.1)
    
    plt.show()

file_path = 'images.txt'
camera_positions = read_file(file_path)
plot_camera_positions(camera_positions)
