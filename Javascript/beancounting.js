function countBs(myString){
    var strCount = 0;
    for(i = 0; i < myString.length; i++) {
        if (myString[i] === "B") {
            strCount = strCount + 1;
        }
    }
    return strCount;
}

function countChar(myString, myLetter){
    var letterCount = 0;
    var chosenLetter = myLetter.toLowerCase();
    for(i = 0; i < myString.length; i++) {
        if (myString[i] === chosenLetter) {
            letterCount = letterCount + 1;
        }
    }
    return letterCount;
}

console.log(countBs("BBC"));
console.log(countBs("BBCBBCBB"));
console.log(countChar("kakkerlak", "K"));
console.log(countChar("babbbalack", "a"));
