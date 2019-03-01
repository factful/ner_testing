#! /usr/bin/env node
const fs = require('fs');
const path = require('path');

// todo: error message if there aren't two
// paths.
const textPath = process.argv[2];
console.log(`Opening text from ${textPath}`);
let binaryText = fs.readFileSync(textPath);

const inputPath = process.argv[3];
console.log(`Opening entities from ${inputPath}`);
let data = JSON.parse(fs.readFileSync(inputPath, {encoding: 'utf8'}));

let contents = { entities: []};
function extractEntities(entityData){
  let id = (entityData.metadata && entityData.metadata.mid);
  let label = entityData.type;
  let wikipediaUrl = (entityData.metadata && entityData.metadata.wikipediaUrl);
  let entity = {
    id: id,
    name: entityData.name,
    wikipediaUrl: wikipediaUrl,
    type: label,
    matches: []
  };
  entityData.mentions.forEach((match) => {
    let supposedOffset = match.text.beginOffset;
    if (supposedOffset <= 0) { 
      throw "Offset is negative (you probably didn't send a character encoding to Google)"; 
    }
    let binarySlice = binaryText.slice(0,supposedOffset);
    let start = binarySlice.toString('utf8').length;
    let end   = start + match.text.content.length;

    entity.matches.push({
      id:    id,
      start: start,
      end:   end,
      label: label
    });
  });
  contents.entities.push(entity);
}

data.entities.forEach(extractEntities);

const dirname = path.dirname(inputPath);
const basename = path.basename(inputPath, ".json");
const outputPath = path.join(dirname, `${basename}.google.json`);
console.log(`Writing to ${outputPath}`);
fs.writeFileSync(outputPath, JSON.stringify(contents));