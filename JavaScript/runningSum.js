/**
 * @param {number[]} nums
 * @return {number[]} temp
 */
var runningSum = function (nums) {
  let temp = [];
  temp.push(nums[0]);
  temp.push(temp[0] + nums[1]);
  for (let i = 1; i < nums.length - 1; i++) {
    temp.push(temp[i] + nums[i + 1]);
  }
  return temp;
};
