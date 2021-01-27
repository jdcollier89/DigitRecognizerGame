from src.settings import Settings
from src.model import Model

ai_settings = Settings()
new_model = Model(train_flag=1, settings=ai_settings)