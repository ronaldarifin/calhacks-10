import { query, mutation, action, internalQuery } from "./_generated/server";
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

export const createTask = mutation({
    args: { user_id: v.string(), text: v.string() },
    handler: async ({ db } , args) => {
        return await db
            .insert("resume", { text: args.text });
    },
});

//CRUD . create, read, update, delete
// export const get_similar_resumes = action({
//   args: {
//     description_embedding: v.array(512),
//     user: v.string()
//   },
//   handler: async (ctx, args) => {
//     const results = await ctx.vectorSearch("resume", "embedding", {
//       vector: args.description_embedding,
//       limit: 5,
//       filter: (q) => q.eq("user", args.user),
//       // username, find out what the field name is.
//     });
//     const experiences = await ctx.runQuery(
//         internal.resume.fetchResults,
//         { ids: results.map((result) => result._id)}
//       );
//       return foods;
//     },
// });

// export const fetchResults = internalQuery({
//     args: { ids: v.array(v.id("resume")) },
//     handler: async (ctx, args) => {
//       const results = [];
//       for (const id of args.ids) {
//         const doc = await ctx.db.get(id);
//         if (doc === null) {
//           continue;
//         }
//         results.push(doc);
//       }
//       return results;
//     },
// });