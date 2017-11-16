# -*- coding: utf-8 -*-
__author__ = 'kikita'

import os, sys, json, urllib, urllib2, httplib, urlparse, mimetools, mimetypes
from cStringIO import StringIO

# generates a new token from Portal
def generate_token(baseurl, username, password):
    tokenUrl = urlparse.urljoin(baseurl, 'sharing/generateToken')
    postdata = { 'username': username, 'password': password,
               'client': 'requestip', 'expiration': 60, 'f': 'json' }
    encoded_postdata = urllib.urlencode(postdata)
    opener = urllib2.build_opener()
    try: resp = opener.open(tokenUrl, data=encoded_postdata)
    except urllib2.HTTPError as e: raise Exception('Unable to connect to Portal, please check the url: {} {}'.format(e.code, e.reason))
    resp_json = json.loads(resp.read())
    if 'error' in resp_json: raise Exception('\n'.join(resp_json['error']['details']))
    return resp_json['token']
    sys.exit(1)

# create proper multi-part POST request data
def _encode_multipart_formdata(fields, files):
    boundary = mimetools.choose_boundary()
    buf = StringIO()
    for (key, value) in fields.iteritems():
        buf.write('--%s\r\n' % boundary)
        buf.write('Content-Disposition: form-data; name="%s"' % key)
        buf.write('\r\n\r\n%s\r\n' % str(value))
    for (key, filepath, filename) in files:
        buf.write('--%s\r\n' % boundary)
        buf.write('Content-Disposition: form-data; name="%s"; filename="%s"\r\n' % (key, filename))
        buf.write('Content-Type: %s\r\n' % (mimetypes.guess_type(filename)[0] or 'application/octet-stream'))
        f = open(filepath, "rb")
        try:
            buf.write('\r\n' + f.read() + '\r\n')
        finally:
            f.close()
    buf.write('--' + boundary + '--\r\n\r\n')
    buf = buf.getvalue()
    return boundary, buf

# send multi-part POST request
def _postmultipart(host, selector, fields, files, ssl):
    boundary, body = _encode_multipart_formdata(fields, files)
    headers = { 'Content-Type': 'multipart/form-data; boundary={0}'.format(boundary) }
    if ssl: h = httplib.HTTPSConnection(host)
    else: h = httplib.HTTPConnection(host)

    h.request('POST', selector, body, headers)
    resp = h.getresponse()

    return resp.read()

# first upload the SD file and create an item in Portal
def addSDItem(baseurl, user, token, title, file, folder = ''):
    addUrl = 'sharing/rest/content/users/{}/{}addItem'
    if folder != '': addUrl = addUrl.format(user, folder + '/')
    else: addUrl = addUrl.format(user, '')

    url = urlparse.urljoin(baseurl, addUrl)

    files = [('file', file, os.path.split(file)[1])]
    fields = { 'token' : token, 'f' : 'json', 'type' : 'Service Definition', 'title' : title,
               'tags' : 'sampletag', 'name': title, 'typeKeywords' : 'Data, Service Definition, ArcGIS, sd' }

    ssl = url.startswith('https://')

    parsed_url = urlparse.urlparse(url)

    print('Uploading {} to {}..'.format(file, baseurl))
    resp = _postmultipart(parsed_url.netloc, str(parsed_url.path), fields, files, ssl)
    resp_json = json.loads(resp)

    if 'error' in resp_json:
      raise Exception('Unable to upload file {}: {}'.format(file, resp_json['error']['message']))

    return resp_json['id']

# second publish the uploaded SD item as a new tiled service
def publishTiles(baseurl, user, token, itemid):
    publishUrl = urlparse.urljoin(baseurl, 'sharing/rest/content/users/{}/publish'.format(user))
    query_dict= { 'f' : 'json', 'token': token, 'itemid': itemid, 'buildInitialCache' : True,
                  'publishParameters' : { 'name' : 'cities' }, 'fileType': 'serviceDefinition' }

    query_string = urllib.urlencode(query_dict)
    print('Publishing tile service from item..')
    response = urllib.urlopen(publishUrl, query_string)

    resp_json = json.loads(response.read())

    if 'error' in resp_json: raise Exception('Unable to publish item: {}'.format(resp_json['error']['message']))

# read input from command line when run as a standalone script
if __name__ == '__main__':
    try:
      url = sys.argv[1]
      user = sys.argv[2]
      password = sys.argv[3]
      f = sys.argv[4]
      title = sys.argv[5]
      if not url.endswith('/'): url += '/' # make sure the url ends with /
    except: # if too few parameters are passed on command line, show usage help
      print('Usage: ')
      print('       publishServiceItem.py [portalUrl] [userName] [password] [sdFilePath] [titleOfServiceItem]')
      print('')
      print('portalUrl           The secure url to the portal, e.g. https://portalmachine.example.com/arcgis/')
      print('userName            The username of a user to publish the service.')
      print('                    This user must have the required publishing privileges.')
      print('password            The password of the user')
      print('sdFilePath          Path to the .sd file containing the service definition')
      print('                    E.g. c:\\temp\cachedService.sd')
      print('titleOfServiceItem  The title to assign to the published item in the portal.')
      sys.exit(1)

    token = generate_token(url, user, password)

    id = addSDItem(url, user, token, title, f)
    publishTiles(url, user, token, id)
    print('Publishing complete. Tile generation has been started and may take a while to finish.')