# include <iostream>
# include <vector>

#include "long_decimal.cc"

int main(){
  // std::cout<<"Hi Mom";


  const LongDecimal A5[] = {LongDecimal(false, 148, 0), LongDecimal(false, 210, 0)}; // A5 dimensions in MM: 148mm x 210mm
  const LongDecimal PT_TO_MM = LongDecimal(false, 0, 3528);// 1 PT = 0.3528 MM
  const LongDecimal A5_HEIGHT_PT = {A5[1]*PT_TO_MM}; // A5 height in points


  std::vector<LongDecimal>divisors_a5;

  // Populate divisors_a5 with the divisiors of a set of natural numbers and PT_TO_MM

  for (auto i = 0; i < 60; ++i)
    divisors_a5.push_back(A5_HEIGHT_PT/LongDecimal(false, i+1, 0));
  

  // Output the results
  for(auto i : divisors_a5)
    std::cout<<i.output()<<std::endl;

  return 0;
}