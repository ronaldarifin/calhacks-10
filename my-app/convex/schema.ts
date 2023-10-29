import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
    resume: defineTable({
        username: v.string(),
        employer: v.string(), 
        position: v.string(),
        location: v.optional(v.string()),
        summary: v.string(),
        website: v.optional(v.string()),
        startDate: v.optional(v.string()),
        endDate: v.optional(v.string()),
        highlights: v.optional(v.array(v.string())), 
        embedding: v.array(v.float64()),
    }).vectorIndex("by_embedding", {
        vectorField: "embedding",
        dimensions: 512,
        filterFields: ["username"],
    }),
    cv_table: defineTable({
        username: v.string(),
        resume_json: v.any(),
    })
});