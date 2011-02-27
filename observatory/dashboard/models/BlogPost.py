# Copyright (c) 2010, individual contributors (see AUTHORS file)
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from django.core.urlresolvers import reverse
from django.db import models
from Event import Event
from Blog import Blog

# a post in a blog
class BlogPost(Event):
  class Meta:
    app_label = 'dashboard'
  
  # the source text of internally hosted blog posts
  markdown = models.TextField("Content")
  
  # the rendered content of blog posts
  content = models.TextField()
  
  # what blog the post is associated with
  blog = models.ForeignKey(Blog)
  
  # the external link for a post, if applicable
  external_link = models.URLField(blank = True, null = True)
  
  # an md5 checksum of the content, to prevent duplicates
  md5 = models.CharField(max_length = 32)
    
  def autoescape(self):
    return False
  
  def type_name(self):
    return "Post"

