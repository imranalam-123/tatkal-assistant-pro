import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  // Render uses "/" while GitHub Pages uses "/tatkal-assistant-pro/".
  base: process.env.VITE_BASE_PATH || "/",
});
