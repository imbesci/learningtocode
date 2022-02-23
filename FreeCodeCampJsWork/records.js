// Setup
const recordCollection = {
    2548: {
      albumTitle: 'Slippery When Wet',
      artist: 'Bon Jovi',
      tracks: ['Let It Rock', 'You Give Love a Bad Name']
    },
    2468: {
      albumTitle: '1999',
      artist: 'Prince',
      tracks: ['1999', 'Little Red Corvette']
    },
    1245: {
      artist: 'Robert Palmer',
      tracks: []
    },
    5439: {
      albumTitle: 'ABBA Gold'
    }
  };
  
  // Only change code below this line
  function updateRecords(records, id, prop, value) {
    if (value === ''){
        delete recordCollection[id][prop];
        return recordCollection;
    }

    if (prop === 'artist' || prop === 'albumTitle'){
        recordCollection[id][prop] = value;
    }
    if (prop === 'tracks'){
        if (recordCollection[id].hasOwnProperty(prop)){
            recordCollection[id][prop].push(value);
        } else {
            recordCollection[id][prop] = [value];
        }
    }
    return recordCollection;
  }
  
  
  
console.log(updateRecords(recordCollection, 2548, "artist", ""));

