const groupCount = 6;

/**
 * 
 * @param {Array} array array to be sorted
 * @returns
 */
function shiftLeft(array) {
  let len = array.length;
  let result = [];

  for (let i = 0; i < len; i++) {
    if (i == 0) result[len - 1] = array[0];
    else result[i - 1] = array[i];
  }

  return result;
}

/**
 * Function to measure which group has to wait more for JCL.
 * @param {Integer} sessionCount number of LBAW Lab Classes
 * @returns {Map} Group -> Score. More score is worse, like in golf.
 */
function determinePoints(sessionCount) {
  let points = []
  let groups = []

  for (let i = 0; i < groupCount; i++) {
    groups.push(i + 1);
    points.push(0);
  }

  for (let i = 0; i < sessionCount; i++) {
    for (let j = 0; j < groupCount; j++) {
      points[groups[j] - 1] += j;
    }
    groups = shiftLeft(groups);
  }

  let score = groups.map((e, i) => [e, points[i]]);

  return score;
}


// script here
determinePoints(13);