import { sb } from "./storyblok";

export async function fetchStory(slug: string) {
  // `version` can be 'draft' during dev; switch to 'published' for prod
  const { data } = await sb.get(`cdn/stories/${slug}`, {
    version: process.env.NODE_ENV === "production" ? "published" : "draft",
  });
  return data.story;
}