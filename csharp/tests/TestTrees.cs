using Xunit;
using System.Collections.Generic;

namespace Problems
{
    public class TestTrees
    {
        [Fact]
        public void MaxDepth()
        {
            var s = new Problems.Trees();
            var root = s.GenerateTreeNode(null, 0, new List<int?>{3,9,20,null,null,15,7});
            Assert.Equal(3, s.MaxDepth(root));
        }
    }
}