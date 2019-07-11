import express from "express";
import puppeteer from "puppeteer";

interface GetPageRequest {
  url: string;
}

async function main() {
  const browser = await puppeteer.launch({
    args: ["--no-sandbox"]
  });
  const app = express();
  app.use(express.json());
  app.get("/", (req, res) => res.send("Hello world"));
  app.post("/get-page", async (req, res) => {
    const request = req.body as GetPageRequest;
    const page = await browser.newPage();
    await page.goto(request.url);
    const filename = `/ss/ss-${Date.now()}.png`;
    await page.screenshot({ path: filename });
    page.close()
    res.sendFile(filename);
  });
  app.listen(80, () => console.log("Example app listening on port 80!"));
}

(async () => {
  try {
    await main();
  } catch (e) {
    // Deal with the fact the chain failed
  }
})();
