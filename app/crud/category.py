from psycopg2.extras import RealDictCursor
from app.db.database import get_db_connection

class CategoryCRUD:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute("SELECT id, name FROM categories WHERE deleted_at IS NULL ORDER BY id ASC")
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def create(name: str):
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute("SELECT id FROM categories WHERE name = %s", (name,))
            existing = cursor.fetchone()
            
            if existing:
                cursor.execute(
                    "UPDATE categories SET deleted_at = NULL, updated_at = NOW() WHERE name = %s RETURNING id, name", 
                    (name,)
                )
            else:
                cursor.execute(
                    "INSERT INTO categories (name, created_at, updated_at) VALUES (%s, NOW(), NOW()) RETURNING id, name",
                    (name,)
                )
            conn.commit()
            return cursor.fetchone()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update(category_id: int, name: str):
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute(
                "UPDATE categories SET name = %s, updated_at = NOW() WHERE id = %s AND deleted_at IS NULL RETURNING id, name",
                (name, category_id)
            )
            conn.commit()
            return cursor.fetchone()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete(category_id: int):
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute(
                "UPDATE categories SET deleted_at = NOW() WHERE id = %s AND deleted_at IS NULL RETURNING id",
                (category_id,)
            )
            conn.commit()
            return cursor.fetchone()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()