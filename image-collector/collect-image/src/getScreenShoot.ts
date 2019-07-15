import { Request, Response, Router } from "express";
import { BrowserService } from "./browserService";

export interface GetScreenShotParameter {
  url: string;
}

const router = Router();

export const getScreenShot = router.post(
  "/get-screen-shot",
  async (request, respose) => {
    const param = request.body as GetScreenShotParameter;
    const page = await BrowserService.getBrowser().newPage();
    await page.goto(param.url);
    const filename = `/ss/ss-${Date.now()}.png`;
    await page.screenshot({ path: filename });
    page.close();
    respose.sendFile(filename);
  }
);
