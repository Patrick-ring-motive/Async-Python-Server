from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import asyncio
from api.promises import *
from api.excepts import *
from api.xhttp import *
from api.zfile import *


class handler(BaseHTTPRequestHandler):

  async def do_ASYNC(request, data):
      content = zreadFile('templates/index.html')
      await zsendHeaders(request,{'status':200,'Content-type':'text/html'})
      await zwriteResponseBody(request, b(content))

  def do_METHOD(request):
    asyncio.run(request.do_ASYNC(request))

  do_GET = do_METHOD
  do_OPTIONS = do_METHOD
  do_POST = do_METHOD
  do_PUT = do_METHOD
  do_PATCH = do_METHOD
  do_HEAD = do_METHOD
  do_DELETE = do_METHOD
  do_CONNECT = do_METHOD
  do_TRACE = do_METHOD