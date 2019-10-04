# Boston University - ECE601 F19 Mini project 1
Group 12:
This project uses twitter api and google google natural language api. We are getting tweets from users about their feelings and opitions over a new product or new food menu added to fast food restaurants. In our example, we are going to use the launch of the "Impossible Burger"(https://impossiblefoods.com/food/) in the Burguer Kind menu.

# Architecture
![image](https://github.com/yanjh95/F19_EC601_t12_mini1/blob/master/architecture.jpg)
# User stories
Me as a major supermarket store, would like to know what people have been cooking at home for different times and locations

Me as online food supplier, would like to know what food is trending in order to more effectively design adds

Me as a reporter or researcher, would like to get access to food data that people have been eating for studies

Me as a food business, would like to have feedback on different dishes, so I can re-adjust the menu.

Me as a restaurant company, would like to know data from other restaurants, so I can learn from their strengths

Me as Government entities, would like to know that produce needs readjustment

Me as FAO , would like to know food needs around the globe.
# tweetgrab.py
In the **tweetgrab.py** file, we use *api.search()* to get the feeds we wanted. For example. the "#fastfood". Then, we could acquire 60 feeds from the twitter search, then saved the feeds in **tweetex.json** file. 
