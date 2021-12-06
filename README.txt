REST API:
Pros:
-Easy to use and understand
-Flexible with the information you can receive and use from body,
path and query parameters
-You always work with json and the IDE is smart to transfrom any dictionary into a json
Cons:
-It doesn't have much security however we are not building 
an actual application so we didn't really implement any. 
-Its stateless and no information is stored on our side and its 
entirely up to the client to give us the information

Good practices of REST:
Its best to work with jsons
Its better to keep the path short and simple without using verbs and plurals
Its best to give informative error messages

I made all functions idempotentical except the delete function in the Address service
since we don't care about its response because we use it through the User service
