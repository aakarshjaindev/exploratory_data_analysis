class ModelTrainer:
    def __init__(self, model, train_data, train_labels):
        self.model = model
        self.train_data = train_data
        self.train_labels = train_labels

    def train_model(self):
        self.model.fit(self.train_data, self.train_labels)

    def save_model(self, file_path):
        import joblib
        joblib.dump(self.model, file_path)