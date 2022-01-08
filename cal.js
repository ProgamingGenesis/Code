const xs = [0.5, 2.5, 1, 2, 0.5, 1, 2, 1, 1.5, 2.5]
const ys = [4.5, 1.6, 3, 1.8, 5, 4.2, 2.4, 3.6, 3.3, 1.4]

let slope = -1.5
let yint = 5.5

for (let i = 0; i < 10; i++){
	let nums = xs[1] * slope
	console.log("Predicted: ", nums)

	let r = nums - ys[i]
	console.log("Residual: ", r)
} 
