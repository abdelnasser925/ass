import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load ID image
img = cv2.imread(r'D:\Downloads\id.jpg', cv2.IMREAD_UNCHANGED)

# If image not found, create placeholder
if img is None:
    img = np.zeros((400, 300, 4), dtype=np.uint8)
    img[:,:,:3] = 50  # Dark gray background
    cv2.putText(img, "ID PLACEHOLDER", (30,200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255,255), 2)

# Convert to BGRA if not already
if img.shape[2] == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# Write name
name = "Abdelnasser Mohamed"
text_size = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
text_x = (img.shape[1] - text_size[0]) // 2  # Center horizontally
cv2.putText(img, name, (text_x, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255,255), 2)

# Draw line under name
line_y = 60
cv2.line(img, (text_x, line_y), (text_x + text_size[0], line_y), (255,255,255,255), 2)

# Draw circles on corners
h, w = img.shape[:2]
radius = min(h, w) // 20  # Dynamic radius based on image size
corners = [(radius, radius), (w-radius, radius), 
           (radius, h-radius), (w-radius, h-radius)]
for x, y in corners:
    cv2.circle(img, (x, y), radius, (0,255,0,255), -1)

# Create 4 transparency versions
alphas = [1.0, 0.75, 0.5, 0.25]
plt.figure(figsize=(12, 8))

for i, alpha in enumerate(alphas):
    plt.subplot(2, 2, i+1)
    
    # Create transparent version
    if alpha < 1.0:
        transparent_img = img.copy()
        transparent_img[:,:,3] = (transparent_img[:,:,3] * alpha).astype(np.uint8)
        plt.imshow(cv2.cvtColor(transparent_img, cv2.COLOR_BGRA2RGBA))
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA))
    
    plt.title(f'Transparency: {int(alpha*100)}%')
    plt.axis('off')

plt.tight_layout()
plt.show()

# Save final image
cv2.imwrite('id_card_with_features.png', img)