import puppeteer from 'puppeteer';
import { google } from 'googleapis';
import url from 'url'; // Import the URL module for parsing URLs

const GET = async () => {
  const scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly'];
  const auth = new google.auth.JWT(
          "dashboard@dashboard-431521.iam.gserviceaccount.com",
          null,
          "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCn/9zGrrWkkR4F\nyi4Bq5PYMNpHvt230swtEGfJIeQ9Xs32fz3pt3vwitBLMYCiZgJxZ/70T+PGczyl\njnHq44INHOHlhtf8sot36KINA73dn8Jcys62jMCkETHO5XQ8Q+d9Z7t9p4FPabPi\nPZ+w0lcptt0D0kXSDvFMCLaZOx2knSmVKbolopk7hO6WdLzYbWgCvccjy4cwj1Gv\nS6VUaW6LbEPgedFjo/X+Kw8Kr1e85F719YvgFjKCLPZHerR3KfgzXBsjZC98Hqus\nuuiiCCz8zSq8xHI8xlfV81vB3+kqdJs504abCxSKgbQayU0eZMaD/ZiVJl0HvtIK\nj4IiYhWJAgMBAAECggEAUOt2HSEkDvtzOZiz5kwNr3GAglRWGWfovsALLZ8sf779\neAC8AqpFgYxrXfyfGBoIjTVpYaZlcT4qdRgSmPAywTwrNtJnkKkzcnNUMu6dcnW0\nOdvaC6XqWFyL4Ds3bJvMkeP4NEMNjwG8CnpiQ9pc75PMCz4qMU7PPS9pPI9z7Mia\nuSYpS98Jj7RwiRlJ7Gk2l0osqRxB7lB4i5Nu/oLTfKSFua4r3+c7v1oWuBEbchDu\nHbhvmk18/dWVc+NNteR8su1x2HKLivLdCFGvGDn60B53DvJF4SwZXofCOcBsXCMz\n7N7KUIYHo5pZVxiWODGH2cdm/8mU58TQkLyl2LXCrQKBgQDYm7G7blIBGh5kOobr\nmuDEZfgtiRhEJWs2/4TyysHlvRu2jRnVMK07udYpbd8wC4JnwP6kpwtlkLcjlW4I\nMpf61t8DtJUHwBnCsZ4YIj1/ntJRc2F3KmWIsT0fjTqfzfmPqsU1xuYggLmrLuHo\n/hzFQxuwu6oSFh9sDduWOk8bbwKBgQDGjSoGPdxYhyUwtbBepOo5th3f+Fw4QtPL\ncBtXmoxoSDZGBfO/hXzRGWRURMRiOC39J3cjy+q3T9pXQvK3h9rqbgdhbUww8W9J\nHs5I1xvOgsNs56MnjNGxOLOJX63CpVmkAUip7YRUnrmRSouJptDQ1fhCBSjrR0/4\nDA2Fb+hChwKBgCIIbGdvkPDdYrMKwxIXloMlJlY5ORfT7UGJ6iCfnNF04frPtqRZ\nbo54x15hBfUticK1fwzttguyLiQoIU6mbFycEBQr9lJua128vIM8Nf9sO81SXJj1\nj1hnyJvBe9mJ6lEZWrz1UEkBEKsFxbbu3iRcQ+iDw9fto+g9USgMZ0t/AoGAWXYX\nflJ3KuhRyH3E5xAVfUVidpz4KF1sApkTqMg5BW+sDKb36c6iq7BuNU360mqPxiX3\nF4j0y/3N2k2PAUTUTZaf+rT9hHv0cZTQy58op0bh+Prx14sqnFh5BKe4qiBIoI33\niKE9Y8dUw3M8Jhykr8QJJO4gPsqV7KS5nusKUpcCgYEAo6RTeFODVfQ5zEqb46aw\nqKheHW5v5RAkA6WREY70fkt49Z3xn87HKWyGm/cxu9vw1GHxR5wlXWFZ3UvBj5o9\nPgubL4+yE7em9UiyTLk/NObhnh4SdBXdrl/UJUt1gFYL2msPI5368fTmc7+yjAW6\nsPJ6P+7iGw+ahOQXeWxKc7o=\n-----END PRIVATE KEY-----\n",
          scopes
    );


  const sheets = google.sheets({ version: 'v4', auth });
  const spreadsheetId = '1C7fP0RZqZkj6EAAeeKz6bvr7F6r3z4o1Htc7eKPyOYE';
  const range = 'active deals!H9:H25'; // Adjust range as needed

  try {
    // Fetch data from Google Sheets
    const response = await sheets.spreadsheets.values.get({
      spreadsheetId,
      range,
    });

    // Extract URLs from the sheet
    const urls = response.data.values.map(item => item[0]);

    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    const results = [];

    for (const sheetUrl of urls) {
      // Parse the domain from the URL
      const parsedUrl = new URL(sheetUrl);
      const domain = parsedUrl.hostname;
      const domain_actual = domain.match(/www\.([^.]*)\.com/);
      // Construct the URL dynamically if needed
      const targetUrl = `https://www.cashbackmonitor.com/cashback-store/${domain_actual[1]}/`;

      await page.goto(targetUrl, { waitUntil: 'networkidle2' });

      // Extract data from the constructed URL
      const data = await page.evaluate(() => {
        const cashbackContainer = document.querySelector(".lo");
        const cashbackName = cashbackContainer ? cashbackContainer.querySelector("a").textContent : 'No cashback name found';
        const cashbackPercentage = document.querySelector("#ra0") ? document.querySelector("#ra0").textContent : 'No cashback percentage found';

        return {
          cashbackName,
          cashbackPercentage
        };
      });

      results.push({ url: data});
    }

    await browser.close();
    console.log(JSON.stringify(results))

    return new Response(JSON.stringify(results || "No data found"), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });

  } catch (error) {
    console.error('Error:', error);
    return new Response(JSON.stringify({ error: 'Something went wrong' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};

// Invoke the GET function
GET();

