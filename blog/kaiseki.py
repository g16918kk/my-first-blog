# coding: utf-8
import sys
import MeCab
import cgi
import io

def result(request):
    return render(request, 'blog/hoge3.html')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
form = cgi.FieldStorage()
if 'sentense' not in form:
    print('Content-type: text/html; charset=UTF-8')
    print('')
    print('sentense フィールドが送信されていません。')
    sys.exit()

print('Content-type: text/html; charset=UTF-8')
print('')
print(sentense) 
