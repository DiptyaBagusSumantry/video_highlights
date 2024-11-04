<template>
  <Navbar/>
  <div class="flex flex-col justify-center items-center min-h-screen p-10 bg-black">
    <div class="w-1/2 mb-4">
      <div class="w-full bg-gray-200 rounded-full h-4">
        <div
          class="bg-[#FF0E0E] h-4 rounded-full"
          :style="{ width: progress + '%' }"
        ></div>
      </div>
      <p class="text-center mt-2 text-white">{{ progress }}% loaded</p>
    </div>

    <div class="grid grid-cols-3 gap-x-10 gap-y-6">
      <div v-for="(video, index) in displayedVideos" :key="index" class="flex flex-col items-center">
        <div class="bg-white rounded-lg shadow-md p-4">
          <div @click="goToVideoPage(video)" class="cursor-pointer">
            <video class="w-96" controls>
              <source :src="video" type="video/mp4" />
              Your browser does not support the video tag.
            </video>
          </div>

          <div class="w-full max-w-sm mt-4">
            <div class="flex items-center">
              <span class="flex-shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-black bg-gray-100 border border-gray-300 rounded-s-lg dark:bg-gray-600 dark:text-white dark:border-gray-600">URL</span>
              <div class="relative w-full">
                <input id="website-url" type="text" aria-describedby="helper-text-explanation" 
                      class="bg-gray-50 border border-e-0 border-gray-300 text-gray-500 dark:text-gray-400 text-sm border-s-0 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                      :value="video" readonly disabled />
              </div>
              <button data-tooltip-target="tooltip-website-url" 
                      @click="copyToClipboard(video)" 
                      class="flex-shrink-0 z-10 inline-flex items-center py-3 px-4 text-sm font-medium text-center text-white bg-[#FF0E0E] rounded-e-lg hover:bg-[#FF0E0E] focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-[#FF0E0E] dark:hover:bg-[#FF0E0E] dark:focus:ring-[#FF0E0E] border border-[#FF0E0E] dark:border-[#FF0E0E] hover:border-[#FF0E0E] dark:hover:border-[#FF0E0E]" 
                      type="button">
                <span id="default-icon">
                  <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                    <path d="M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z" />
                  </svg>
                </span>
                <span id="success-icon" class="hidden inline-flex items-center">
                  <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 12">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5.917 5.724 10.5 15 1.5" />
                  </svg>
                </span>
              </button>
              <!-- <div id="tooltip-website-url" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
                <span id="default-tooltip-message">Copy link</span>
                <span id="success-tooltip-message" class="hidden">Copied!</span>
                <div class="tooltip-arrow" data-popper-arrow></div>
              </div> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { resultVideo } from '../../api/api';
import Navbar from '../../components/Navbar/navbar.vue';

export default {
  data() {
    return {
      allVideos: [],
      displayedVideos: [],
      progress: 0,
    };
  },
  components: {
    Navbar
  },
  mounted() {
    this.loadVideosDynamically();
  },
  methods: {
    async loadVideosDynamically() {
      try {
        const paramFromUrl = this.$route.params.name;

        const response = await resultVideo(paramFromUrl);
        this.allVideos = response;

        let index = 0;
        const interval = setInterval(() => {
          if (index < this.allVideos.length) {
            this.displayedVideos.push(this.allVideos[index]);
            this.progress = Math.floor(((index + 1) / this.allVideos.length) * 100);
            index++;
          } else {
            clearInterval(interval);
          }
        }, 2000);
      } catch (error) {
        console.error('Error loading videos:', error);
      }
    },
    goToVideoPage(video) {
      window.location.href = video;
      // window.open(video, '_blank');
    },
    copyToClipboard(url) {
      // navigator.clipboard.writeText(url)
      //   .then(() => {

      //     const tooltip = document.getElementById('tooltip-website-url');
      //     tooltip.classList.remove('invisible', 'opacity-0');
      //     tooltip.classList.add('opacity-100');

      //     setTimeout(() => {
      //       tooltip.classList.add('invisible', 'opacity-0');
      //       tooltip.classList.remove('opacity-100');
      //     }, 2000);
      //   })
      //   .catch(err => {
      //     console.error('Failed to copy: ', err);
      //   });
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url)
          .then(() => {
              const tooltip = document.getElementById('tooltip-website-url');
              tooltip.classList.remove('invisible', 'opacity-0');
              tooltip.classList.add('opacity-100');

              setTimeout(() => {
                  tooltip.classList.add('invisible', 'opacity-0');
                  tooltip.classList.remove('opacity-100');
              }, 2000);
          })
          .catch(err => {
              console.error('Failed to copy: ', err);
          });
      } else {
        const textarea = document.createElement("textarea");
        textarea.value = url;
        document.body.appendChild(textarea);
        textarea.select();
        try {
          document.execCommand("copy");
          const tooltip = document.getElementById('tooltip-website-url');
          tooltip.classList.remove('invisible', 'opacity-0');
          tooltip.classList.add('opacity-100');

          setTimeout(() => {
              tooltip.classList.add('invisible', 'opacity-0');
              tooltip.classList.remove('opacity-100');
          }, 2000);
        } catch (err) {
          console.error('Failed to copy using fallback: ', err);
        }
        document.body.removeChild(textarea);
      }
    }
  },
};
</script>
