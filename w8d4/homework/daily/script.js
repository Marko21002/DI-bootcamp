class Video {
    constructor(title, uploader, time) {
      this.title = title;
      this.uploader = uploader;
      this.time = time;
    }
    watch() {
        return `${this.uploader} watched all ${this.time} seconds of ${this.title}!`;
      }
  }

  const video1 = new Video("Bones-HDMI","Bones",180);
  console.log(video1.watch())
  const video2 = new Video("","Bones",180);