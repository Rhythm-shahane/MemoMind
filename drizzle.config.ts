import type { Config } from "drizzle-kit";
import dotenv from "dotenv";

// Load environment variables from.env file located in the project root
dotenv.config({ path: ".env" });

export default {
    dialect:"postgresql",
  driver: "pg", // Specifies the database driver
  schema: "./lib/db/schema.ts", // Path to your database schema file
  dbCredentials: {
    url: "process.env.DATABASE_URL!", // Ensure DATABASE_URL is defined in your.env file
  },
} as Config; // Explicitly cast to satisfy the Config interface
