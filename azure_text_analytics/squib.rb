here = File.dirname(__FILE__)
require File.join(here, 'azure.rb')

azure = Azure.new(File.join(here, 'credentials.json'))

azure.analyze(Dir.glob(File.join(here, "..", "documents", "*.txt")))
azure.write_results
