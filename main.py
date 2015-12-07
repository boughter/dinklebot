#!/usr/bin/env python

import json
import logging
import webapp2

import commands
import slack

class CommandHandler(webapp2.RequestHandler):
  def post(self):
    logging.info('request params: %s', self.request.params)
    full_command_text = slack.get_text(self.request)
    command, extra = commands.parse(full_command_text)
    slack_response = slack.response(command(extra), command.is_private)
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(json.dumps(slack_response))

app = webapp2.WSGIApplication([
    ('/v1/', CommandHandler)
], debug=True)
