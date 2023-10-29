import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
    resume: defineTable({
        username: v.string(),
        employer: v.string(), 
        position: v.string(),
        location: v.string(),
        summary: v.string(),
        website: v.string(),
        startDate: v.string(), 
        highlights: v.array(v.string()), 
        embedding: v.array(v.float64()),
    }).vectorIndex("by_embedding", {
        vectorField: "embedding",
        dimensions: 512,
        filterFields: ["username"],
    }),
});