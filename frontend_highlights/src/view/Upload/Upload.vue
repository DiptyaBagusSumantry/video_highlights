<template>
  <div class="flex justify-center items-center h-screen">
    <div class="flex flex-col items-center justify-center w-1/4">
      <!-- <h1 class="text-lg font-semibold mb-4">Upload Your Video</h1> -->
      <label
        for="dropzone-file"
        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
      >
        <div class="flex flex-col items-center justify-center pt-5 pb-6">
          <svg
            v-if="!selectedVideo"
            class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 20 16"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
            />
          </svg>
          <p v-if="!selectedVideo" class="mb-2 text-sm text-gray-500 dark:text-gray-400">
            <span class="font-semibold">Click to upload</span> or drag and drop
          </p>
          <p v-if="!selectedVideo" class="text-xs text-gray-500 dark:text-gray-400">MP4</p>

          <p v-if="selectedVideo" class="mb-2 text-sm text-green-500">
            {{ selectedVideo.name }}
          </p>

          <video
            v-if="selectedVideoPreview"
            class="w-48 mt-4"
            controls
            :src="selectedVideoPreview"
          >
            Your browser does not support the video tag.
          </video>
        </div>
        <input
          id="dropzone-file"
          type="file"
          class="hidden"
          @change="handleVideoUpload"
          accept="video/mp4"
        />
      </label>
      <button
        @click="submitVideo"
        class="mt-4 bg-blue-500 text-white p-2 rounded-lg"
        :disabled="loading"
      >
        Submit
      </button>

      <div v-if="loading" class="mt-4">
        <svg class="animate-spin h-5 w-5 text-blue-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 108 8V12H4z"></path>
        </svg>
        <p class="mt-2 text-sm text-gray-500">Processing your video...</p>
      </div>
    </div>
  </div>
</template>

<script>
import { uploadVideo } from '../../api/api';

export default {
  data() {
    return {
      selectedVideo: null,
      selectedVideoPreview: null,
      loading: false,
    };
  },
  methods: {
    handleVideoUpload(event) {
      const file = event.target.files[0];
      if (file && file.type === 'video/mp4') {
        this.selectedVideo = file;
        this.selectedVideoPreview = URL.createObjectURL(file);
      } else {
        alert('Please upload a valid MP4 video.');
      }
    },
    async submitVideo() {
      if (!this.selectedVideo) {
        alert('No video selected.');
        return;
      }

      this.loading = true;
      try {
        const timestamp = Date.now();
          setTimeout(() => {
        this.$router.push(`/result/${timestamp}`);
        }, 150000);

        const result = await uploadVideo(this.selectedVideo, timestamp);
        
        this.selectedVideo = null;
        this.selectedVideoPreview = null;
      } catch (error) {
        console.error(error.message);
        alert('Failed to upload video.');
      } finally {
        this.loading = false; 
      }
    },
  },
};
</script>

<style scoped>
.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
