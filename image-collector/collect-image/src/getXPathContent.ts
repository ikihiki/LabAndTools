import { Request, Response, response, Router } from "express";
import { BrowserService } from "./browserService";

export interface GetXPathContentParameter {
  url: string;
  waitXPath: string;
  getXPath: string;
  property?: string;
}

const router = Router();

export const getXPathContent = router.post(
  "/get-xpath-content",
  async (request: Request, respose: Response) => {
    try {
      const param = request.body as GetXPathContentParameter;
      const page = await BrowserService.getBrowser().newPage();
      await page.goto(param.url);
      await page.waitForXPath(param.waitXPath);
      const elements = await page.$x(param.getXPath);
      const result = [];
      for (const element of elements) {
        if (param.property) {
          const prop = await element.getProperty(param.property);
          result.push(await prop.jsonValue());
        } else {
          const props = await element.getProperties();
          const r = new Map<string, any>();
          for (const prop of props) {
            r.set(prop[0], await prop[1]);
          }
          result.push(r);
        }
      }
      await page.close();
      respose.status(200).json(result);
    } catch (e) {
      respose.status(500);
      respose.json({ message: e.message, stack: e.stack });
    }
  }
);
