package solution;
import java.util.Collections;

import java.util.HashSet;
import java.util.Set;

/**
 * User
 * 
 * This class represents a user.
 * A user can join a league.
 * A user can leave a league.
 * 
 * @param name The name of the user.
 */

public class User
{
    private static Long next_id = 0L;
    private Long id = next_id++;

    private final String name;

    private Set<League> leagues = new HashSet<League>();

    public User(String name)
    {
        this.name = name;
        //System.out.println("User " + id + " created.");
    }

    /**
     * Get the id of the user.
     * 
     * @return The id of the user.
     */

    public Long getId()
    {
        return id;
    }

    /**
     * Get the name of the user.
     * 
     * @return The name of the user.
     */

    public String getName()
    {
        return name;
    }

    /**
     * Get the leagues the user has joined.
     * 
     * @return The leagues the user has joined.
     */

    public Set<League> getLeagues()
    {
        return Collections.unmodifiableSet(leagues);
    }

    /**
     * Join a league.
     * 
     * @param league The league to join.
     */

    public void join(League league)
    {
        if (!leagues.contains(league)) {
            leagues.add(league);
        }
    }

    /**
     * Leave a league.
     * 
     * @param league The league to leave.
     */

    public void leave(League league)
    {
        if (league != null) {
            leagues.remove(league);
        }
    }
}