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

export const insert_cv = mutation({
  args: { text: v.string() },
  handler: async ({ db } , args) => {
      return await db
          .insert("cv_table", { text: args.text });
  },
});