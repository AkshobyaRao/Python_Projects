let webdriver = require('selenium-webdriver');
require("chromedriver")
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

export async function GET() {
  let driver;
  try {
    driver = await new webdriver.Builder().forBrowser('chrome').build();
    await driver.get('https://www.cashbackmonitor.com/cashback-store/dell-technologies/');
    await sleep(3000);

    let button = await driver.findElement(By.className("css-47sehv"));
    await sleep(3000);
    await button.click();
    await sleep(3000);

    let cashbackContainer = await driver.findElement(By.className("lo"));
    let cashbackNameElement = await cashbackContainer.findElement(By.css("a"));
    let cashbackPercentageElement = await driver.findElement(By.id("ra0"));

    let cashbackName = await cashbackNameElement.getText();
    let cashbackPercentage = await cashbackPercentageElement.getText();

    // Close the driver 
    await driver.quit();

    return new Response(JSON.stringify({ cashbackName, cashbackPercentage }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    console.error('Error:', error);
    if (driver) {
      await driver.quit();
    }
    return new Response(JSON.stringify({ error: 'Error accessing data' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}
