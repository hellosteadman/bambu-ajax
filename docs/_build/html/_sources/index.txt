Bambu AJAX
==========

AJAX utility functions for Django that can be accessed via a single URL
(ala WordPress admin-ajax.php)

About Bambu AJAX
----------------

Bambu AJAX lets you write utility functions for your Django apps that
can be called via AJAX, without having to specify a separate URL pattern
and view for each one.

Installation
------------

Install the package via Pip:

::

    pip install bambu-ajax

Add it to your ``INSTALLED_APPS`` list:

.. code:: python

    INSTALLED_APPS = (
        ...
        'bambu_ajax'
    )

Add ``bambu_ajax.urls`` to your URLconf:

.. code:: python

    urlpatterns = patterns('',
        ...
        url(r'^ajax/', include('bambu_ajax.urls')),
    )

Basic usage
-----------

Create a file called ``ajax.php`` within your Django app, and import the
necessary module from the ``bambu-ajax`` package, like so:

.. code:: python

    from bambu_ajax import site

    @site.register
    def my_ajax_function(request):
        return [
            'a', 'list', 'of', 'things'
        ]

Using the ``site.register`` decorator registers your AJAX function with
the ``bambu_ajax`` view.

To leverage this function from within a Django template, use the
``ajaxurl`` template tag, like so:

.. code:: html

    {% load ajax %}
    <script>
        $.getJSON('{% ajaxurl 'my_project.my_app.my_ajax_function' %}&callback=?',
            function(data) {
                console.log(data);
            }
        );
    </script>

Here, ``my_project`` should refer to the name of your Django project,
``my_app`` should be the name of the app you put your ``ajax.py`` file
in, and ``my_ajax_function`` is the name of the function you defined
within ``ajax.py``.

The notation is similar to that used when referring to Django models, in
that you always skip the common portion ``ajax`` from the naming
convention.

Shortcut
--------

Make your life easier by including the utility library in your template:

.. code:: html

    <script src="{% url 'ajax_utility' %}"></script>
    <script>
        bambu.ajax.get('my_project.my_app.my_ajax_function',
            function(data) {
                console.log(data);
            }
        );
    </script>

This achieves the same result, but in a much cleaner way.

Dynamically updating page content
---------------------------------

As well as returning JSON-serialisable data per the examples above, you
can also use AJAX functions just like views, in that they can return an
``HttpResponse`` object.

Using that method, the example above would print out the HTML (or other
data) returned in the HTTP response.

Additional decorators
---------------------

You can of course add other decorators, just as you would with normal
views.

Todo
----

-  Add a dedicated ``login_required`` decorator that returns a more
   helpful response for anonymous users
-  Look into integrating this with `Plunja`_, my dynamic JavaScript
   templating library.

Questions or suggestions?
-------------------------

Find me on Twitter (@iamsteadman) or `visit my blog`_.

.. _Plunja: http://iamsteadman.github.io/plunja/
.. _visit my blog: http://steadman.io/
