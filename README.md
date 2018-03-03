# Project 6: Brevet time calculator service

A continuous project based on project 5, used MongoDB database and API.


## Functionality 

   "http://localhost:5001/listAll" should return all open and close times in the database
   
   "http://localhost:5001/listOpenOnly" should return open times only
   
   "http://localhost:5001/listCloseOnly" should return close times only

   "http://localhost:5001/listAll/csv" should return all open and close times in CSV format
   
   "http://localhost:5001/listOpenOnly/csv" should return open times only in CSV format
   
   "http://localhost:5001/listCloseOnly/csv" should return close times only in CSV format

   "http://localhost:5001/listAll/json" should return all open and close times in JSON format
   
   "http://localhost:5001/listOpenOnly/json" should return open times only in JSON format
   
   "http://localhost:5001/listCloseOnly/json" should return close times only in JSON format

   "http://localhost:5001/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 
   
   "http://localhost:5001/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format

## Build
docker-compose build

docker-compose up
