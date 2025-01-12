# Cross-Site Scripting (XSS) Guide

## Introduction

Cross-Site Scripting (XSS) is a prevalent security vulnerability in web applications that allows attackers to inject malicious scripts into web pages viewed by users. This guide explains the types of XSS, common attack vectors, prevention techniques, and testing tools to help you mitigate this threat.

---

## What is XSS?

XSS enables attackers to execute malicious scripts in a victim's browser. These scripts can:

- Steal sensitive data such as cookies and session tokens.
- Deface web pages or redirect users to malicious websites.
- Perform unauthorized actions on behalf of a user.

---

## Types of XSS

### 1. Stored XSS (Persistent)
- **Description:** The malicious script is permanently stored on the target server, often in a database or message board.
- **Example:**
  An attacker posts the following script in a comment field:
  ```html
  <script>alert('Stored XSS');</script>
  ```
  When other users view the comment, the script executes in their browsers.

### 2. Reflected XSS (Non-Persistent)
- **Description:** The malicious script is reflected off a web application and executed immediately, typically through URL parameters or form inputs.
- **Example:**
  A crafted URL:
  ```
  http://example.com/search?q=<script>alert('Reflected XSS');</script>
  ```

### 3. DOM-Based XSS
- **Description:** The vulnerability lies in client-side scripts that manipulate the DOM without proper sanitization.
- **Example:**
  ```javascript
  var search = document.location.hash.substring(1);
  document.write("<h1>" + search + "</h1>");
  ```
  If the URL is:
  ```
  http://example.com/#<script>alert('DOM XSS');</script>
  ```
  The script executes when the browser processes the hash.

---

## Common XSS Attack Vectors

### Event Handlers
Injecting scripts via HTML event handlers such as `onclick`, `onerror`, or `onload`.
```html
<img src="invalid.jpg" onerror="alert('XSS');">
```

### Data URIs
Using `data:` URIs to execute scripts.
```html
<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=">Click here</a>
```

### JavaScript URIs
Leveraging the `javascript:` URI scheme.
```html
<a href="javascript:alert('XSS')">Click me</a>
```

---

## Prevention Techniques

1. **Input Validation:**
   - Enforce strict input validation to reject potentially harmful input.

2. **Output Encoding:**
   - Encode data before rendering it in the browser to neutralize special characters.

3. **Content Security Policy (CSP):**
   - Use a CSP header to restrict the sources from which scripts can be loaded.
   - **Example:**
     ```
     Content-Security-Policy: default-src 'self'; script-src 'self';
     ```

4. **Use HTTPOnly and Secure Cookies:**
   - Mark cookies as `HttpOnly` and `Secure` to prevent client-side scripts from accessing them.

5. **Framework-Specific Defenses:**
   - Use built-in XSS prevention mechanisms in frameworks like React, Angular, or Django.

---

## Testing for XSS Vulnerabilities

### Automated Tools

1. **Burp Suite:**
   - Intercept and modify HTTP requests to inject malicious payloads.

2. **OWASP ZAP:**
   - Scan web applications for XSS vulnerabilities.

3. **Arachni:**
   - A powerful web application security scanner with XSS detection capabilities.

### Manual Techniques

1. **Fuzzing:**
   - Inject various payloads like `<script>alert('XSS')</script>` into input fields and observe the response.

2. **Source Code Review:**
   - Check for improper input handling and unsafe DOM manipulations.

---

## Real-World Example

### Twitter XSS Vulnerability (2010)
An attacker exploited a Reflected XSS vulnerability in Twitter by crafting malicious tweets. Users who hovered over the tweets unknowingly executed JavaScript in their browsers, leading to potential account compromise.

---

## References

- [OWASP XSS Prevention Cheat Sheet](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [Google CSP Evaluator](https://csp-evaluator.withgoogle.com/)

---

This guide aims to provide a foundational understanding of XSS, helping you identify and prevent these vulnerabilities in your applications. Stay secure! 🚀
