#ifndef STRINGSINGLETON_H
#define STRINGSINGLETON_H
#include <string>

class StringSingleton
{
    //private:
	public:      
  std::string mString;
        StringSingleton() {}
        StringSingleton(const StringSingleton& right) {}
        const StringSingleton& operator=(const StringSingleton &old) {}
        //virtual ~StringSingleton() {}
    protected:
    public:
        std::string GetString() const
        {
            return mString;
        }
        void SetString (const std::string &newString)
        {
            mString = newString;
        }
        static StringSingleton &Instance()
        {
            static StringSingleton* instance = new StringSingleton;
            return *instance;
        }
};

#endif // STRINGSINGLETON_H
