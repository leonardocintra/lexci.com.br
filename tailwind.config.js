/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundVideo: {
        "hero-section": "url('/video/video.mp4')",
      },
    },
    container: {
      center: true,
    },
    extend: {},
  },
  plugins: [],
};
