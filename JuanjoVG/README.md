# Research project: Tableau

## What is data visualization?

Data Visualization is a way to represent data using visual techniques. Although they can’t substitute totally the text reports, they are a perfect complement to offers an easier, faster and more intuitive way to show some kinds of data. In the last years, with the increment of data sciences, the interest on this techniques has grown a lot. In another hand, sometimes the graphical data visualization has become the only feasible way to show data with more than two dimensions and that combines different kinds of variables. The merge of this concepts has made the data visualization an essential for most of the current contexts.

This growth and democratization of the data usage have shown a very demanded need to cover, the data visualization tools. Data visualization tools can be used in a variety of ways. Users can create their own plots, views, and dashboards without very technical and specific knowledge. The data visualization tools come with connectors to different data sources like to databases, big data platforms, and cloud resources. And, with these collected resources, the user can select the best way of presenting the data between a huge variety of options.

## What is Tableau?
- Description:

  Tableau is a powerful business intelligence and data visualization tool that has a very intuitive user interface. 
  You don’t need any coding knowledge to work with Tableau. It is very useful in drilling-down data, creating insightful reports and garner actionable business insights.

- Advantages
  + No need technical knowledge
  + Hughe community support
  + Easy sharing your work
  + Easy to visualize your data
  + Import data from  different data sources

As at first sight, it doesn’t seem too important to have a tool that does not need technical knowledge of data sources, data aggregations and how to manage the data. But when it comes to business and real enterprises you need tools that allow you to visualize your data easily without needing that extra knowledge that as a non-technical person you don’t have and you don0t really need for any other thing.  

Also having community support is really important when it comes to a tool as you for sure will find problems and the invested time in searching a solution mostly depends on how much information is responsible about this topic.

And finally doing easy the process of sharing your work is always a plus as you will do visualizations for presentations, reports or similar so sharing them easily is a must for one of this tools.

Tableau also allows us to import data from multiple data sources which can be useful that our data can come from really different sources.

## Tableau Products

The Tableau platform is split into three components that can be combined between them in order to get a full analysis data experience. These components are Tableau Desktop, Tableau for organizations, and Tableau Prep.
  * **Tableau Desktop:** Tableau Desktop is the core tool of Tableau platform. It can be installed on any computer that meets the technical requirements and it allows us to use the functionalities explained in the previous sections. Individually, it only allows an individual use and it makes possible the offline work since it provides a way to download the data sources that we will analyze and visualize.

  * **Tableau for Organizations:** Tableau offers two ways to integrate this tool in a collaborative environment as an organization or group use. This kind of tools allows us to share dashboards, views, data sources and more between a group (not necessarily closed) of users.

    * **Tableau Server:** This is the most customizable option for a collaborative environment. Tableau Server can be deployed on a local or cloud server in order to connect the work of multiple users. It is a good option to control the governance, security, access and physical location because the service provider is managed directly by the organization technical team. On another hand, this solution force to the organization to invest resources in the infrastructure, deploy and management of the platform.

    * **Tableau Online:** Tableau Online is another option to use a collaborative environment without worrying about any platform management process. It is a cloud version managed by the Tableau team and offers an opportunity for organizations without a specific technical team. It is less customizable but is a more than enough solution for most cases.

  * **Tableau Prep:** Tableau Prep is a tool that offers extra processing functionalities to achieve the most complex tasks with our data. It allows us to clean, combine and prepare our data in order to maximize the usefulness of the created visualizations. It is thought to cover the preparation needs of the data before to be visualized.

## Pricing

Tableau considers three kinds of users for its platform: Creator, Explorer, and Viewer.

  * **Creator:** The Creator users are the users with more possibilities and they can do everything with the platform. This profile of users is responsible for management and administration of the associated Tableau instance and analyze the raw data. Profile thought for the data analyst with a technical profile.
  
  * **Explorer:** The Explorer users have the second rank of the user kinds. They are allowed to create and modify the data visualizations inside the platform. Basically, they can do the same than the Creators but add and prepare new data sources and manage the Tableau instance. Profile thought for corporative users that use and manage the data but without deep knowledge of data analysis.
  
  * **Viewer:** The viewer users are the consumers of the platform. They can visualize and use the previously created visualization but they can’t create nor modify them. Profile thought for CEO and final customers.

The Tableau license system is based on individual license depending on the user profile. The licenses are bought yearly, but the prices are shown monthly. So, in function of if the system uses Tableau Server or Tableau Online, the different prices are the following:

|            | Tableau Server | Tableau Online |
| ---------- |:--------------:| --------------:|
| *Creator*  | 70$/month      | 70$/month      |
| *Explorer* | 35$/month      | 42$/month      |
| *Viewer*   | 12$/month      | 15$/month      |

Last, Tableau has a free version named Tableau Public. Tableau Public allows to the users to use the Tableau Desktop Public Edition, which is a limited version of Tableau Desktop. Also, it offers 10GB of online storage and the possibility of share and includes the created visualization with Social Networks, web pages or blogs.

## Example
For the example, we used Tableau Public and a JSON that contained data from a player. We Decided to show how easy is to import, select what you want and plot it in a user-friendly way.

We use Tableau Public as with this it will be easily reproducible by anyone and without having to waste the free trial 15 days of a premium version just for exploring how it works. For this example we will need two resources:

Tableau public

JSON with the data ![Data](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/Data/HEX%20Taliuzz.json)

