# api_yamdb

������ YaMDb �������� ������ ������������� �� ��������� ������������.

## **��� ��������� ������:**

����������� ����������� � ������� � ���� � ��������� ������:

>*git clone https://github.com/airatns/api_final_yatube.git*

C������ � ������������ ����������� ���������:

>*python3 -m venv env*

>*source env/scripts/activate*

���������� ����������� �� ����� requirements.txt:

>*python3 -m pip install --upgrade pip*

>*pip install -r requirements.txt*

��������� ��������:

>*python3 manage.py migrate*

��������� ������:

>*python3 manage.py runserver*

## **����������� ������ ������������**
>*http://127.0.0.1:8000/api/v1/auth/signup/*

��� ����������� ������� **email** � **username**.

����� �� ��� ����������� ������� ���� ����� **confirmation_code**.

## **��������� JWT-������**
>*http://127.0.0.1:8000/api/v1/auth/token/*

��� �������������� ������� **username** � **confirmation_code**.

��� ����� ����� **token** ��� �������� � API.

���� �������� ������ **14 ����**.

### **������ ������������� JWY-������**

>*Bearer ey8Df...*


## **������� �������� � API**

### **��������� ������ ����� ������� ������**

>*http://127.0.0.1:8000/api/v1/users/me/*

*Request*

>*"first_name": "first",*

>*"last_name": "forever"*

>*"bio": "I was born on January 1st"*

*Response*

>*"username": "first#1",*

>*"email": "first#1@google.com",*

>*"first_name": "first",*

>*"last_name": "forever"*

>*"bio": "I was born on January 1st"*

>*"role": "user"*

### **�������� �����**

>*DELETE /api/v1/genres/{slug}/*

*Response*

>*HTTP Code: 204*

### **���������� ������������**

>*POST /api/v1/titles/*

*Request*
>{
>
>*"name": "Alien",*
> 
>*"year": 1979*
>
>*"description": "In space no one can hear your scream"*
>
>*"genre": "horror"*
>
>*"category": "films"*
>
>}


*Response*
>{
> 
>*"id": 13,*
>
>*"name": "Alien",*
>
>*"year": 1979*
>
>*"rating": "None"*
>
>*"description": "In space no one can hear your scream"*
>
>*"genre"*: 
> [{
> *"slug": "horror"*,
> *"name": "�����"*
> }]
>
>*"category"*: {
> *"slug"*: *"films"*,
> *"name"*: *"����"*
> }
>
> }