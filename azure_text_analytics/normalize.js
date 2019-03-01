#! /usr/bin/env node
const fs = require('fs');
const path = require('path');

const inputPath = process.argv[2];
console.log(`Opening ${inputPath}`);
let data = JSON.parse(fs.readFileSync(inputPath, {encoding: 'utf-8'}));

let contents = { entities: []};
function extractEntities(entityData){
  let id = entityData.bingId;
  let label = (entityData.subType) ? entityData.subType : entityData.type;
  let entity = {
    id: id,
    name: entityData.name,
    wikipediaUrl: entityData.wikipediaUrl,
    type: label,
    matches: []
  };
  entityData.matches.forEach((match) => {
    entity.matches.push({
      id: id,
      start: match.offset,
      end: match.offset+match.length,
      label: label
    });
  });
  contents.entities.push(entity);
}

data.documents[0].entities.forEach(extractEntities);

const dirname = path.dirname(inputPath);
const basename = path.basename(inputPath, ".json");
const outputPath = path.join(dirname, `${basename}.azure.json`);
console.log(`Writing to ${outputPath}`);
fs.writeFileSync(outputPath, JSON.stringify(contents));