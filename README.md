# Пример автоматизации тестирования с помощью Selenium и unittest

В данном проекте представлен пример написания автотестов для сайта Saucedemo.com с использованием паттерна POM <!-- описание репозитория -->

<!--Запуск тестов-->

## Установка зависимостей

```pip3 install -r requirements.txt```

## Запуск тестов

1. Запуск теста авторизации

```python -m unittest tests.test_login```

2. Запуск теста основного функционала

```python -m unittest tests.test_smoke```

3. Запуск всех тестов
   
```python -m unittest discover```
   


