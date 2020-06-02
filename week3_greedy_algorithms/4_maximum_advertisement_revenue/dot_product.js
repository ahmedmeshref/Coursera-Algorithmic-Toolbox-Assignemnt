/**
 * max_ads_revenue function distribute the ads profite given in a list a among the slots given in b to
 * maximize the total revenue.
 * @param a: list of integers, where a𝑖 represents the profit per click of the 𝑖-th ad
 * @param b: list of integers, where b𝑖 is the average number of clicks per day of the 𝑖-th slot
 * @returns {*} an integer represents the max profit possible of placing the ads on the website
 */
let max_ads_revenue = function(a, b) {
    a.sort((a, b) => a - b)
    b.sort((a, b) => a - b)
    return a.reduce((tot, c_val, i) => tot + (c_val * b[i]), 0)
}




