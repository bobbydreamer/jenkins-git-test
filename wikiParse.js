//https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States
const rp = require('request-promise');
const cheerio = require('cheerio');
const url = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States';

rp(url)
  .then(function(html){
    //success!
    $ = cheerio.load(html);
    const wikiUrls = [];
    for (let i = 0; i < 46; i++) {
      wikiUrls.push($('td > b > a', html)[i].attribs.title);
    }
    console.log(wikiUrls);
  })
  .catch(function(err){
    //handle error
  });