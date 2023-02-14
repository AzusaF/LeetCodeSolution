/**
 * 88. Merge Sorted Array
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
 var merge = function(nums1, m, nums2, n) {
   let tempindex= 0; let nums2index=0; let nums1index=0;
   let temp = [...nums1];
   while((nums1index < m+n)&&(n!=0)) {
      // console.log("temp ", temp[tempindex]);ß
      // console.log("num2 ", nums2[nums2index]);
      if((temp[tempindex]<nums2[nums2index])&&(m > tempindex)||(n < nums2index)){
         // console.log("if ", nums1[nums1index]);
         nums1[nums1index]=temp[tempindex];
         tempindex++;
      }else{
         nums1[nums1index]=nums2[nums2index];
         nums2index++;
         // console.log("else ", nums1[nums1index]);
      }
      nums1index++;
   }
};