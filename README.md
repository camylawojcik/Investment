# Investment

### Solution:
Considering the complexity to solve a higher degree polynomial equation, I decided to use a search-based method. I observed that the solution converged well after less than a 500 iterations. This approach reduces development complexity, as well as memory and processing consumption. This assumption may vary if the dataset is very large.

### Completed tasks:

- <s>Read an CSV file with the assets;</s>
- <s>Calculate the IRR(You must create your own algorithm (don't use any python mathematical function for that) we want to test your logical   thinking here;</s>
- <s>Consume a public web service that return the Selic rate of the day;</s>
- <s>Show the IRR calculated and the Selic rate in console;</s>
- Store the information of the CSV file, the calculated IRR and Selic rate in a in memory database - Feel free to use structure or           framework you like;
- <s>Create a Docker image with the application ready to use;</s>
- Create unit tests with 50% code coverage;

### How to run:
Open the terminal, navigate to the project root and run the following commands:

<code>
 docker image build -t python_investment .
 
 docker run python_investment
 </code>
