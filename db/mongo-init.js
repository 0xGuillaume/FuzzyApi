db.getSiblingDB('fuzzy');

db.createUser(
	{
		user: "api",
		pwd: "root",
		roles: [
			{
				role: "readWrite",
				db: "fuzzy"
			}
		]
	}
);


db.createCollection("foo");

db.foo.insert([
	{"title": 1, "description": "lorem ipsum"},
	{"title": 2, "description": "lorem ipsum"},
	{"title": 3, "description": "lorem ipsum"},
	{"title": 4, "description": "lorem ipsum"}
]);
