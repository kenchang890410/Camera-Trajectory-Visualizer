# Camera Trajectory Visualizer

這個專案包含兩個 Python 程式，它們的核心功能是從不同三維建模的相機位姿估測 (Camera Pose Estimation) 階段所輸出的檔案中讀取相機位姿。

接著在三維空間計算出每張影像相機中心的三維坐標，並將其連接繪製成三維空間中的移動軌跡線段。

可以視覺化展示 3D 高斯潑濺 (3D Gaussian Splatting) 三維建模所使用的 COLMAP 相機位姿估測的效能。

以及視覺化展示 Endo-Depth-and-Motion 三維建模的相機位姿估測效能。

## 核心工具與功能一覽

### 3DGS_path_tracking.py

使用 3DGS_path_tracking.py 查看相機移動軌跡之前需要把 COLMAP 算完的 sparse\0\images.bin 轉換成 images.txt，

執行指令為 
```
colmap model_converter --input_path ./sparse/0 --output_path ./output --output_type TXT
```
完成這個指令後就會把 images.bin 轉換成 images.txt

接著將 file_path 改成 images.txt 路徑執行 3DGS_path_tracking.py 程式計算相機中心串成軌跡，以 3D 圖顯示，結果如下圖。

![image](https://github.com/kenchang890410/Camera-Trajectory-Visualizer/blob/5170706487aea27ce3c7d2a9c89f08596e0583ab/3DGS_path_tracking_sample.jpg)

圖中使用顏色漸變來表示影像順序，紅色線段代表影像序列前段起始的相機位置，藍色線段代表影像序列後段結束的相機位置。

### endo_depth_path_tracking.py

使用方法為將 file_path 改成 Endo-Depth-and-Motion 輸出的 poses.log 路徑。

同樣以 3D 圖顯示，結果如下圖。

![image](https://github.com/kenchang890410/Camera-Trajectory-Visualizer/blob/5170706487aea27ce3c7d2a9c89f08596e0583ab/endo_depth_path_tracking_sample.jpg)

圖中使用顏色漸變來表示影像順序，紅色線段代表影像序列前段起始的相機位置，藍色線段代表影像序列後段結束的相機位置。

