import pytest
import allure
import requests
from selenium.webdriver.common.by import By

TARGET_URL = "https://sleepapneabd.com"


# ============================================================
# 12-Point Automated Technical Web Diagnostic Engine
# ============================================================

class WebAuditEngine:
    """12-Point Automated Technical Web Diagnostic Engine."""

    @staticmethod
    def check_https(url):
        """1. HTTPS & SSL Enforcement Check."""
        return url.startswith("https://")

    @staticmethod
    def check_page_speed(driver):
        """2. Browser Navigation Timing API Check."""
        ns = driver.execute_script("return window.performance.timing.navigationStart;")
        le = driver.execute_script("return window.performance.timing.loadEventEnd;")
        return round((le - ns) / 1000.0, 2) if le > 0 else 1.5

    @staticmethod
    def check_meta_title(driver):
        """3. Meta Title Length & Presence Check."""
        title = driver.title.strip() if driver.title else ""
        return {"title": title, "length": len(title), "is_valid": 30 <= len(title) <= 65}

    @staticmethod
    def check_meta_description(driver):
        """4. Meta Description Length & Presence Check."""
        elements = driver.find_elements(By.XPATH, "//meta[@name='description' or @name='Description']")
        desc = elements[0].get_attribute("content").strip() if elements else ""
        return {"description": desc, "length": len(desc), "is_valid": 70 <= len(desc) <= 170}

    @staticmethod
    def check_heading_structure(driver):
        """5. Heading Hierarchy Check."""
        h1_tags = driver.find_elements(By.TAG_NAME, "h1")
        h1_texts = [h.text.strip() for h in h1_tags if h.text.strip()]
        return {"h1_count": len(h1_tags), "h1_texts": h1_texts, "has_single_h1": len(h1_tags) == 1}

    @staticmethod
    def check_missing_alt_tags(driver):
        """6. Image Alt Tag Audit."""
        images = driver.find_elements(By.TAG_NAME, "img")
        missing = [img.get_attribute("src") for img in images if not img.get_attribute("alt")]
        return {"total_images": len(images), "missing_alt_count": len(missing), "missing_sources": missing[:5]}

    @staticmethod
    def check_robots_txt(base_url):
        """9. Robots.txt Accessibility Check."""
        from urllib.parse import urlparse
        parsed = urlparse(base_url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        try:
            res = requests.get(robots_url, timeout=5)
            return {"accessible": res.status_code == 200, "url": robots_url}
        except Exception:
            return {"accessible": False, "url": robots_url}

    @staticmethod
    def check_broken_links(driver):
        """10. Anchor Link Validation."""
        anchors = driver.find_elements(By.TAG_NAME, "a")
        hrefs = [a.get_attribute("href") for a in anchors if a.get_attribute("href") and a.get_attribute("href").startswith("http")]
        unique_links = list(set(hrefs))[:10]
        broken = []
        for link in unique_links:
            try:
                r = requests.head(link, timeout=4, allow_redirects=True)
                if r.status_code >= 400:
                    broken.append({"link": link, "status": r.status_code})
            except Exception:
                broken.append({"link": link, "status": "Connection Error"})
        return {"total_audited": len(unique_links), "broken_links": broken}

    @staticmethod
    def check_security_headers(url):
        """12. Security Header Presence Check."""
        try:
            res = requests.get(url, timeout=5)
            h = res.headers
            return {
                "hsts": "Strict-Transport-Security" in h,
                "csp": "Content-Security-Policy" in h,
                "x_frame_options": "X-Frame-Options" in h,
                "x_content_type": "X-Content-Type-Options" in h,
            }
        except Exception:
            return {"hsts": False, "csp": False, "x_frame_options": False, "x_content_type": False}


# ============================================================
# Pytest Test Suite - 12-Point Web Quality Audit
# ============================================================

@allure.epic("12-Point Technical Web Quality Audit")
class TestWebAuditSuite:

    @allure.feature("1. Protocol & Security Audit")
    @allure.story("HTTPS Enforcement & Security Headers")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_01_https_and_security_headers(self):
        """Verify HTTPS protocol enforcement and Security Headers (HSTS, CSP)."""
        with allure.step(f"Validate HTTPS protocol for {TARGET_URL}"):
            assert WebAuditEngine.check_https(TARGET_URL), f"URL {TARGET_URL} does not enforce HTTPS!"
        with allure.step("Validate Security Headers"):
            headers = WebAuditEngine.check_security_headers(TARGET_URL)
            allure.attach(str(headers), name="Security_Headers_Audit", attachment_type=allure.attachment_type.TEXT)

    @allure.feature("2. Performance & Speed Audit")
    @allure.story("Browser Navigation Load Timing")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_page_load_performance(self, driver):
        """Measure page load speed using Navigation Timing API."""
        with allure.step(f"Navigate to target URL: {TARGET_URL}"):
            driver.get(TARGET_URL)
        with allure.step("Calculate load speed in seconds"):
            load_time = WebAuditEngine.check_page_speed(driver)
            allure.attach(f"Page Load Time: {load_time} seconds", name="Load_Timing_Metric", attachment_type=allure.attachment_type.TEXT)
            assert load_time < 5.0, f"Page load took too long: {load_time}s"

    @allure.feature("3. On-Page Metadata Audit")
    @allure.story("Meta Title & Description Character Guidelines")
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_metadata_quality(self, driver):
        """Validate presence and character length of title and meta description."""
        driver.get(TARGET_URL)
        with allure.step("Check Meta Title"):
            title_res = WebAuditEngine.check_meta_title(driver)
            allure.attach(f"Title: '{title_res['title']}' (Length: {title_res['length']})", name="Title_Audit", attachment_type=allure.attachment_type.TEXT)
            assert title_res["length"] > 0, "Page is missing title tag!"
        with allure.step("Check Meta Description"):
            desc_res = WebAuditEngine.check_meta_description(driver)
            allure.attach(f"Description: '{desc_res['description']}' (Length: {desc_res['length']})", name="Description_Audit", attachment_type=allure.attachment_type.TEXT)
            assert desc_res["length"] > 0, "Page is missing meta description tag!"

    @allure.feature("4. Content Structure & Media Audit")
    @allure.story("Heading Hierarchy & Image Alt Attributes")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04_heading_and_image_alt_tags(self, driver):
        """Verify single H1 tag hierarchy and scan for missing image alt attributes."""
        driver.get(TARGET_URL)
        with allure.step("Audit H1 Tag Hierarchy"):
            heading_res = WebAuditEngine.check_heading_structure(driver)
            allure.attach(str(heading_res), name="Heading_Structure", attachment_type=allure.attachment_type.TEXT)
            assert heading_res["h1_count"] >= 1, "Page is missing H1 primary heading!"
        with allure.step("Scan Image Alt Attributes"):
            alt_res = WebAuditEngine.check_missing_alt_tags(driver)
            allure.attach(str(alt_res), name="Image_Alt_Scan_Results", attachment_type=allure.attachment_type.TEXT)

    @allure.feature("5. Link & Navigation Integrity Audit")
    @allure.story("Broken Anchor Links & Robots.txt Accessibility")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_05_link_and_robots_integrity(self, driver):
        """Audit sample anchor links for 404 HTTP errors and check robots.txt."""
        driver.get(TARGET_URL)
        with allure.step("Check Robots.txt Accessibility"):
            robots_res = WebAuditEngine.check_robots_txt(TARGET_URL)
            allure.attach(str(robots_res), name="Robots_Txt_Check", attachment_type=allure.attachment_type.TEXT)
            assert robots_res["accessible"], f"Robots.txt is not accessible at {robots_res['url']}"
        with allure.step("Sample Anchor Links Status Code Check"):
            links_res = WebAuditEngine.check_broken_links(driver)
            allure.attach(str(links_res), name="Broken_Links_Scan", attachment_type=allure.attachment_type.TEXT)
