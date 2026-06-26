from pydantic import BaseModel, Field

class CategoryCreateRequest(BaseModel):
    name: str = Field(..., max_length=100, description="Category display name")

class CategoryUpdateRequest(BaseModel):
    name: str = Field(..., max_length=100, description="Updated category display name")