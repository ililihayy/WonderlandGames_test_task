# WonderlandGames_test_task
Хрестики-нолики описані за допомогою паттерну MVC. 

  MVC - це шаблон для проектування архітектури проекту. Його суть це: model-view-controller. Тобто шаблон поділяє архітектуру на три частини, які взаємопов'язані.   
  
  У частині Model знаходить основна логіка програми, бази даних(якщо вони є). 
  
  У View - інтерфейс користувача, всі візуальні елементи. 
  
  Controller відповідає за зв'язок перших двох частин. Це проміжний код між першими двома частинами, який приймає зміни, та виконує взаємодію між логікою програми та інтерфейсом.
  
Використання цього паттерну дозволяє легше редагувати великий проект, особливо коли над ним працює багато людей. Також, сильно спрощується паралельна розробка, адже кожна команда може працювати над різним блоком коду. Загалом MVC досить зручний, особливо для роботи з графічним інтерфейсом. 


Коротко про архітектуру проєкту:
 
### class Model: 
Містить основну логіку гри, а саме методи для перевірки виграшу, нічиї та метод із процесом гри.

 - xWinner(self, map)

 - oWinner(self, map)

 - draw(self, map)

 - playGame(self, player1, player2)

### class View:
Містить два методи: 

- printMap(self, map) - виводить карту на консоль

- greeting(self) - запитує імена користувачів


### class Controller:
Також два методи:

- playerMove(self, player_name, map, symbol) - запитує  в гравця його хід, та перевіряє чи місце не зайняте та чи номер клітинки валідний

- newGame(self, player1, player2) - починає нову гру, якщо написати "+"