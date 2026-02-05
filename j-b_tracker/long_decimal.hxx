#ifndef LONG_DECIMAL_HXX
#define LONG_DECIMAL_HXX 

#include <cstddef>
#include <cmath>
#include <string>
#include <stdexcept>
#include <cinttypes>
#include <cstdlib>

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

  doublet pair_of_numbers_decimal_adjusted(const LongDecimal& this_obj, const LongDecimal& other) const {
    // Figure out lenght of decimal parts to convert the numbers to integers
    size_t decimal_places_to_move = std::max(std::log10(this_obj.decimal), std::log10(other.decimal));

    if (decimal_places_to_move < 0)
      throw std::runtime_error("Decimal places to move cannot be negative");
    
    // Convert both numbers to integers by shifting decimal places
    // if (decimal_places_to_move != 0)
    size_t temp_this = this_obj.natural_number * std::pow(10, decimal_places_to_move) + this_obj.decimal; 
    size_t temp_other = other.natural_number * std::pow(10, decimal_places_to_move) + other.decimal;
    
    return doublet(temp_this, temp_other); 
  }

public:
  LongDecimal(bool is_signed, size_t natural_number, size_t decimal);
  
  LongDecimal operator/(const LongDecimal& divisor) const;
  LongDecimal operator*(const LongDecimal& multiplicand) const;

  size_t get_natural_number() const { return natural_number; }
  size_t get_decimal() const { return decimal; }
  bool get_is_signed() const { return is_signed; }

  
  std::string output() const;
};

// size_t ipow10(size_t);

#endif  // LONG_DECIMAL_HXX