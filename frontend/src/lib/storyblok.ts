import StoryblokClient from "storyblok-js-client";

const token = process.env.NEXT_PUBLIC_STORYBLOK_PREVIEW_TOKEN!;

if (!token) {
  throw new Error("Missing storyblok token")

}

export const sb = new StoryblokClient({


  accessToken: token,
  cache: {clear: "auto", type: "memory"}
})

