# How to Push to GitHub - Troubleshooting Guide

## Current Status
✅ Git repository initialized
✅ Files committed
✅ Remote configured: https://github.com/Utsavchauhan/todo-manager.git

## Common Issues and Solutions

### Issue 1: Authentication Required

GitHub requires authentication. You have several options:

#### Solution A: Use Personal Access Token (Recommended)

1. **Create a Personal Access Token:**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Name: "Todo Manager"
   - Select scope: `repo` (check the box)
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again!)

2. **Push using the token:**
   ```bash
   cd "/Users/utsav.chauhan/Todo Manager"
   git push -u origin main
   ```
   - Username: `Utsavchauhan`
   - Password: **Paste your Personal Access Token** (not your GitHub password)

#### Solution B: Use SSH Instead of HTTPS

1. **Check if you have SSH keys:**
   ```bash
   ls -la ~/.ssh/id_rsa.pub
   ```

2. **If you don't have SSH keys, generate them:**
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   # Press Enter to accept default location
   # Press Enter twice for no passphrase (or set one)
   ```

3. **Add SSH key to GitHub:**
   ```bash
   cat ~/.ssh/id_rsa.pub
   # Copy the output
   ```
   - Go to: https://github.com/settings/keys
   - Click "New SSH key"
   - Paste your public key
   - Click "Add SSH key"

4. **Change remote to SSH:**
   ```bash
   cd "/Users/utsav.chauhan/Todo Manager"
   git remote set-url origin git@github.com:Utsavchauhan/todo-manager.git
   git push -u origin main
   ```

#### Solution C: Use GitHub CLI (if installed)

```bash
gh auth login
cd "/Users/utsav.chauhan/Todo Manager"
git push -u origin main
```

### Issue 2: Repository Doesn't Exist on GitHub

Make sure the repository exists:
1. Go to: https://github.com/Utsavchauhan/todo-manager
2. If you see 404, create it:
   - Go to: https://github.com/new
   - Repository name: `todo-manager`
   - **DO NOT** initialize with README
   - Click "Create repository"

### Issue 3: Wrong Username/Case Sensitivity

GitHub usernames are case-sensitive. Make sure:
- Your GitHub username is exactly: `Utsavchauhan` (check at https://github.com/settings/profile)

If different, update the remote:
```bash
git remote set-url origin https://github.com/YOUR_ACTUAL_USERNAME/todo-manager.git
```

## Quick Push Commands

### Using HTTPS (with Personal Access Token):
```bash
cd "/Users/utsav.chauhan/Todo Manager"
git push -u origin main
# Enter username: Utsavchauhan
# Enter password: YOUR_PERSONAL_ACCESS_TOKEN
```

### Using SSH:
```bash
cd "/Users/utsav.chauhan/Todo Manager"
git remote set-url origin git@github.com:Utsavchauhan/todo-manager.git
git push -u origin main
```

## Verify Push

After pushing, check:
- https://github.com/Utsavchauhan/todo-manager
- You should see all your files there

## Still Having Issues?

1. Check if repository exists: https://github.com/Utsavchauhan/todo-manager
2. Verify your GitHub username is correct
3. Make sure you have a Personal Access Token with `repo` scope
4. Try using SSH instead of HTTPS

