import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'upload',
        component: () => import('../view/Upload/Upload.vue')
    },
    {
        path: '/result/:name',
        name: 'result',
        component: () => import('../view/Result/Result.vue')
    },
    {
        path: '/result',
        name: 'List Match',
        component: () => import('../view/ListMatch/ListMatch.vue')
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router