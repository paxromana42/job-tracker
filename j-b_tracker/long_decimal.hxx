#ifndef LONG_DECIMAL_HXX
#define LONG_DECIMAL_HXX 

#include <cstddef>
#include <cmath>
#include <string>
#include <stdexcept>
#include <cinttypes>
#include <cstdlib>


// returns the multiple of 10 through 10^n
size_t pow10(size_t);

struct doublet {
  size_t original_number;
  size_t second_number;

  doublet(size_t original_number, size_t second_number)
    : original_number(original_number), second_number(second_number) {}
};


class LongDecimal {
private:
  bool is_signed;
  size_t natural_number;
  size_t decimal;
  size_t decimal_count;

  doublet pair_of_numbers_decimal_adjusted(const LongDecimal& this_obj, const LongDecimal& other) const {
    return doublet(this_obj.natural_number * pow10(this_obj.decimal_count) + this_obj.decimal,
                   other.natural_number * pow10(other.decimal_count) + other.decimal); 
  }

public:
  LongDecimal(bool is_signed, size_t natural_number, size_t decimal);
  
  LongDecimal operator/(const LongDecimal& divisor) const;
  LongDecimal operator*(const LongDecimal& multiplicand) const;

  size_t get_natural_number() const { return natural_number; }
  size_t get_decimal() const { return decimal; }
  bool get_is_signed() const { return is_signed; }
  size_t get_decimal_digits(size_t value)const { return decimal_count; }
  
  std::string output() const;
  size_t calculate_decimal_digits(size_t);
};



#endif  // LONG_DECIMAL_HXX