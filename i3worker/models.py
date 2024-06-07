from uuid import UUID
from pydantic import (BaseModel, ConfigDict, Field)


class Page(BaseModel):
    id: UUID
    number: int
    document_version_id: UUID

    # Config
    model_config = ConfigDict(from_attributes=True)


class DocumentVersion(BaseModel):
    id: UUID
    number: int
    file_name: str | None = None
    size: int = 0
    page_count: int = 0
    document_id: UUID
    pages: list[Page] = []

    # Config
    model_config = ConfigDict(from_attributes=True)


class Document(BaseModel):
    id: UUID
    versions: list[DocumentVersion] = []

    # Config
    model_config = ConfigDict(from_attributes=True)
