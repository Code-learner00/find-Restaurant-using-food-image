from flask import Flask, render_template, request, redirect, url_for
import os
import uuid

# Import your backend functions.
from app import search_restaurants_by_food_item
from search_by_image import get_food_from_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get the food item entered by the user.
    food_item = request.form.get('food_item')
    if food_item:
        restaurants = search_restaurants_by_food_item(food_item)
        return render_template('results.html', restaurants=restaurants, query=food_item)
    return redirect(url_for('index'))

@app.route('/search_image', methods=['POST'])
def search_image():
    # Process the image uploaded by the user.
    if 'food_image' not in request.files:
        return redirect(url_for('index'))
    file = request.files['food_image']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        # Save the file temporarily.
        filename = f"{uuid.uuid4()}_{file.filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Use the backend function to identify food from the image.
        food_item = get_food_from_image(filepath)
        restaurants = search_restaurants_by_food_item(food_item)
        
        # Remove the temporary file.
        os.remove(filepath)
        return render_template('results.html', restaurants=restaurants, query=food_item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
