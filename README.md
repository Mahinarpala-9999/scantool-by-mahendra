# ScanTool

ScanTool is your all-in-one companion for web security scanning. It helps you uncover vulnerabilities and generate detailed reports with ease. With ScanTool, you can perform various types of scans, including Nmap, Nikto, and WPScan, all from one place.

## Features

- **Nmap Scanning**: Quickly detect open ports and services on your network.
- **Nikto Scanning**: Find known vulnerabilities in your web servers.
- **WPScan**: Check WordPress sites for common security issues.
- **Dirsearch**: Discover hidden directories and files through brute-forcing.
- **Full Scan**: Run a comprehensive scan using multiple techniques.

## Project Motivation and Background

ScanTool was created to make web security assessments easier and more accessible. The goal is to provide a simple yet powerful tool for security professionals and enthusiasts to identify potential vulnerabilities in their web applications and networks. By combining multiple scanning techniques, ScanTool saves time and effort in conducting thorough security checks.

## Installation

Here's how you can get Mahitool up and running on your system:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/mahitool.git
   cd ScanTool
   ```

2. Run the installation script:
   ```sh
   ./install.sh
   ```

3. Install the required Python packages:
   ```sh
   pip install -r conf/requirements.txt
   ```

## Detailed Usage Examples

Using Mahitool is straightforward. Here are some examples to get you started:

1. **Nmap Scan**:
   ```sh
   python webmap.py --nmap 192.168.1.1
   ```
   This command performs an Nmap scan on the IP address 192.168.1.1.

2. **Nikto Scan**:
   ```sh
   python webmap.py --nikto http://example.com
   ```
   Run this to check for known vulnerabilities on the web server at http://example.com.

3. **WPScan**:
   ```sh
   python webmap.py --wpscan http://example.com
   ```
   Use this to scan a WordPress site for security issues.

## Configuration Options

You can customize Mahitool by editing the `conf/conf.py` file. Here are some options you can adjust:

- **SCAN_TIMEOUT**: Set the timeout duration for scans.
- **OUTPUT_DIR**: Specify where scan reports should be saved.
- **NMAP_OPTIONS**: Customize options for Nmap scans.
- **NIKTO_OPTIONS**: Adjust options for Nikto scans.

## Dependencies

ScanTool relies on the following tools and libraries:

- Python 3.8 or higher
- Nmap
- Nikto
- WPScan

Make sure these are installed and accessible from your command line.

## Output Explanation

After running a scan, you'll find the reports in the `reports/` directory. Here's what each type of report includes:

- **Nmap Reports**: Details about open ports, services, and possible vulnerabilities.
- **Nikto Reports**: Information on known vulnerabilities in the target web server.
- **WPScan Reports**: Security issues specific to WordPress installations.

These reports provide insights into the security status of your targets, helping you take appropriate actions.

