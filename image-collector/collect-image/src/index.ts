import express from "express";
import { getScreenShot } from "./getScreenShoot";
import { getXPathContent } from "./getXPathContent";
import { env } from "process";
import { BrowserService } from "./browserService";

async function main() {
  await BrowserService.setup();
  const app = express();
  app.use(express.json());
  app.get("/", (req, res) => res.send("Hello world"));
  app.use(getScreenShot);
  app.use(getXPathContent);
  const port = Number(env.PORT) || 80;
  app.listen(port, () => console.log(`Example app listening on port ${port}!`));
  await BrowserService.close();
}

main();

