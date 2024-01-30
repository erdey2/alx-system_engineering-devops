#!/usr/bin/env ruby
# validate telephone number
puts ARGV[0].scan(/[0-9]{10}/).join
