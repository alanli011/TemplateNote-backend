# Backend Endpoints

## Users

- GET /users/id = return specific user
- POST /users = sign up
- DELETE /users/id = delete specific user

### NoteBook

- GET /notebook = returns all notebooks
- GET /notebook/id = returns specific notebook
- POST /notebook = create notebook
- DELETE /notebook/id = delete specific notebook

### Notes

- GET /notebook_id/notes = returns all notes for specific notebook
- GET /notebook_id/notes/id = returns specific note for specific notebook
- PUT /notebook_id/notes/id = edits specific note
- DELETE /notebook_id/notes/id = deletes specific note

## Template

- GET /notes/templates = returns all templates for notes
- GET /notes/templates/id = returns specific tempalte
- POST /notes/templates = creates template for note
- DELETE /notes/templates/id = deletes specific template
- PUT /notes/templates/id = edits specific template

## Tags

- GET /tags = returns all tags
- GET /tags/id = returns specific tag
- POST /tags = creates a tag
- PUT /tags/id = edit specific tag
- DELETE /tags/id = delete specific tag
