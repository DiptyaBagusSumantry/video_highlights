<template>
    <nav class="flex w-full justify-between items-center shadow-md backdrop-saturate-200 backdrop-blur-2xl bg-opacity-80 border border-white/80 text-white sticky top-0 z-10 h-max max-w-full rounded-none px-4 py-2 lg:px-8 lg:py-4 bg-[#100F0F]/100 border-none">
    <div class="flex items-center justify-between text-blue-gray-900">
      <a href="https://hailightz.com/demo" class="block antialiased font-sans mr-4 cursor-pointer py-1.5 font-medium text-4xl text-white">
        H<span style="color:#FF0E0E">AI</span>LIGHTZ
      </a>
    </div>
    <ul class="hidden lg:flex space-x-4 text-white">
      <li><a href="https://hailightz.com/demo" class="hover:text-gray-400">Home</a></li>
      <li><a href="/" class="hover:text-gray-400">Upload</a></li>
      <li><a href="/result" class="hover:text-gray-400">Result</a></li>
      <li>
        <a class="align-middle select-none font-sans font-bold text-center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-2 px-4 border hover:opacity-75 focus:ring focus:ring-gray-300 active:opacity-[0.85] text-white border-[#FF0E0E] normal-case rounded"
          type="button"
          style="position: relative; overflow: hidden;"
        >
          Sign Up 
        </a>
      </li>
      <li>
        <a class="align-middle select-none font-sans font-bold text-center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-2 px-4 text-white shadow-md shadow-gray-900/10 hover:shadow-lg hover:shadow-gray-900/20 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none bg-[#FF0E0E] normal-case rounded"
          type="button"
          style="position: relative; overflow: hidden;"
        >
          Sign In
        </a>
      </li>
    </ul>
  </nav>
</template>