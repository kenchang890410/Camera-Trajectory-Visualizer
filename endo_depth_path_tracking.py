import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

np.set_printoptions(suppress=True, precision=10)

def read_trajectory(file_path):
    
    trajectory = []

    with open(file_path, "r") as f:
        lines = f.readlines()

    i = 0

    while i < len(lines):
        parts = lines[i].strip().split()
        if len(parts) == 3:

            frame_id = int(parts[2])

            i += 1
            matrix = []

            for _ in range(4):
                matrix.append([float(x) for x in lines[i].strip().split()])
                i += 1

            matrix = np.array(matrix)
            R = matrix[:3, :3]
            T = matrix[:3, 3]

            camera_center = -np.transpose(R).dot(T)
            camera_center = camera_center.astype(float)

            print(f"Frame {frame_id} Camera Center: {camera_center}")
            trajectory.append(camera_center)

        else:
            i += 1

    return np.array(trajectory)

file_path = "poses.log"
trajectory = read_trajectory(file_path)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

segments = [[trajectory[i], trajectory[i + 1]] for i in range(len(trajectory) - 1)]
lc = Line3DCollection(segments, cmap="coolwarm", linewidth=1)
lc.set_array(np.linspace(1, 0, len(segments)))
ax.add_collection(lc)

ax.scatter(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2],
           c=np.linspace(1, 0, len(trajectory)), cmap="coolwarm", marker="o", s=5)

ax.set_xlim(-0.04, 0.1)
ax.set_xticks(np.arange(-0.1, 0.2, 0.05))

ax.set_ylim(0, 0.01)
ax.set_yticks(np.arange(0, 0.1, 0.05))

ax.set_zlim(-0.01, 0.05)
ax.set_zticks(np.arange(-0.10, 0.15, 0.05))

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Camera Trajectory")

plt.colorbar(lc, ax=ax, label="Trajectory Progress")
plt.show()
