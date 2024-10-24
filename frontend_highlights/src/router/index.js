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
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router