from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, Request, HTTPException, status, Form
from backend.db import get_db
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from models.company import Company
from schemas import *

router = APIRouter(prefix="", tags=["main"])
templates = Jinja2Templates(directory='templates')


@router.get('/main')
async def main_page(request: Request):
    title = 'ООО "ПО "Высота"'
    heading = 'Главная страница'
    context = {
        'title': title,
        'heading': heading,
        'request': request
    }
    return templates.TemplateResponse(name='main.html', context=context)


@router.get('/main/catalog')
async def catalog_page(request: Request):
    title = 'ООО "ПО "Высота"'
    heading = 'Каталог'
    context = {
        'title': title,
        'heading': heading,
        'request': request
    }
    return templates.TemplateResponse(name='catalog.html', context=context)


@router.get('/main/contacts')
async def contacts_page(request: Request):
    title = 'ООО "ПО "Высота"'
    heading = 'Контакты'
    context = {
        'title': title,
        'heading': heading,
        'request': request
    }
    return templates.TemplateResponse(name='contacts.html', context=context)


@router.get('/main/description')
async def description_page(request: Request):
    title = 'ООО "ПО "Высота"'
    heading = 'О нас'
    context = {
        'title': title,
        'heading': heading,
        'request': request
    }
    return templates.TemplateResponse(name='description.html', context=context)


@router.get('/main/catalog/company_form')
async def company_create_page(request: Request):
    title = 'ООО "ПО "Высота"'
    heading = 'Опросный лист'
    context = {
        'title': title,
        'heading': heading,
        'request': request
    }
    return templates.TemplateResponse(name='company_form.html', context=context)


@router.post('/main/catalog/company_form', status_code=status.HTTP_201_CREATED)
async def company_create(request: Request,
                         db: Annotated[Session, Depends(get_db)],
                         company: str = Form(),
                         name: str = Form(),
                         email: str = Form(),
                         phone: str = Form(),
                         address: str = Form(),
                         description: str = Form()):
    db.execute(insert(Company).values(company=company,
                                      name=name,
                                      email=email,
                                      phone=phone,
                                      address=address,
                                      description=description))
    db.commit()
    return templates.TemplateResponse(name='success.html', context={"request": request, "company": company_create})


@router.put('/update')
async def company_update(db: Annotated[Session, Depends(get_db)], company_id: int, company_update: CompanyUpdate):
    company = db.scalar(select(Company).where(Company.id == company_id))
    if company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Company was not found'
        )
    db.execute(update(Company).where(Company.id == company_id).values(
        company=company_update.company,
        name=company_update.name,
        email=company_update.email,
        phone=company_update.phone,
        address=company_update.address,
        description=company_update.description))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Company update is successful!'
    }


@router.delete('/delete')
async def company_delete(db: Annotated[Session, Depends(get_db)], company_id: int):
    company = db.scalar(select(Company).where(Company.id == company_id))
    if company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Company was not found'
        )
    db.execute(delete(Company).where(Company.id == company_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Company delete is successful!'
    }
