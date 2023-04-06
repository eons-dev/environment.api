# environment.api
An easy way to create environments for Apie.

## When to use
Use the environment.api any time you want to provide users with different behavior at different urls. This is not a means of testing a git branch of an api you have in your VCS.

To illustrate, consider when you might want to expose `dev.your.domain` to your users as a means of testing their application before they use `your.domain`. You may want to provide additional details, like the runtime or cost of a users request, only when that users hits the dev Apie server. When they hit your prod server, you want to be as optimized as possible and return only as much information as is necessary.

## How to use
Simply specify `environment`, and the environment.api will append the given environment to subsequent calls.

Then environment.api is best used as a preprocessor for a dedicated Apie deployment (e.g. add `preprocessor: environment` and `environment: ...` to your Apie config).
However, you can also use it in a regular Apie call (e.g. `curl https://eons.sh/environment/whatever...?environment=dev`)

For example, if our `environment` is `dev` and we call `whatever`, our call will be routed to `whatever_dev`.

Environments can be anything you'd like. However, we recommend:
* `dev` - for development; volatile & verbose.
* `pre` - for pre-production testing; somewhat volatile & quiet.
* ` ` (i.e. nothing) - for production; stable & quiet.