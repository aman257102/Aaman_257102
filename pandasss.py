# import pandas as pd

# data = [10, 20, 30, 40]
# s = pd.Series(data)

# print(s)

# import pandas as pd

# # Dictionary with comma between key-value pairs
# data = {
#     'Name': ['Ritik', 'Aman', 'Priya', 'Neha'],
#     'Age': [21, 23, 20, 22],
#     'Marks': [85, 90, 78, 88]
# }

# # Create DataFrame
# df = pd.DataFrame(data)
# print(df)

# # Print pandas version
# print(pd.__version__)

# # Create Series
# data = [10, 20, 30, 40]
# s = pd.Series(data)



# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)

# import pandas as pd

# import pandas as pd
# df = pd.read_csv("crocodile_dataset.csv")
# print(df.describe())

# import pandas as pd
# # Create Series from dictionary
# marks = {"math": 90, "science": 85, "English": 78}
# s = pd.Series(marks)
# print("Series:\n", s)
# print("\nMarks for science:", s["science"])
# print("\nData type:", s.dtype)
# print("Shape:", s.shape)


# import pandas as pd
# s = pd.Series([5, 10, 15, 20, 25])
# s_plus_5 = s + 5
# s_final = s_plus_5 * 2
# print("First 3 elements:\n", s_final[:3])


# 🦁 Shahi Python Code to Display a Lion Image

import matplotlib.pyplot as plt        # For displaying the image
from PIL import Image                  # For image processing
import requests                        # For downloading the image
from io import BytesIO                 # For handling byte stream of image

# 📷 Lion image URL
lion_url = "https://copilot.microsoft.com/th/id/BCO.8a914c1c-c779-4be9-b8c9-115ca951d114.png"

try:
    # 🔽 Download the image
    response = requests.get(lion_url)
    response.raise_for_status()  # Raise error if download fails

    # 🖼️ Open the image using Pillow
    lion_img = Image.open(BytesIO(response.content))

    # 🎨 Display the image using matplotlib
    plt.figure(figsize=(8, 6))
    plt.imshow(lion_img)
    plt.axis('off')  # Hide axes for clean look
    plt.title("🦁 Majestic Lion", fontsize=16, fontweight='bold')
    plt.show()

except requests.exceptions.RequestException as e:
    print("Image download failed:", e)
except Exception as e:
    print("Error displaying image:", e)