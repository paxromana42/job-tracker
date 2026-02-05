#include "long_decimal.hxx"

// Implement long decimal functionalities here

// Only Partially implemented for demonstration purposes

// Constructor(with initializer list) for LongDecimal class with parameters to 
// determine if the number is signed, its natural part and its decimal part.
// is_signed: true if the number is negative, false otherwise
inline LongDecimal::LongDecimal(bool is_signed, size_t natural_number, size_t decimal)
  : is_signed(is_signed), natural_number(natural_number), decimal(decimal) {};

inline LongDecimal LongDecimal::operator/(const LongDecimal& divisor) const {
  // Division logic for LongDecimal
  // Note: This is a simplified version and may not handle all edge cases.
  
  // Check if dividing by zero
  if (divisor.natural_number == 0 && divisor.decimal == 0)
    throw std::runtime_error("Division by zero");
  
  auto temp = pair_of_numbers_decimal_adjusted(*this, divisor);
  auto temp_this = temp.original_number;
  auto temp_other = temp.second_number;

  // Perform integer division
  auto div_result = imaxdiv(temp_this, temp_other);

  // Output the result above, plus inline sign handling
  return LongDecimal(this->is_signed != divisor.is_signed, div_result.quot, div_result.rem);
};

inline LongDecimal LongDecimal::operator*(const LongDecimal& multiplicand) const {
  // Multiplication logic for LongDecimal
  // Note: This is a simplified version and may not handle all edge cases.
  auto temp = pair_of_numbers_decimal_adjusted(*this, multiplicand);
  auto temp_this = temp.original_number;
  auto temp_other = temp.second_number;
  auto result = temp_this * temp_other;

  // Calculate natural and decimal parts of the result
  size_t scale = std::log10(std::max(this->decimal, multiplicand.decimal));
  size_t result_natural = result / scale;
  size_t result_decimal = result % scale;

  // Output the result above, plus inline sign handling
  return LongDecimal(this->is_signed != multiplicand.is_signed, result_natural, result_decimal);
};




inline std::string LongDecimal::output() const{
  std::string sign = is_signed ? "-" : "";
  return sign + std::to_string(natural_number) + "." + std::to_string(decimal);
};

// inline size_t ipow10(size_t exp) {
//     size_t result = 1;
//     while (exp--) result *= 10;
//     return result;
// }