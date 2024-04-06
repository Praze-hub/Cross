# Cross
## How To Run Project

This project is a Docker image and depends on another image, which you can find at [https://github.com/Praze-hub/cross_db/tree/main](https://github.com/Praze-hub/cross_db/tree/main).

### Dependencies

- Docker: You need to have Docker installed as this project is an image.
- Clone this project: [https://github.com/Praze-hub/cross_db/tree/main](https://github.com/Praze-hub/cross_db/tree/main).

### Setup

1. Create a Docker network with the name "cross":
   
   ```bash
   docker network create cross
2. Make sure there is nothing running at you local host port :5432 , as this is the port postgresql will run .
3. Run and build the postgres image that you have cloned.
   - Run the code below in the postgresql_db_docker project base/root directory.
     ```bash
      docker-compose up --build
4. Wait for the postgresql_db_docker image to finish running (you can tell when you see a prompt in the console/terminal that says database system is ready to accept connections) then continue with the steps
5. Run the code below in this projects base/root directory .
   ```bash
   docker-compose up --build
  - If you are running on windows when you navigate to the url 0.0.0.0:8000 replace 0.0.0.0 with localhost to become localhost:8000 and everything would work fine.
6. Navigate to the url provided after build and click on the docs link to find the various endpoints that you can work with.
     
     
