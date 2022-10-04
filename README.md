# monitoring-crypto
An example flask rest API server, for SE Fall 2022.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

We will write a API-driven adventure game where characters explore a world, meet threats, find treasure, etc.

## Requirements

### Game endpoints:
* List all available games
* Get a description of a game


## User endspoints:
* Signup
* Signin
* list all available users
* get a description of a user

### Character type endpoints
* list all available character types
* get a description of a character types


### In-game actions
* List all active characters
* Describe a locale
* Allow character to move
* Allow character to act
* Allow character to talk to other characters in locale


## Design
Each of the main requirements will correspond to an API endpoint.

We will need to carefully consider a security system, and modify the design of these endpoints to reflect our security policy