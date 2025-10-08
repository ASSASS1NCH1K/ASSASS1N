from django.shortcuts import render

def test_templates(request):
    return render(request,
                  'test.html',
                  {
                      'sometext': 'Hello World'
                  })
