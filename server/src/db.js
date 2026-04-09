import { MongoClient } from "mongodb";

/** Mongo client singleton for the datalog API. */
let client;

/**
 * Returns a connected MongoClient, reusing the existing connection when possible.
 * @param {string} uri
 * @returns {Promise<MongoClient>}
 */
export async function getClient(uri) {
  if (client) return client;
  client = new MongoClient(uri);
  await client.connect();
  return client;
}

/**
 * @param {MongoClient} mongoClient
 * @param {string} dbName
 */
export function getDb(mongoClient, dbName) {
  return mongoClient.db(dbName);
}
