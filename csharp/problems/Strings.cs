using System.Linq;

namespace Problems
{
    public class Strings
    {
        public int LengthOfLastWord(string s)
        {
            var split = s.Split(s, System.StringSplitOptions.RemoveEmptyEntries);
            if (split.Length == 0) return 0;
            return split.Last().Length;
        }
    }
}