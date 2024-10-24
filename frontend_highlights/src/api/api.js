import axios from "axios";
// const token = localStorage.getItem("token")

const axiosInstance = axios.create({
  baseURL: "http://localhost:5000/",
  headers: {
    "Content-Type": "application/json",
    //  Authorization: `Bearer ${token}`
  },
});


export const uploadVideo = async (video, timestamp) => {
  const formData = new FormData();
  formData.append('video', video);
  formData.append('timestamp', timestamp);

  try {
    const response = await axiosInstance.post('process-video', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    throw new Error('Error uploading video: ' + error.message);
  }
};

export const resultVideo = async (param) => {
  try {
    console.log(`get-video/${param}`)
    const response = await axiosInstance.get(`get-video/${param}`);
    return response.data;
  } catch (error) {
    throw new Error('Error uploading video: ' + error.message);
  }
};
