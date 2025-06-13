// Array of random animal facts to be pulled in
let facts = [
  `<h5 id='quoteTitle'>Elephants can recognize themselves in mirrors</h5>
  <p id='quote'>Elephants are one of the few animal species that can pass the mirror test.</p>`,
  `<h5 id='quoteTitle'>Polar bears have black skin</h5>
  <p id='quote'>While their fur is white, their skin is actually black, which helps them absorb heat from the sun.</p>`,
  `<h5 id='quoteTitle'>Sloths have very sluggish digestion</h5>
  <p id='quote'>Sloths have a very slow metabolism, and their digestive process can take up to a month to complete.</p>`,
  `<h5 id='quoteTitle'>Flamingos are naturally white</h5>
  <p id='quote'>Their pink color comes from the carotenoids in the algae and brine shrimp they eat.</p>`,
  `<h5 id='quoteTitle'>Butterflies taste with their feet</h5>
  <p id='quote'>Butterflies have taste receptors on their feet that they use to determine if a plant is poisonous or not.</p>`,
  `<h5 id='quoteTitle'>Cows have best friends</h5>
  <p id='quote'>Cows are social animals and form close friendships, and they can experience stress when separated from their preferred companions.</p>`,
  `<h5 id='quoteTitle'>Kangaroos cannot walk backwards</h5>
  <p id='quote'>Kangaroos have large tails and feet that make it difficult for them to move in reverse.</p>`,
  `<h5 id='quoteTitle'>Otters hold hands while sleeping</h5>
  <p id='quote'>Otters hold hands while they sleep to prevent drifting apart in the water.</p>`,
  `<h5 id='quoteTitle'>Giraffes have purple tongues</h5>
  <p id='quote'>Giraffes have tongues that are dark, ranging from purple to black, due to high melanin content.</p>`,
];

// Function generate a random order
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}

// call getRandomInt function to generate a random number from 0 to the length of facts array
currentFact = getRandomInt(0, facts.length);
// set the DOM
element = document.getElementById("animalFacts");
// put the random fact into the HTML of our ID
element.innerHTML = facts[currentFact];
