Goals
======

short-term
----------

* model
* test model migration using django (import/export, model upgrade)

v1.0 codename 'Jean-Pierre Debondt'
-----------------------------------

be as powerful as the files of the ex-president, Jean-Pierre.

that is:

* hold user details:
  * name
  * birthdate
  * phone number(s)
  * address
  * email
  * picture
* subscription of a user
  * before subscription
    * documents submitted
    * amount paid
  * after
    * subscription completion date
    * subscription validity start date
* subscription
  * price
  * validity criterion/criteria
    * number of lessons since subscription validity start date
    * validity end date
* documents received by user
  * date given to user
  * who gave document
  * transmission method (post, by hand?)
  * document
* lessons
  * time
  * place


long-term
---------

* hold user level (Yoseikan budo? more general?) => introduce levels table?

* introduce module/exercise (e.g. 2014 lessons, special track, ...)
  * lessons belong to a module
  * subscriptions can be valid only for a module => new validity criterion

* validity on a period of time starting from the subscription validity start date
