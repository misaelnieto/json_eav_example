# The Risk application

I started this application as a hiring project and quickly became a ground test for me to try all new technologies on 2018.

Here's the challenge:

> An insurance company used to manage their risks as primary property-based (homes, farms, churches, etc.), so their data model is very rigid since assumed that all the risks are properties and have addresses. Now they want to work with other kinds of risks like Cars, Cyber Liability Coverage (protection against hacking), or Prize Insurance (if someone gets a $1 million hole-in-one prize at a golf tournament, the golf course doesn't pay it, they have an insurance policy to cover them).

So, they need to have a dynamic data model. They want to avoid to add a table everytime they come up with a with a new Risk type. 

Q: How to solve this in a civilized way?
A: This looks like a good fit for Entity Atribute Value (EAV) pattern.

Backend:
- Django
- Postgresql
- Django REST Framework

Frontend:
- Vue.JS ?

Current state:

Backend:

- [x] Django installed and configured
- [x] Core data model
- [ ] JSON API Backend

Frontend:
- [ ] Decide framework
- [ ] Basic Auth
- [ ] Single Plage App using selected framework

