import { Browser, launch } from "puppeteer";

export class BrowserService {
  private static browser: Browser | null = null;

  public static getBrowser() {
    if (this.browser) {
      return this.browser;
    }
    throw "Please run setup first";
  }

  public static async setup() {
    this.browser = await launch({
      executablePath:"/usr/bin/chromium-browser",
      args: [
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-setuid-sandbox"
      ]
    });

    this.browser.on("disconnected",async ()=> await this.setup());

    console.log(`Started Puppeteer with pid ${this.browser.process().pid}`);
  }

  public static async close() {
    if (this.browser) {
      await this.browser.close();
    }
  }
}
