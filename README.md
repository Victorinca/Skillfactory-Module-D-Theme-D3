# Skillfactory Module D. Theme D3

Completed homework for Skillfactory Course: 'Python Web Developer'. Module D - 'Backend-development in Python and Django'. Theme D3 - 'Views and Templates in Django'.

## Репозиторий учебного проекта NewsPaper для курсов "Веб-разработчик на Python" и "Fullstack-разработчик на Python"
### [Модуль D. Тема D3 "Представления и шаблоны в Django"](https://victorinca.github.io/Skillfactory-Module-D-Theme-D3/)

Приложение новостного портала NewsPaper, созданное с помощью Python и Django, чтобы можно было: 1) смотреть новости 2) читать статьи.

Итоговое задание по теме D3 "Представления и шаблоны в Django" заключается в создании страниц со списком статей и с конкретными статьями.

База данных: sqlite.

Состоит из приложений news и accounts.

#### Приложение news включает в себя модели:
1) Author - авторы статей, новостей (далее - постов).
2) Category - категории постов - темы, которые они отражают (бизнес и экономика, наука и технологии, образование и вакансии, стиль жизни и здоровье и т.д.).
3) Post - посты (статьи и новости), которые создают пользователи. Каждый объект может иметь одну или несколько категорий.
4) PostCategory - промежуточная модель (явная) для связи "многие ко многим".
5) Comment - хранение комментариев к постам, оставляемых под каждой новостью/статьёй.

Все модели собраны в единый скрипт (код) в приложении news в файл models.py.

#### В качестве результата задания нужно доработать своё новостное приложение NewsPaper.

1) Сделать новую страничку с адресом /news/, на которой должен выводиться список всех новостей.

2) Сделать отдельную страницу для каждой конкретной статьи/ новости по адресу /news/<id новости>.

3) Все новые странички должны быть частью основного шаблона default.html.

4) Настроить внешний вид страниц. Все статьи/ новости должны быть выведены в следующем виде: заголовок, дата публикации в формате (день.месяц.год) и первые 50 символов текста статьи.

5) Сверху страницы должно быть выведено количество всех новостей (используется фильтр news|length).
6) Новости должны выводиться в порядке от более свежей до самой старой. Все посты отображаются по адресу /news/.

7) На странице статьи (по ссылке /news/<id новости>) должна выводиться вся информация о статье/ новости в следующем виде:
заголовок, дата создания в формате ДЕНЬ-МЕСЯЦ-ГОД ЧАС:МИНУТЫ и текст.

8) Создать/ Написать собственный фильтр Censor, который цензурирует нежелательную лексику в названиях и текстах статей, и применить его к названию и содержанию статей.

## Поддержать, отблагодарить автора
Если представленная работа Вам понравилась, принесла пользу, сэкономила время, то Вы можете поддержать автора, воспользовавшись различными платежными системами.
- [Поддержать автора через ЮMoney](https://yoomoney.ru/to/4100117804016773)
- [Выразить признательность через Qiwi](https://qiwi.com/n/VICTORINCA)
- [Поблагодарить автора через WebMoney](https://donate.webmoney.com/w/5hctnjhg47g6EvMB6vItYb)
#### Благодарю Вас за щедрость!
#### Ваша поддержка и признательность очень приятны и важны!

## Ссылки

- [Ссылка на сайт проекта](https://victorinca.github.io/Skillfactory-Module-D-Theme-D3/)
- [Ссылка на GitHub](https://github.com/Victorinca/Skillfactory-Module-D-Theme-D3)


По всем вопросам, которые касаются выполненного задания, можно писать на почту victoriavladimirskaya@gmail.com.
