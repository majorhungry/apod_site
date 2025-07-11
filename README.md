**What is this?**

This pulls NASA's 'Astronomy Picture of the Day' and displays in a webpage with the description and an option to download the photo as well. 

**What You Need**

NASA's API key in a .env file in the root of the project.
You can get one for free at https://api.nasa.gov/
```
nasa_api_key=INPUT_YOUR_API_KEY
```

**How to Run?**

You will need to build the docker image and then run
it. I have provided a docker compose file if you
prefer to run it that way.

Clone this repository
```bash
git clone https://github.com/majorhungry/apod_site.git
```

Build the docker image
```bash
docker build -t apodsite:1.0 .
```

Move the 'docker-compose.yml' file to where you want to
run this container and store your '.env' file in the same
directory as the compose file.

```bash
docker compose up -d
```

This will run the container and the site will be
at http://localhost:8080 by default.

**Inspiration**

I'm not trying to be original with this project I know 
better projects exit and do this better but this is mine. 
If you look at NASA's dedicated page its looks very close to 
what I made. https://apod.nasa.gov

