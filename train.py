
# Load a model

if __name__ == '__main__':   #model = YOLO("yolo11n-cls.yaml").load(r"C:\Users\Jack\Desktop\blackjack\yolov8m_synthetic.pt")  # build a new model from YAML\\\
    from ultralytics import YOLO

    model = YOLO(r"C:\Users\Jack\Desktop\blackjack\yolov8m_synthetic.pt")  # load a pretrained model (recommended for training)
    #model = YOLO(r"C:\Users\Jack\Desktop\blackjack\runs\detect\train25\weights\best.pt")
#model = YOLO("yolo11n-cls.yaml").load("yolo11n-cls.pt")  # build from YAML and transfer weights
    path=r"C:\Users\Jack\Desktop\blackjack\poker cards.v2-release.yolov11\data.yaml"
# Train the model 
    save_dir=r"C:\Users\Jack\Desktop\blackjack"
    model.to('cuda')
    results = model.train(data=path, epochs=100, imgsz=640,workers=0,save=True,save_dir=save_dir)

    #model = YOLO("yolo11n-cls.pt")  # load an official model
    #model = YOLO("best.pt")  # load a custom model

    # Validate the model

    metrics = model.val()  # no arguments needed, dataset and settings remembered
    #x-entropy=results[0].boxes.xyxy)
    #print(results.save_dir(r'\runs\detect\train'))
    #metrics.top1  # top1 accuracy
    #metrics.top5  # top5 accuracy
