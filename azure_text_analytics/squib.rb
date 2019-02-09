here = File.dirname(__FILE__)
require_relative 'azure'

azure = Azure.new(File.join(here, 'credentials.json'))

azure.analyze(Dir.glob(File.join(here, "..", "documents", "*.txt")))
azure.write_results
