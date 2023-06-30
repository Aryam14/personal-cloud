from app import app
@app.route('/product/category/addnew')
def new_cat():
    return "you can add new category"