The JSON contains stats of a player with different champions. We used this dataset as is really simple and we used it originally to explore tableau.

First what we will do is import the json and it will prompt a dialog to select the levels of the json that we want to import in this way we can select the levels of the json that we want just by checking them. In our example we will check all of them as follows:

![Screenshot Demo](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/demo00.png)

Now we will see that our data is imported and shown in table mode.
Now we will see how to plot a really basic plot. For this, we will create a new Sheet by clicking in the low left corner. This we will prompt us a new blank sheet.

![Screenshot Demo](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/demo01.png)


In this windows we have the following layout:
  - In the Left:
    - The data divided into dimensions and metrics.
    - Serie of cards to modify the plots that are in the sheet
  - Center:
    - On the top, we have a contextual menu
    - The rest is the current workspace where the plots will show
  - On the Right:
    - Plots available

To do our first plot we will select from the dimension: Champion Name and from the metrics wins. Then we will select a simple bar plot.

![Screenshot Demo](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/demo02.png)


Now we will click the treemap and we will obtain the following:

![Screenshot Demo](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/demo03.png)


As we see the color is practically unreadable and has no sense as it means exactly the same as the size. So we will go to marks and we will remove the color representation from the sum of games and we will drag to this section the champion names again and will assign the color to it so we will obtain the next:

![Screenshot Demo](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/demo04.png)

So now we have changed the colors meaning and added a label wich show us the size value and we have obtained the following plot:

![Screenshot Demo](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/demo05.png)

As we can see now we have a more readable plot in a very easy way.

Now we will do a bar plot comparing the kills and deaths to see another way of doing this. First, we will create a new sheet and we will drag the champions name to the column field and the deaths and kills to the rows field. And we will obtain the following plot:

![Screenshot Demo](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/demo06.png)

Now we want to merge the two plots so we simply drag one plot into the other. Then as we want to differentiate the two metrics with colors we will drag the “Metrics Names” into the marks and will select this as color. Now we will click color and select the correct colors.

![Screenshot Demo](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/demo07.png)

Now we will add a filter to only show this stats for five champions by dragging the champion name into the filter section and selecting the 5 we want to visualize.

Finally, we will create a dashboard to get all our plots together. For this, we will do left click and select new Dashboard. And there we will drag the two sheets that we previously created.

![Screenshot Demo](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/demo08.png)

And now if we save out the project it would automatically upload to tableau public server and you will have a link to your project that allows you to share your work. 

If you followed all the steps you should end up with something like this: https://public.tableau.com/profile/sergi.tortosa#!/vizhome/Ejemplo_65/Dashboard1

## Alternatives
* **Qlik:** Qlik Sense is a business intelligence (BI) and visual analytics platform that supports a range of use cases, including centrally deployed guided analytics apps and dashboards, custom and embedded analytics, and self-service visualization, all within a scalable, governed framework. The solution comes in three different editions - Qlik Sense Desktop, Enterprise and Cloud.

* **Microsoft Power BI Software:** Microsoft Power BI is a web-based business analytics and data visualization platform that is suitable for businesses of all sizes. It monitors important organizational data and also from all apps used by organizations. Microsoft Power BI provides tools to quickly analyze, transform and visualize data, and also share reports.

* **TIBCO Spotfire Software:** TIBCO Spotfire provides executive dashboards, data analytics, data visualization and KPI push to mobile devices. It complements existing business intelligence and reporting tools, while midsize organizations can use dashboards and analytics tools. It keeps the total cost of ownership low by allowing users to build once and publish to thousands of users over internet or intranet, as a PDF or as MS PowerPoint reports. It can be deployed either in cloud or on-premise.

* **Sisense:** Sisense is an agile business intelligence (BI) solution that provides advanced tools to manage and support business data with analytics, visuals and reporting. The solution allows businesses to analyze big and disparate datasets and generate relevant business trends for them. Sisense can be deployed on-premises or hosted in the cloud as a SaaS application.

We also want to show you a comparative between diferent BI tools and their classification

![Comparative](https://github.com/JuanjoVG/CLOUD-COMPUTING-CLASS-2018/blob/master/Research-topic/ImagesReport/comp.png)

As we can see we have four sub-quadrants:

*Leaders:* Leaders are all-around strong products. They offer a wide range of functionality to a wide range of customers. These products are considered highly valuable by customers.
 
*Masters:* Masters may focus more heavily on certain key features or market segments than Leaders do. If you need a more specialized set of functionality without bells and whistles, then a product in the Masters quadrant might be right for you.
 
*Pacesetters:* Pacesetters may offer a strong set of features, but are not rated as highly on value. For example, a Pacesetter might offer greater functionality, but cost more.
 
*Contenders:* Contenders may focus on a more specialized set of capabilities that are priced at a higher point. This makes them ideal for companies willing to pay more for specific features that meet their unique needs.

Taking this into accound from the presented alternatives based on the information an users opinions we will give a try to MS Power Bi can be a good tool to replace tableau (but is not popular as tableau and has not the same support). And also Qlik as has a free online tool that can be really interesant to explore. 

## Conclusions

Tableau is easy to use without any previous knowledge as they said.

Doing data aggregations is not that easy and not easy to revert so you might end up re-importing your data.

Tableau Desktop Is really complete (in data sources and options) and it can be sync with the cloud.

All the products keep the same interface which helps you to start with public and if you like it then jump to a premium version.

Tableau public is quite more limited than they actually say as there is a limit of the data that can be imported, formats and share options.

