"""
A tool for using view functions without templates.
Will render
"""

class RawResponseMiddleware(object):
    
    
    def process_response(self, request, response):
        """
        Wraps the response body in <pre></pre> tags to avoid http rendering
        
        Will NOT do so to admin pages
        Will NOT do so unless status code is 200 
        """
        
        if (not request.path.startswith('/admin')) and response.status_code == 200:
            escaped_content = (response.content
                                .replace('&','&amp;')
                                .replace('<','&lt;')
                                .replace('>','&gt;')
                                .replace('"','&quot;'))
            response.content = "<pre>%s</pre>" % escaped_content
        
        return response