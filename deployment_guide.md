# Deployment Guide: Dr. Reddy's Attendance App via Render

This guide will help you deploy your FastAPi application to [Render](https://render.com/), a cloud hosting platform.

## Prerequisites

1. **GitHub Account**: You need a GitHub account to host your code.
2. **Render Account**: Sign up at [dashboard.render.com](https://dashboard.render.com/).

## Step 1: Push Code to GitHub

You need to push your code to a new GitHub repository.

1. Create a **new repository** on GitHub (e.g., `dr-reddys-attendance`).
2. Open your terminal in the project folder (`attendance_service`).
3. Initialize Git and push:

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/dr-reddys-attendance.git
    git push -u origin main
    ```

## Step 2: Deploy on Render

1. Log in to your **Render Dashboard**.
2. Click **"New +"** -> **"Web Service"**.
3. Select **"Build and deploy from a Git repository"**.
4. Connect your GitHub account and select the `dr-reddys-attendance` repository.
5. **Configure the Service**:
    * **Name**: `dr-reddys-attendance` (or similar)
    * **Region**: Any (e.g., Singapore, Frankfurt)
    * **Branch**: `main`
    * **Runtime**: `Python 3`
    * **Build Command**: `pip install -r requirements.txt`
    * **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
    * **Plan**: Free (ideal for demos)
6. Click **"Create Web Service"**.

## Step 3: Verify Deployment

1. Render will start building your app. It may take 2-3 minutes.
2. Once "Live", you will get a URL like `https://dr-reddys-attendance.onrender.com`.
3. **Open the App**:
    * Mobile App: `https://<YOUR-URL>/mobile`
    * Simulation Controls: `https://<YOUR-URL>/simulate`

## Testing the Deployment

* Open the `/mobile` link on your **OnePlus Pad** or Phone.
* Try the **Simulation Scenarios**:
  * **Holiday**: Select Jan 26th (Republic Day) -> Verify "Holiday Block".
  * **Weekend**: Select a Sunday -> Verify "Weekend Block".
  * **Past Date**: Select yesterday -> Verify "Past Date Block".
  * **Lockout**: Go to `/simulate`, toggle "System Lockout", try checking in today.

Your app is now cloud-hosted and ready for the demo! 🚀
