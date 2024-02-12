#bash 

if [ $# -gt 0 ]; then

    if [ ! -d "target" ]; then
        mvn -q compile  

        if [ $? -ne 0 ]; then
            echo "[ERROR]: compilation failed"
            mvn -q clean
            exit 1
        fi
    fi
    
    
    if [ "$1" = "solution" ]; then
        mvn -q exec:java -Dexec.mainClass="solution.Application"

        if [ $? -ne 0 ]; then
            echo "[ERROR]: build failed"
            mvn -q clean
            exit 1
        fi
    elif [ "$1" = "test" ]; then
        mvn -q test

        if [ $? -ne 0 ]; then
            echo "[ERROR]: test failed"
            mvn -q clean
            exit 1
        fi
    elif [ "$1" = "clear" ]; then
        mvn -q clean
    else
        echo "[ERROR]: invalid argument $1"
    fi

else
    echo "[ERROR]: no argument provided"
fi


