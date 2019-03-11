require 'nokogiri'
require 'json'

input_path = ARGV.first

# read the marked up output and pretend it's HTML
data = Nokogiri::HTML::fragment(File.read(input_path))

# iterate over all of the text spans, and keep a running 
# tally of the position.
entities = []
data.children.reduce(0) do |position, span| 
  # The start and end positiosn are
  # the current cumultative position we've kept
  # and the lenght of the current span.
  end_position = position+span.text.length; 
  if span.name != 'text'
    entities.push({
      name: span.text,
      type: span.name,
      matches:[{
        'start': position,
        'end':   end_position,
        label:   span.name
      }]
    })
  end
  end_position # make sure to exit the loop w/ the end position
end

basename = File.basename(input_path, ".*")
out_path = File.join(".", "#{basename}.stanford.json")
File.open(out_path,'w'){ |f| f.write({entities: entities}.to_json) }
