# 🧠 Monocular 3D Scene Reconstruction from Video

> Transform any single-camera video into a **VR-ready 3D scene** using MiDaS, COLMAP, and Open3D.

---

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

## ▶️ How to Run

1. **Extract Frames**
```bash
python 
```
2. **Run Depth Estimation (MiDaS)**
```bash
python 
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
5.**(Optional) Convert .ply to .glb**
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

##🙌 Author
Made with 💻 + 🧠 by Ved Khajone
> _Turning ordinary videos into immersive 3D scenes_

## 📜 License
MIT License. Free for personal & academic use. Attribution appreciated!
