# alexa-python-hello-world
A starting point for a simple Alexa skill backed by a python lambda function.

NOTE: Requires AWS Account (shouldn't break past the free tier) with cli configuration


### Getting Started
First things first, fork this repo so you can customize it.

The only required change to the code before you get up and running is to change the `Source` `Location` in `/development-resources.yaml` to point to your new fork.

Now we can really have some fun!

1. Get yourself a virtual environment for this project.
2. `pip install -r requirements-dev.txt`
3. `aws cloudformation create-stack --stack-name PythonAlexaDevResources --template-body file://development-resources.yaml --capabilities CAPABILITY_IAM`
4. In the AWS console, run the newly created CodeBuild job (should have "LambdaPackageJob" in the name)
5. Copy the ARN for the newly created Lambda function (should have "AlexaLambdaHandler" in the name)
6. Log in to the [ASK portal](https://developer.amazon.com/alexa/console/ask).
7. Create a new skill, naming it and choosing an invocation phrase as you please.
8. Under "Endpoint", choose Lambda and paste the Lambda Function ARN from step 5 into the "Default Region" and save.
9. Copy `/interaction_model.json` into the "Interaction Model" "JSON Editor" and save.
10. Save and Build the model for the skill.
11. Test it out. You can search for github repositories by default.
12. Make it your own and do something awesome!

When you make a change to your fork's master branch, you can simply re-run the CodeBuild job to update the Lambda stack. The Alexa skill will automatically use the updated lambda function.


#### TODOs
* Tests!!!
* CI/CD with full CodeBuild/CodePipeline suite
* More or different functionality
