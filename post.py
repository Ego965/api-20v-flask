from database import get_db_connection

def get_all_posts():
    """Recupera todos los posts de la base de datos."""
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return posts

def get_post_by_id(post_id: int):
    """Recupera un solo post por su ID."""
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return post

def create_post(title: str, content: str):
    """Inserta un nuevo post en la base de datos."""
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()

def update_post(post_id: int, title: str, content: str):
    """Actualiza el título y contenido de un post existente."""
    conn = get_db_connection()
    conn.execute(
        'UPDATE posts SET title = ?, content = ? WHERE id = ?',
        (title, content, post_id)
    )
    conn.commit()
    conn.close()

def delete_post(post_id: int):
    """Elimina un post por su ID."""
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()