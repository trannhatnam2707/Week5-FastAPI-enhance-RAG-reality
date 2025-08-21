import PostDetail from "./Page/PostDetail";
import PostList from "./Page/PostList";

export const route = [
    { 
        path: "/",
        page: PostList
    },
    {
        path: "/PostDetail",
        page: PostDetail
    }
]