# Setup Vetty_Assignment in Local

# Clone the Repo:
```bash
git clone https://github.com/Shoony0/Vetty_Assignment.git
```

# Go to **Vetty_Assignment/** folder and execute command:
```bash
cd Vetty_Assignment
rm mysql_data/delete.txt
```

# Run Docker Compose command to setup django and mysql sever:
```bash
docker compose --env-file .env -f docker-compose.yml up --build --force-recreate --remove-orphans
```

# To Run Test cases and Check the Coverage Report:
### Login Docker bash shell:
```bash
docker compose --env-file .env -f docker-compose.yml exec django /bin/bash
```
### Run the tests with coverag:
```bash
coverage run manage.py test
```
### Generate a coverage report:
```bash
coverage report
```
 
### Generate an HTML report (optional):
```bash
coverage html
```
 
