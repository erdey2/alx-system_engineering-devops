#!/usr/bin/env ruby
# validate telephone number
puts ARGV[0].scan(/^\d{10}$/).join
