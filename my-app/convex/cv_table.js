import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const get_cv = query({
  args: { username: v.string() },
  handler: async({ db } , args) => {
      return await db
          .query("cv_table")
          .filter(q => q.eq(q.field("username"), args.username ))
          .collect();
  }
});

// export const insert_cv = mutation({
//   args: {text: v.string() },
//   handler: async ({ db } , args) => {
//       const row = JSON.parse(args.text);
//       return await db
//           .insert("cv_table", { text: row });
//   },
// });

export const insert_cv = mutation({
  args: { resume_json: v.any(), username: v.string() }, // Directly define the args
  handler: async ({ db }, args) => {
      return await db
          .insert("cv_table", { 
            resume_json: args.resume_json, 
            username: args.username
          });
  },
});
