// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";

type Company = {
  name: string;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Company>
) {
  res.status(200).json({ name: "John Doe" });
}
