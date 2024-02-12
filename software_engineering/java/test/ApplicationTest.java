package test;
import org.junit.Test;

import solution.User;

public class ApplicationTest
{

    @Test
    public void testApplication()
    {
        System.out.println(" ApplicationTest.testApplication()");

        User user1 = new User("peter");
        User user2 = new User("fireship");

        assert user1.getId() != user2.getId();
    }

}