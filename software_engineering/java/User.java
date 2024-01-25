import java.util.Queue;

public class User
{
    private static Long next_id = 0L;
    private Long id = next_id++;

    private String name;

    public User(String name)
    {
        this.name = name;
        //System.out.println("User " + id + " created.");
    }

    public Long getId()
    {
        return id;
    }

    public String getName()
    {
        return name;
    }
}