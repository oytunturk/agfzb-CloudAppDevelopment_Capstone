#Clone your git repo
git clone git@github.com:oytunturk/agfzb-CloudAppDevelopment_Capstone.git

#Run backend (cloudant db, otherwise the front-end won't work)
sudo npm install -g couchimport
export IAM_API_KEY="ykjw4Onb12_yVddNhLWgIEhSd36H9BsiK9aozQxyfpuI"
export COUCH_URL="https://791a549d-a6d5-4c1d-b7c0-599bbb16c1ba-bluemix.cloudantnosqldb.appdomain.cloud"
cd cloudant/data
#Export dealership and review data to cloud database (otherwise the cloud database3 won't have any info that we can use for testing the front-end)
cat ./dealerships.json | couchimport --type "json" --jsonpath "dealerships.*" --database dealerships
cat ./reviews.json | couchimport --type "json" --jsonpath "reviews.*" --database reviews

#Make sure functions/sample/reviews.py has the correct cloudant credentials
#cloudant_username = '791a549d-a6d5-4c1d-b7c0-599bbb16c1ba-bluemix'
#cloudant_api_key = 'ykjw4Onb12_yVddNhLWgIEhSd36H9BsiK9aozQxyfpuI'
#cloudant_url = 'https://791a549d-a6d5-4c1d-b7c0-599bbb16c1ba-bluemix.cloudantnosqldb.appdomain.cloud'

#Follow the instructions here to create actions in your cloudant
#https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0321EN-SkillsNetwork/labs/module_3_backend_services/4-instructional-labs-API-Changes.md.html
#Actually, these didn't work and I had to make code changes in the cloned git repo as suggested by the discussion forums on Coursera




#Run front-end
cd server
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

