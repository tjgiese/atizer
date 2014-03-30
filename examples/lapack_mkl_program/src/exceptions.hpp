#ifndef _lalg_exceptions_hpp_
#define _lalg_exceptions_hpp_

#include <string>
#include <sstream>

namespace lalg
{
  class exception : public std::exception
  {
  public:
    exception( char const * msg ) : _what(msg) {};
    virtual ~exception() throw() {};
    virtual void rethrow() const { throw *this; };
    char const * what() const throw() { return _what.c_str(); };
  protected:
    std::string _what;
  };

  class illegal_argument : public lalg::exception
  {
  public:
    illegal_argument( char const * msg, int const i ) 
      : lalg::exception(msg) 
    {
      std::stringstream m;
      m << "; argument " << i;
      _what += m.str();
    };
    virtual ~illegal_argument() throw() {};
    virtual void rethrow() const { throw *this; };
  };

}


#endif
