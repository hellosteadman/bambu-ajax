from bambu_ajax import site

@site.register
def test_function(request):
    return True
