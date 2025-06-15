# 🧠 Monocular 3D Scene Reconstruction from Video

> Transform any single-camera video into a **VR-ready 3D scene** using MiDaS, COLMAP, and Open3D.
---
 | ![2](imgs/room.gif)   | ![z](imgs/3d.gif) |
| ------------------------------ | ---------------------------- |

## 🚀 Project Overview

This project reconstructs a **3D model** from a monocular video by predicting depth, estimating camera pose, and fusing RGB-D data into a mesh. The result is exported as `.glb` format, viewable in WebXR, Unity, or other 3D engines.

---

## 🛠️ Tech Stack

- **Depth Estimation**: [MiDaS](https://github.com/isl-org/MiDaS)
- **Camera Pose Estimation**: [COLMAP](https://colmap.github.io/)
- **TSDF Fusion & Mesh Export**: [Open3D](http://www.open3d.org/)
- **3D Format**: `.ply` → `.glb` for VR/AR

---

## 📷 Pipeline Steps

| Step | Description |
|------|-------------|
| 🎥 1. Frame Extraction | Convert video to individual RGB frames |
| 🌊 2. Depth Estimation | Run MiDaS on frames to get `.npy` depth maps |
| 📸 3. COLMAP SfM       | Use COLMAP to estimate camera poses and point cloud |
| 🧱 4. TSDF Fusion      | Fuse RGB + depth using Open3D and camera poses |
| 🌐 5. Export Mesh      | Save final mesh as `.ply` or `.glb` for VR use |

---

## 📂 Folder Structure

- ├── input_frames/ # RGB images
- ├── depth_output/ # MiDaS .npy depth maps
- ├── colmap_output/ # COLMAP images.txt, cameras.txt
- ├── mesh_output/ # Final mesh (ply/glb)
---

## ▶️ How to Run (Update the file location in code based on your folder)

1. **Extract Frames**
```bash
python 
```
2. **Run Depth Estimation (MiDaS)**
### Setup 

1) Pick one or more models and download the corresponding weights to the `weights` folder:

MiDaS 3.1
- For highest quality: [dpt_beit_large_512](https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_beit_large_512.pt)
- For moderately less quality, but better speed-performance trade-off: [dpt_swin2_large_384](https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_swin2_large_384.pt)
- For embedded devices: [dpt_swin2_tiny_256](https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_swin2_tiny_256.pt), [dpt_levit_224](https://github.com/isl-org/MiDaS/releases/download/v3_1/dpt_levit_224.pt)
- For inference on Intel CPUs, OpenVINO may be used for the small legacy model: openvino_midas_v21_small [.xml](https://github.com/isl-org/MiDaS/releases/download/v3_1/openvino_midas_v21_small_256.xml), [.bin](https://github.com/isl-org/MiDaS/releases/download/v3_1/openvino_midas_v21_small_256.bin)

MiDaS 3.0: Legacy transformer models [dpt_large_384](https://github.com/isl-org/MiDaS/releases/download/v3/dpt_large_384.pt) and [dpt_hybrid_384](https://github.com/isl-org/MiDaS/releases/download/v3/dpt_hybrid_384.pt)

MiDaS 2.1: Legacy convolutional models [midas_v21_384](https://github.com/isl-org/MiDaS/releases/download/v2_1/midas_v21_384.pt) and [midas_v21_small_256](https://github.com/isl-org/MiDaS/releases/download/v2_1/midas_v21_small_256.pt) 

```bash
python depth_estimation.py
```
3.**COLMAP**
- Run COLMAP GUI
- Feature Matching
- SfM
- MVS
- Export images.txt, cameras.txt
  
4. **Integrate RGBD to Mesh**
```bash
python integrate_tsdf.py
```
5.**To view th ply generated run viewply.py**
```bash
python viewply.py
```
6.**(Optional) Convert .ply to .glb**
```bash
Use blender or unity to import .pyl file and export it to .glb
```
## ✅ Requirements
```bash
pip install requirements.txt
```
### Also install:
- COLMAP
- MiDaS requirements: torch, timm, cv2, etc.

## 🙌 Author
Made with 💻 + 🧠 by Ved Khajone
> _Turning ordinary videos into immersive 3D scenes_

## 📜 License
MIT License. Free for personal & academic use. Attribution appreciated!
