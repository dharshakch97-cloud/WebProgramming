function deepEqual(a, b) {
    if (a === b) return true;
    if (a == null || typeof a != 'object' || b == null || typeof b != 'object') {
        return false;
    }
    var propsInA = 0, propsInB = 0;
    for (var p in a)
        propsInA += 1
    for (var p in b)
        propsInB += 1
        if (!(p in a) || deepEqual(a[p], b[p]))
            return false
    return propsInA == propsInB
}

obj1 = { fn: "dharshak", ls:"ch" }
obj2 = { fn: "Swappdev", number: 12 }

str1 = "dh"
str3 = "harsha"
str2 = 83
console.log(deepEqual(obj1, obj2))
console.log(deepEqual(str1, str2))
console.log(deepEqual(str1, str1))
