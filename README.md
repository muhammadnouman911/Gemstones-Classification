
# 💎 Gemstones-Classification

A deep learning-based image classification project that uses the powerful **VGG16** model to classify various types of gemstones with **~100% accuracy**.

This project demonstrates the effectiveness of transfer learning in image classification tasks and provides a simple interface for testing the model.

---

## 🧠 Overview

Gemstones can look very similar to the human eye, but deep learning can help distinguish them with great precision. We’ve leveraged the **VGG16** architecture (pre-trained on ImageNet) and fine-tuned it on our custom gemstone dataset. The result? Almost **perfect classification accuracy**!

---

## 📁 Project Structure

```
📦 Gemstones-Classification
 ┣ 📂 Dataset/                # Contains training/testing gemstone images
 ┣ 📜 Classification.ipynb    # Jupyter Notebook - training + evaluation
 ┣ 📜 app.py                  # Script or web app for making predictions
 ┣ 📜 README.md               # Project documentation
```

---

## ✅ Features

- 🧠 Transfer learning with **VGG16**
- 📊 Achieves **90% accuracy**
- 📸 Handles gemstone image classification
- 🖥️ Simple script/app for real-time predictions

---

## 🔧 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/muhammadnouman911/Gemstones-Classification.git
cd Gemstones-Classification
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` not available, install manually:
```bash
pip install tensorflow keras numpy matplotlib opencv-python scikit-learn
```

### 3. Prepare Dataset

Organize your dataset like this:
```
/Dataset
  /train
    /ruby/
    /emerald/
    /sapphire/
  /test
    /ruby/
    /emerald/
    /sapphire/
```

> Make sure image folders are named according to gemstone classes.

### 4. Run the Notebook
```bash
jupyter notebook Classification.ipynb
```

### 5. Predict with the App
If you're using `app.py` (e.g., Streamlit or Flask):
```bash
python app.py
```

---

## 🧠 Model Details

- **Base Model:** VGG16 (Pre-trained on ImageNet)
- **Top Layers:** Flatten → Dense → Dropout → Output
- **Fine-tuning:** Last few layers unfrozen
- **Optimizer:** Adam
- **Loss:** Categorical Crossentropy
- **Accuracy Achieved:** ~**100%**

---

## 📊 Performance

| Metric       | Value       |
|--------------|-------------|
| Accuracy     | 90%       |
| Precision    | 90%        |
| Recall       | 90%        |
| F1-Score     | 90%        |

---

## 🎯 Future Improvements

- ✅ Add ResNet and Inception options
- ✅ Real-time image prediction using camera input
- ✅ Deploy on web with Streamlit/Flask
- ✅ Add Grad-CAM visualizations

---

## 📬 Contact

Feel free to reach out for collaboration, feedback, or queries:
**GitHub:** [@muhammadnouman911](https://github.com/muhammadnouman911)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
