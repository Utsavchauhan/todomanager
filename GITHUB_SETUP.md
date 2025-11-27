# How to Push to GitHub

## Step 1: Initialize Git Repository (if not already done)

```bash
cd "/Users/utsav.chauhan/Todo Manager"
git init
```

## Step 2: Add All Files

```bash
git add .
```

## Step 3: Create Initial Commit

```bash
git commit -m "Initial commit: Python Todo Manager with Flask and SQLite"
```

## Step 4: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `todo-manager` (or any name you prefer)
3. Description: "A simple Todo Manager built with Python Flask and SQLite"
4. Choose Public or Private
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

## Step 5: Add Remote and Push

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/todo-manager.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Alternative: Using SSH (if you have SSH keys set up)

```bash
git remote add origin git@github.com:YOUR_USERNAME/todo-manager.git
git branch -M main
git push -u origin main
```

## Quick One-Liner Setup

If you want to do it all at once:

```bash
cd "/Users/utsav.chauhan/Todo Manager"
git init
git add .
git commit -m "Initial commit: Python Todo Manager with Flask and SQLite"
git remote add origin https://github.com/YOUR_USERNAME/todo-manager.git
git branch -M main
git push -u origin main
```

## Troubleshooting

### If you get "remote origin already exists":
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/todo-manager.git
```

### If you need to authenticate:
- GitHub now requires Personal Access Token instead of password
- Generate token: https://github.com/settings/tokens
- Use token as password when prompted

### If push is rejected:
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

## Future Updates

After making changes:

```bash
git add .
git commit -m "Your commit message"
git push
```

