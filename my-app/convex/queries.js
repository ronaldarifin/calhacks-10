import { query } from "./_generated/server";
import { v } from "convex/values";

export const get_resume = query({
    args: { user_id: v.string() },
    handler: async({db}, args) => {
        return await db
            .query("resume")
            .filter(q => q.eq(q.field("user_id"), args.user_id ))
            .collect();
    }
});