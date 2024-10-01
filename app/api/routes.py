# /app/api/routes.py
print("Loading routes.py")

# from app.controllers.meal_controller import MealController  # Comment this out
# from app.controllers.profile_controller import ProfileController  # Comment this out

from app.controllers.user_controller import UserController  # Leave one controller uncommented
print("Successfully imported UserController in routes.py")
