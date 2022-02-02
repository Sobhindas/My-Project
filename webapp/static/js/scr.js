let x=0;

    setInterval(time,2000)
     function time()
    {

            if(x==0)

            {

                document.getElementById("time1").src="/static/img/wall paper/wall4.png";
                console.log(x);
                x++;


            }
            else if(x==1)
            {
                document.getElementById("time1").src="/static/img/wall paper/wall2.png";
                 console.log(x);
                  x++;
            }
            else if(x==2)
            {
                document.getElementById("time1").src="/static/img/wall paper/wall3.png";
                console.log(x);
                x=0;

            }

    }




