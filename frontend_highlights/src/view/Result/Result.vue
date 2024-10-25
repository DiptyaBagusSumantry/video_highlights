<template>
  <div class="flex flex-col justify-center items-center min-h-screen p-10">
    <div class="w-1/2 mb-4">
      <div class="w-full bg-gray-200 rounded-full h-4">
        <div
          class="bg-blue-600 h-4 rounded-full"
          :style="{ width: progress + '%' }"
        ></div>
      </div>
      <p class="text-center mt-2">{{ progress }}% loaded</p>
    </div>

    <div class="grid grid-cols-3 gap-x-10 gap-y-6">
      <div v-for="(video, index) in displayedVideos" :key="index" class="flex justify-center">
        <video class="w-96" controls>
          <source :src="video" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
    </div>
  </div>
</template>

<script>
import { resultVideo } from '../../api/api';

export default {
  data() {
    return {
      allVideos: [],
      displayedVideos: [],
      progress: 0,
    };
  },
  mounted() {
    this.loadVideosDynamically();
  },
  methods: {
    async loadVideosDynamically() {
      try {
        const paramFromUrl = this.$route.params.name;

        const response = await resultVideo(paramFromUrl);
        // console.log(response)
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
  },
};

// export default {
//   data() {
//     return {
//       allVideos: [
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//         { src: '../../../public/video/video.mp4' },
//       ],
//       displayedVideos: [],
//       progress: 0,
//     };
//   },
//   mounted() {
//     this.loadVideosDynamically();
//   },
//   methods: {
//     loadVideosDynamically() {
//       let index = 0;
//       const interval = setInterval(() => {
//         if (index < this.allVideos.length) {
//           this.displayedVideos.push(this.allVideos[index]);
//           this.progress = Math.floor(((index + 1) / this.allVideos.length) * 100);
//           index++;
//         } else {
//           clearInterval(interval);
//         }
//       }, 2000);
//     },
//   },
// };
</script>

<!-- <script>
export default {
  data() {
    return {
      videos: [
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' },
        { src: '../../../public/video/video.mp4' }
      ]
    };
  }
};
</script>

<template>
    <div class="flex justify-center items-center min-h-screen p-10">
    <div class="grid grid-cols-3 gap-x-10 gap-y-6">
        <div v-for="(video, index) in videos" :key="index" class="flex justify-center">
        <video class="w-96" controls>
            <source :src="video.src" type="video/mp4" />
            Your browser does not support the video tag.
        </video>
        </div>
    </div>
    </div>
</template> -->