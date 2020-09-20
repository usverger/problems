using Xunit;

namespace Problems
{
    public class TestStrings
    {
        [Fact]
        public void LengthOfLastWord()
        {
            var s = new Problems.Strings();
            Assert.Equal(0, s.LengthOfLastWord(""));
        }
    }
}