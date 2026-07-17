from playwright.sync_api import sync_playwright, TimeoutError

URL = "https://www.justdial.com/Lucknow/IT-Companies"

def scrape_justdial():
    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(
            headless=False,      # Keep False while debugging
            slow_mo=100
        )

        # Create browser context
        context = browser.new_context(
            viewport={"width": 1366, "height": 768},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            locale="en-US"
        )

        page = context.new_page()

        page.set_default_navigation_timeout(120000)
        page.set_default_timeout(120000)

        try:
            print("Opening Justdial...")

            page.goto(
                URL,
                wait_until="domcontentloaded",
                timeout=120000
            )

            page.wait_for_timeout(5000)

            print("Page Title:")
            print(page.title())

            # Scroll to load more results
            for i in range(5):
                page.mouse.wheel(0, 3000)
                page.wait_for_timeout(3000)

            print("Current URL:", page.url)

            # Save HTML
            html = page.content()

            with open("justdial.html", "w", encoding="utf-8") as f:
                f.write(html)

            print("HTML saved successfully.")

            # Save Screenshot
            page.screenshot(path="justdial.png", full_page=True)
            print("Screenshot saved.")

        except TimeoutError:
            print("Navigation timed out.")

        except Exception as e:
            print("Error:", e)

        finally:
            browser.close()


if __name__ == "_main_":
    scrape_justdial()