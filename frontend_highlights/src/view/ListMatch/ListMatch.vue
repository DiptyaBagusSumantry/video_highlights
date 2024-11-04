<template>
    <Navbar/>
    <div class="p-4 bg-black h-screen">
        <h1 class="flex p-8 text-2xl font-bold mb-4 text-white justify-center">List Pertandingan</h1>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
            <div 
                v-for="(match, index) in listMatch" 
                :key="index" 
                class="card bg-white shadow-md rounded-md p-4 cursor-pointer hover:shadow-lg transition-shadow duration-200 border-2 border-red-600 border-opacity-0 hover:border-opacity-100" 
                @click="redirectToResult(match)"
            >
                <h2 class="text-lg font-semibold">Pertandingan {{ index + 1 }}</h2>
                <p class="text-gray-600">Waktu: {{ formatTimestamp(match) }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { listMatch } from '../../api/api';
import Navbar from '../../components/Navbar/navbar.vue';
export default {
    data() {
        return {
            listMatch: []
        }
    },
    components: {
        Navbar
    },
    mounted() {
        this.fetchListMatch();
    },
    methods: {
        async fetchListMatch() {
            try {
                const response = await listMatch();
                this.listMatch = response; 
            } catch (error) {
                console.error("Error fetching list match:", error);
            }
        },
        formatTimestamp(timestamp) {
            const date = new Date(Number(timestamp));
            return date.toLocaleString('id-ID', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
            });
        },
        redirectToResult(timestamp) {
            this.$router.push(`/result/${timestamp}`);
        }
    }
}
</script>

<style scoped>
.card {
    transition: transform 0.2s;
}
.card:hover {
    transform: scale(1.05);
}
</style>
