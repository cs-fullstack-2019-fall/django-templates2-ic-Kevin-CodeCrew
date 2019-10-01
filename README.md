# Template inheritance with Django

## Lecture:
Demonstrate the basics of templat inheritence in Django. Discuss named blocks and basic rules for their use.

* Create your ```templates``` location uder your app directory, then create 2 template files, ```base.html``` and ```child.html```.
* Using ```base.html``` as the parent template, create a basic header and footer. Add named blocks for the title, header, and footer. In the body add block named ```content``` that produces no content by default.
* Using ```child.html``` template, extend the base template and update the header and footer blocks. In the content block, add a simple for filter that will iterate through an array called ```entries``` that will be injected by the view, printing each element as a paragraph.
* Create an endpoint and view called ```base``` that will render the base template.
* Create an endpoint and view called ```child``` that will render the child template while injecting the following ```cars``` array into the context. ```cars = ['Honda', Toyota', 'GM', 'Nissan']```

Observe how the output differs depending on which template is rendered from the view.

## Exercises IC:

### Exercise 1:
* Create your ```templates``` location uder your app directory, then create 2 template files. ```blog.html``` and ```blog_entry.html```
* Using ```blog.html``` as the parent template, create a basic header with ```<h1>``` that says "My Blog" and a named block for a subtitle using an ```<h2>``` tag. In the body add a block named ```content``` iterate the array of dictionay entries (provided below) and a CSS grid with 2 columns. The first column should display the date of the entry and the second column should contain a hyperlink generated from the blog post title and its ```post_index``` (e.g. http://localhost:8000:blog_entry/2) (note: use the ```url``` helper and the named route you will create below)
* Using ```blog_entry.html` with a block named ```content``` that will display the blog date, blog title, and blog text for the selected entry.
* Create an endpoint that will route to a view the renders the 'blog_entry' and uses the index value from the URL to display the appropriate entry. It should include a url generated link back to the main page.

Data for entries:
```
blog_posts = [
  {
    'post_index': 0,
    'post_date': '01/08/2019',
    'post_title': 'Starting my journey!',
    'post_text': 'My first day of Code School! A little nervous, but mostly excited about what is to come!'
  },
  {
    'post_index': 1,
    'post_date': '02/02/2019',
    'post_title': 'Making Progress',
    'post_text': 'The class moves fast, and can be hectic, but I am learning a lot. I am confident I can do this!'
  },
  {
    'post_index': 2,
    'post_date': '02/19/2019',
    'post_title': 'Django',
    'post_text': 'Django is our first server-side, or backend framework we have learned. It has lots of moving parts but is clearly powerful. I will soon officially be developing fullstack applications!'
  }

]
