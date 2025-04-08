// Connect to the octofit_db database
const { MongoClient } = require("mongodb");
const uri = "mongodb://localhost:27017";
const client = new MongoClient(uri);

async function initDatabase() {
	try {
		await client.connect();
		const db = client.db("octofit_db");
		console.log("Connected to the octofit_db database");

		// Create the users collection with a unique index on the email field
		await db.collection("users").createIndex({ "email": 1 }, { unique: true });

		// Create the teams collection
		await db.createCollection("teams");

		// Create the activity collection
		await db.createCollection("activity");

		// Create the leaderboard collection
		await db.createCollection("leaderboard");

		// Create the workouts collection
		await db.createCollection("workouts");

		console.log("Collections created successfully");
	} catch (error) {
		console.error("Error initializing database:", error);
	} finally {
		await client.close();
	}
}

initDatabase();

// Create the users collection with a unique index on the email field
db.users.createIndex({ "email": 1 }, { unique: true });

// Create the teams collection
db.createCollection("teams");

// Create the activity collection
db.createCollection("activity");

// Create the leaderboard collection
db.createCollection("leaderboard");

// Create the workouts collection
db.createCollection("workouts");

// Verify the collections in the database
const collections = await db.listCollections().toArray();
console.log("Collections in the database:", collections.map(c => c.name));
