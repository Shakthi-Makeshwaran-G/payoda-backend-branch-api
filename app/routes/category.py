from fastapi import APIRouter, HTTPException, status
from app.schemas.category import CategoryCreateRequest, CategoryUpdateRequest
from app.crud.category import CategoryCRUD

router = APIRouter(prefix="/api/v1/categories", tags=["Categories"])

@router.get("")
def read_categories():
    try:
        rows = CategoryCRUD.get_all()
        return {"success": True, "message": "Categories fetched successfully", "data": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"success": False, "message": "Server Error", "raw_error_message": str(e)})

@router.post("", status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreateRequest):
    try:
        new_item = CategoryCRUD.create(payload.name)
        return {"success": True, "message": "Category created successfully", "data": new_item}
    except Exception as e:
        if "unique constraint" in str(e).lower():
            raise HTTPException(status_code=400, detail={"success": False, "message": "Category name already exists"})
        raise HTTPException(status_code=500, detail={"success": False, "message": "Server Error", "raw_error_message": str(e)})

@router.put("/{category_id}")
def update_category(category_id: int, payload: CategoryUpdateRequest):
    try:
        updated_item = CategoryCRUD.update(category_id, payload.name)
        if not updated_item:
            raise HTTPException(status_code=404, detail={"success": False, "message": "Category not found or inactive"})
        return {"success": True, "message": "Category updated successfully", "data": updated_item}
    except HTTPException as he:
        raise he
    except Exception as e:
        if "unique constraint" in str(e).lower():
            raise HTTPException(status_code=400, detail={"success": False, "message": "Target name already taken"})
        raise HTTPException(status_code=500, detail={"success": False, "message": "Server Error", "raw_error_message": str(e)})

@router.delete("/{category_id}")
def delete_category(category_id: int):
    try:
        deleted_item = CategoryCRUD.delete(category_id)
        if not deleted_item:
            raise HTTPException(status_code=404, detail={"success": False, "message": "Category not found or already deleted"})
        return {"success": True, "message": "Category deleted successfully", "data": {"id": category_id}}
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail={"success": False, "message": "Server Error", "raw_error_message": str(e)})