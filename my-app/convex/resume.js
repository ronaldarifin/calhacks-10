import { query, mutation, action, internalQuery } from "./_generated/server";
import { internal } from "./_generated/api";
import { v } from "convex/values";

export const get_resume = query({
    args: { username: v.string() },
    handler: async({ db } , args) => {
        return await db
            .query("resume")
            .filter(q => q.eq(q.field("username"), args.username ))
            .collect();
    }
});

export const insert_experience = mutation({
    args: { text: v.string() },
    handler: async ({ db } , args) => {
        return await db
            .insert("resume", { text: args.text });
    },
});

//CRUD . create, read, update, delete
export const get_similar_resumes = action({
  args: {
    description_embedding: v.string(),
    username: v.string()
  },
  handler: async (ctx, args) => {
    // convert into json array
    const embedding_arr = JSON.parse(args.description_embedding);
    const results = await ctx.vectorSearch("resume", "by_embedding", {
      vector: embedding_arr,
      limit: 5,
      filter: (q) => q.eq("username", args.username),
    });
    const experiences = await ctx.runQuery(
      internal.resume.fetchResults,
      { ids: results.map((result) => result._id), scores: results.map((result) => result._score)}
    );
    return experiences;
    },
});

export const fetchResults = internalQuery({
    args: { ids: v.array(v.id("resume")), scores: v.array(v.float64()) },
    handler: async (ctx, args) => {
      const results = [];
      for (const id of args.ids) {
        const doc = await ctx.db.get(id);
        if (doc === null) {
          continue;
        }
        results.push(doc);
      }
      return results;
    },
});