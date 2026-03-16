# DeepCor Website

A modern, responsive website for the DeepCor fMRI denoising tool, hosted on GitHub Pages.

## 🚀 How to View Locally

You can view the website on your local machine before pushing changes to GitHub.

### Option 1: Using Python (Recommended)
If you have Python installed (Mac comes with it), run this simple command in the project folder:

1. Open your terminal.
2. Navigate to this folder:
   ```bash
   cd /Users/aidasaglinskas/Desktop/deepcor-webpage-github
   ```
3. Start a local server:
   ```bash
   python3 -m http.server
   ```
4. Open your browser and go to: `http://localhost:8000`

### Option 2: Using VS Code Live Server
If you use VS Code:
1. Open the project in VS Code.
2. Install the "Live Server" extension.
3. Right-click `index.html` and select **"Open with Live Server"**.

## 🌐 How to Deploy to GitHub Pages

1. **Push your changes** to the GitHub repository:
   ```bash
   git add .
   git commit -m "Update website content"
   git push origin main
   ```

2. **Configure GitHub Pages** (if not already done):
   - Go to the repository on GitHub.
   - Click **Settings** > **Pages** (in the sidebar).
   - Under "Build and deployment", select **Source** -> **Deploy from a branch**.
   - Select **Branch** -> `main` and folder `/ (root)`.
   - Click **Save**.

3. Your site will be live at `https://[your-username].github.io/[repo-name]/`.
