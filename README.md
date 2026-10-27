# Textbook Library

A separate textbook website for Years 7–12. It starts with an empty catalogue; no textbook files have been copied from other projects.

Features: title/author/ISBN search, subject and year filters, edition information, sorting, a saved bookshelf, and recently opened books. Bookmarks and recent history stay on the visitor's device.

## Add textbooks
Edit `site/catalog.json` and add one object for each textbook. Commit to main; GitHub Actions validates and publishes the site.

Example entry (documentation only; not included in the live collection):
```json
{
  "id": "unique-book-edition-id",
  "title": "Textbook title",
  "author": "Author name",
  "subject": "Physics ATAR",
  "subjectGroup": "Science",
  "years": [11, 12],
  "edition": "Third edition",
  "publisher": "Publisher name",
  "isbn": "ISBN if known",
  "format": "PDF",
  "description": "A short description.",
  "added": "2026-10-27",
  "url": "https://example.com/authorised-textbook-link"
}
```

Use `subjectGroup` for broad subject tabs: Science, Mathematics, English or Humanities. Other subjects remain searchable through the subject filter. An optional `cover` field accepts an HTTPS cover-image URL; without it the website generates a typographic cover.

Keep large original files in cloud storage and put their share link in the catalogue. The website does not grant access to private Drive files; their existing sharing settings still apply. Publisher links may require a separate account.

Direct uploads and admin approval are not connected. Google verification for the separate School Library backend remains paused; this project does not activate it.

## Checks
```sh
python3 scripts/validate.py
python3 scripts/test_catalog.py
node --check site/app.js
```

GitHub Pages uses the GitHub Actions source in Settings → Pages. No reuse licence over textbook content is granted. Include only files and links you are authorised to share.
