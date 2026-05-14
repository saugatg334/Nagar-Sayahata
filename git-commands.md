

# Git Workflow (Node Project)

## 🟢 1. First time setup (Clone project)
git clone <repo-url>
cd <project-folder>

---

## 🟢 2. Always start with latest code
git checkout main
git pull origin main

---

## 🟢 3. Create new feature branch
git checkout -b feature/your-task-name

Example:
git checkout -b feature/login-api

---

## 🟢 4. Work on project
(do your coding in Node project)

---

## 🟢 5. Check changes
git status

---

## 🟢 6. Add changes to staging
git add .

OR specific file:
git add filename

---

## 🟢 7. Commit changes
git commit -m "clear message about changes"

Example:
git commit -m "add login API"

---

## 🟢 8. Push branch to GitHub
git push origin feature/your-task-name

---

## 🟢 9. After PR merge → update main
git checkout main
git pull origin main

---

## 🟢 10. Merge (only if needed locally)
git checkout main
git merge feature/your-task-name
git push origin main

---

## 🟡 Optional (Rebase - advanced)
git checkout feature/your-task-name
git rebase main

---

# 🔥 Golden Rule Flow

Every new task:
git checkout main
git pull origin main
git checkout -b feature/new-task

Work:
git add .
git commit -m "message"
git push origin feature/new-task


