from fastapi import APIRouter, HTTPException, Depends
from typing import List

import schemas
import auth
from database import get_db_connection

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=List[schemas.TaskResponse])
def get_tasks(current_user_email: str = Depends(auth.get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE owner_email = ?", (current_user_email,)
    )
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


@router.post("/", response_model=schemas.TaskResponse)
def create_task(
    data: schemas.TaskCreate,
    current_user_email: str = Depends(auth.get_current_user),
):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, completed, owner_email) VALUES (?, ?, ?)",
        (data.title, False, current_user_email),
    )
    conn.commit()
    new_task_id = cursor.lastrowid
    conn.close()

    return {
        "id": new_task_id,
        "title": data.title,
        "completed": False,
        "owner_email": current_user_email,
    }


def _get_owned_task_or_404(cursor, task_id: int, current_user_email: str):
    """Shared helper: fetches a task and ensures it belongs to the current user."""
    cursor.execute(
        "SELECT * FROM tasks WHERE id = ? AND owner_email = ?",
        (task_id, current_user_email),
    )
    task = cursor.fetchone()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.get("/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, current_user_email: str = Depends(auth.get_current_user)):
    conn = get_db_connection()
    cursor = conn.cursor()

    task = _get_owned_task_or_404(cursor, task_id, current_user_email)
    conn.close()

    return dict(task)


@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    data: schemas.TaskUpdate,
    current_user_email: str = Depends(auth.get_current_user),
):
    conn = get_db_connection()
    cursor = conn.cursor()

    task = _get_owned_task_or_404(cursor, task_id, current_user_email)

    new_title = data.title if data.title is not None else task["title"]
    new_completed = (
        data.completed if data.completed is not None else bool(task["completed"])
    )

    cursor.execute(
        "UPDATE tasks SET title = ?, completed = ? WHERE id = ?",
        (new_title, new_completed, task_id),
    )
    conn.commit()
    conn.close()

    return {
        "id": task_id,
        "title": new_title,
        "completed": new_completed,
        "owner_email": current_user_email,
    }


@router.delete("/{task_id}")
def delete_task(
    task_id: int, current_user_email: str = Depends(auth.get_current_user)
):
    conn = get_db_connection()
    cursor = conn.cursor()

    _get_owned_task_or_404(cursor, task_id, current_user_email)

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    return {"message": "Task deleted successfully"}