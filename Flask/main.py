from flask import Flask, request, render_template
from models.models import Company
from create_db import db

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/main', methods=['GET'])
def main_page():
    """Get-запрос главной страницы"""
    title = 'ООО "ПО "Высота"'
    heading = 'Главная страница'
    return render_template('main.html', title=title, heading=heading)


@app.route('/main/catalog', methods=['GET'])
def catalog_page():
    """Get-запрос страницы каталога"""
    title = 'ООО "ПО "Высота"'
    heading = 'Каталог'
    return render_template('catalog.html', title=title, heading=heading)


@app.route('/main/contacts', methods=['GET'])
def contacts_page():
    """Get-запрос страницы с контактной информацией"""
    title = 'ООО "ПО "Высота"'
    heading = 'Контакты'
    return render_template('contacts.html', title=title, heading=heading)


@app.route('/main/description', methods=['GET'])
def description_page():
    """Get-запрос страницы информации об организации"""
    title = 'ООО "ПО "Высота"'
    heading = 'О нас'
    return render_template('description.html', title=title, heading=heading)


@app.route('/main/catalog/company_form', methods=['GET', 'POST'])
def company_create_page():
    """Get/Post-запрос страницы с формой опросного листа"""
    if request.method == 'GET':
        title = 'ООО "ПО "Высота"'
        heading = 'Опросный лист'
        return render_template('company_form.html', title=title, heading=heading)
    elif request.method == 'POST':
        heading = 'Опросный лист'
        company = request.form.get('company')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        description = request.form.get('description')
        new_company = Company(
            company=company,
            name=name,
            email=email,
            phone=phone,
            address=address,
            description=description
        )
        db.session.add(new_company)
        db.session.commit()
        return render_template('success.html', heading=heading)
    return


if __name__ == '__main__':
    app.run(port=8000)
