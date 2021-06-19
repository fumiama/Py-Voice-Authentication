
   # Voice Biometrics Authentication<br>

Voice Biometrics Authentication using GMM and Face Recognition Using Facenet and Tensorflow
___

   ## How to Run :
   
 **Install dependencies by running**  ```pip3 install -r requirement.txt```
 
 ### Run in terminal in following way :
 
   **To add new user :**
   ```
     python3 add_user.py
   ```
   **To Recognize user :**
   ```
     python3 recognize.py
   ```
   **To delete an existing user :**
   ```
     python3 delete_user.py
   ```
___
## Voice Authentication

   *For Voice recognition, **GMM (Gaussian Mixture Model)** is used to train on extracted MFCC features from audio wav           file.*<br><br>

**References :**
*Code for Facenet model is based on the assignment from Convolutional Neural Networks Specialization by Deeplearning.ai on Coursera*.<br>
https://www.coursera.org/learn/convolutional-neural-networks/home/welcome 
*Florian Schroff, Dmitry Kalenichenko, James Philbin (2015). [FaceNet: A Unified Embedding for Face Recognition and Clustering](https://arxiv.org/pdf/1503.03832.pdf)*
*The pretrained model used is inspired by Victor Sy Wang's implementation and was loaded using his code: https://github.com/iwantooxxoox/Keras-OpenFace.*
*Inspiration from the official FaceNet github repository: https://github.com/davidsandberg/facenet*
